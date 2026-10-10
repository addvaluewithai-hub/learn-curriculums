#!/usr/bin/env python3
"""Hydrate pinned B01 factory takes in a temporary CI workspace, no new TTS."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import io
import json
import os
from pathlib import Path
import tempfile
import urllib.error
import urllib.request
from urllib.parse import urlsplit
import zipfile
from common import ROOT, clips_for, load_lesson, read_json, require, sha256, write_json
from audio import collect
from validate import validate_lesson
from statics_b01_stage06_preflight import manifest, LESSONS

FACTORY="addvaluewithai-hub/gemini-tts"
URL="https://api.github.com/repos/"+FACTORY+"/actions/artifacts"
MAX_ZIP=14000000

def api_json(url,token):
    require(url.startswith("https://api.github.com/repos/"+FACTORY+"/actions/artifacts"),
            "Cross-repo GitHub API restriction")
    headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"}
    if token:headers["Authorization"]="Bearer "+token
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=35) as r:
        return json.load(r)

def all_artifacts(token,read=api_json):
    mapping={}
    page=1
    while page<=5:
        obj=read(URL+"?per_page=100&page="+str(page),token)
        rows=obj.get("artifacts",[])
        for item in rows:
            if item.get("name","").startswith("tts-") and not item.get("expired",True):
                if item["name"] in mapping: raise ValueError("Duplicate factory artifact "+item["name"])
                mapping[item["name"]]=item
        if len(rows)<100:break
        page+=1
    return mapping

class NoFollow(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):
        return None

def archive_bytes(url,token):
    """Fetch a GitHub API archive, stripping the bearer token at the blob redirect."""
    require(url.startswith("https://api.github.com/repos/"+FACTORY+"/actions/artifacts/") and
            url.endswith("/zip"),"Unexpected factory artifact URL")
    headers={"Accept":"application/vnd.github+json"}
    if token:headers["Authorization"]="Bearer "+token
    request=urllib.request.Request(url,headers=headers)
    opener=urllib.request.build_opener(NoFollow())
    try:
        response=opener.open(request,timeout=45)
    except urllib.error.HTTPError as error:
        if error.code not in (301,302,303,307,308):raise
        dest=error.headers.get("Location","")
        parsed=urlsplit(dest)
        require(parsed.scheme=="https" and parsed.hostname and
                (parsed.hostname.endswith(".actions.githubusercontent.com") or
                 parsed.hostname.endswith(".blob.core.windows.net") or
                 parsed.hostname.endswith(".githubusercontent.com")),
                "Unexpected artifact download host")
        # New request: never forward token to blob storage host.
        response=urllib.request.urlopen(urllib.request.Request(dest),timeout=50)
    with response as r:
        data=r.read(MAX_ZIP+1)
        require(len(data)<=MAX_ZIP,"Factory artifact exceeds permitted size")
        return data

def original_factory_result(zipped,job_id):
    with zipfile.ZipFile(io.BytesIO(zipped)) as archive:
        files=archive.namelist()
        require(files.count("result.json")==1,"Missing exact original result.json")
        require(len(files)<=12,"Unexpected factory artifact structure")
        info=archive.getinfo("result.json")
        require(info.file_size<100000,"Factory result metadata unexpectedly large")
        obj=json.loads(archive.read("result.json"))
    require(obj.get("id")==job_id and obj.get("status")=="completed",
            "Wrong or unfinished factory result")
    require(obj.get("audio_url","").startswith("https://res.cloudinary.com/") and
            obj.get("transcript_url","").startswith("https://res.cloudinary.com/"),
            "Invalid original factory delivery URLs")
    return obj

def chosen(rows,limit):
    if limit==0:return rows
    # Smoke test samples first ordinary narration and first bilingual feedback.
    selected=[next(x for x in rows if x["lessonId"]=="ems-y1-foundations-models" and x["clipId"]=="N01"),
              next(x for x in rows if x["lessonId"]=="ems-y1-newton-gravity" and x["clipId"]=="F02")]
    require(limit in (1,2),"Smoke --limit only supports 1 or 2; zero selects all")
    return selected[:limit]

def import_one(root,row,clip,artifact,token,download=archive_bytes):
    result=original_factory_result(download(artifact["archive_download_url"],token),row["jobId"])
    meta=result.get("metadata",{})
    require(meta.get("clipId")==row["clipId"] and
            meta.get("lessonId")==row["lessonId"] and
            meta.get("curriculumId")=="engineering-mechanics-statics-y1" and
            meta.get("role")==clip["role"] and
            meta.get("scriptHash")==sha256(clip["script"]),
            "Factory original result/script identity mismatch")
    require(result["audio_url"]==row["wav"] and
            result["transcript_url"]==row["transcript"],
            "Factory original delivery does not match accepted Cloudinary take")
    lesson_dir=Path(root)/"curricula"/"engineering-mechanics-statics-y1"/"lessons"/row["lessonId"]
    job_file=lesson_dir/"jobs"/(row["jobId"]+".json")
    if not job_file.is_file():
        config=read_json(Path(root)/"production.json")["audio"]
        req={"text":clip["script"],"voice":config["voice"],"style":config["style"],
             "routing":config["routing"],"format":"wav","sample_rate":config["sampleRate"],
             "transcript":{"language_codes":config["languageCodes"],"write_vtt":True},
             "metadata":{"curriculumId":"engineering-mechanics-statics-y1",
                         "lessonId":row["lessonId"],"clipId":row["clipId"],
                         "role":clip["role"],"scriptHash":sha256(clip["script"])}}
        write_json(job_file,{"event_type":"tts.generate",
                   "client_payload":{"job_id":row["jobId"],"request":req}},exclusive=True)
    with tempfile.TemporaryDirectory(prefix="b01result-") as temp:
        result_file=Path(temp)/"result.json"
        write_json(result_file,result)
        collected=collect(root,str(job_file.relative_to(root)),str(result_file))
    receipt=read_json(lesson_dir/"media"/row["clipId"]/"receipt.json")
    require(collected["status"]=="delivered-structure-verified" and
            receipt["jobId"]==row["jobId"],"Failed selected-media import")
    return {"lessonId":row["lessonId"],"clipId":row["clipId"],"jobId":row["jobId"],
            "durationMs":receipt["durationMs"],"audioHash":receipt["audioHash"],
            "transcriptHash":receipt["transcriptHash"],
            "warnings":collected["warnings"],"source":"original-github-factory-artifact",
            "humanListening":"user-approved-general-2026-10-10",
            "semanticTimingReviewed":False}

def run(root=ROOT,limit=2,token=None,read=api_json,download=archive_bytes,workers=4):
    index,canonical=manifest(root)
    rows=chosen(index["assets"],limit)
    artifacts=all_artifacts(token,read)
    require(all("tts-"+x["jobId"] in artifacts for x in rows),
            "Factory artifacts missing/expired; stop before synthetic provenance")
    out,failed=[],[]
    with ThreadPoolExecutor(max_workers=workers) as executor:
        jobs={executor.submit(import_one,root,row,canonical[(row["lessonId"],row["clipId"])],
            artifacts["tts-"+row["jobId"]],token,download):row for row in rows}
        for future in as_completed(jobs):
            row=jobs[future]
            try:out.append(future.result())
            except Exception as exc:failed.append({"clipId":row["clipId"],
                "lessonId":row["lessonId"],"error":str(exc)})
    out.sort(key=lambda x:(x["lessonId"],x["clipId"]))
    stages={}
    for lesson in sorted(set(x["lessonId"] for x in rows)):
        if len([x for x in rows if x["lessonId"]==lesson])==LESSONS[lesson] and not failed:
            stages[lesson]=validate_lesson(root,"engineering-mechanics-statics-y1",lesson,"media")
    return {"expected":len(rows),"imported":len(out),"failed":failed,
        "fullLessonMediaValidation":{x:y["valid"] for x,y in stages.items()},
        "resultProvenance":"original factory GitHub Actions result.json",
        "publicationApproved":False,"timedPreviewApproved":False,"clips":out}

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--limit",type=int,default=2,choices=(0,1,2))
    p.add_argument("--output",required=True,type=Path)
    args=p.parse_args()
    try:
        result=run(limit=args.limit,token=os.environ.get("GH_TOKEN"))
        write_json(args.output,result)
        print(json.dumps({k:result[k] for k in ("expected","imported","failed",
            "fullLessonMediaValidation","publicationApproved")},ensure_ascii=False))
        raise SystemExit(0 if result["expected"]==result["imported"] and not result["failed"] else 1)
    except Exception as e:
        print("STAGE 06 ORIGINAL-ARTIFACT COLLECTOR: "+str(e),file=__import__("sys").stderr)
        raise SystemExit(1)
