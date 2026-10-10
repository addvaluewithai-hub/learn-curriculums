#!/usr/bin/env python3
"""Evidence-only B01 Stage06 media audit; does not certify listening/timing."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import io
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit
from urllib.request import urlopen
import wave
from common import ROOT, clips_for, load_lesson, read_json, sha256, write_json

COURSE="engineering-mechanics-statics-y1"
LESSONS={"ems-y1-foundations-models":22,"ems-y1-newton-gravity":25,
         "ems-y1-units-conversions":22}
MAX_WAV=8000000
MAX_TEXT=1000000


def require(ok,message):
    if not ok:
        raise ValueError(message)


def valid_url(url,suffix):
    require(isinstance(url,str),"Expected URL")
    p=urlsplit(url)
    require(p.scheme=="https" and p.hostname=="res.cloudinary.com" and p.port is None
            and p.path.startswith("/as9o12al/") and p.path.endswith(suffix)
            and not p.query and not p.fragment and ".." not in p.path,
            "Unsafe/unknown Cloudinary media URL")


def fetch(url,maximum):
    suffix=".wav" if maximum==MAX_WAV else ".json" if url.endswith(".json") else ".vtt"
    valid_url(url,suffix)
    with urlopen(url,timeout=35) as response:
        valid_url(response.geturl(),suffix)
        data=response.read(maximum+1)
        require(len(data)<=maximum,"Media size too large")
        return data


def manifest(root=ROOT):
    index=read_json(Path(root)/"curricula"/COURSE/"blocks"/"B01"/"AUDIO_ASSETS.json")
    require(index.get("schemaVersion")==1 and index.get("courseId")==COURSE
            and index.get("blockId")=="B01" and index.get("reviewStatus")=="untested",
            "Invalid B01 media index or unsupported human review status")
    canonical={}
    for lesson_id,count in LESSONS.items():
        _,lesson,scenes=load_lesson(root,COURSE,lesson_id)
        clips=clips_for(scenes)
        require(lesson["id"]==lesson_id and len(clips)==count,"Canonical lesson changed")
        for clip in clips:
            key=(lesson_id,clip["id"])
            require(key not in canonical,"Duplicate source clip")
            canonical[key]=clip
    rows=index["assets"]
    require(len(rows)==len(canonical)==69,"Expected 69 delivered clips")
    seen=set()
    for row in rows:
        key=(row["lessonId"],row["clipId"])
        require(key in canonical and key not in seen,"Unexpected/duplicate source clip")
        seen.add(key)
        job=row["jobId"]
        require(job.startswith(key[0]+"-"+key[1]+"-") and row["reviewStatus"]=="untested",
                "Job/clip mismatch or manufactured audio approval")
        for field,suffix in (("wav",".wav"),("transcript",".transcript.json"),
                             ("vtt",".transcript.vtt")):
            valid_url(row[field],suffix)
            require(row[field].split("/gemini-tts/")[-1]==job+suffix,
                    "Media URL does not match the exact job ID")
    return index,canonical


def audit_clip(row,clip,wav_bytes,transcript_bytes,vtt_bytes):
    require(len(wav_bytes)==row["audioBytes"],"WAV bytes changed from provider index")
    with wave.open(io.BytesIO(wav_bytes),"rb") as wav:
        require(wav.getframerate()==24000 and wav.getsampwidth()==2 and
                wav.getnchannels()==1 and wav.getcomptype()=="NONE" and wav.getnframes()>0,
                "Unexpected WAV format or empty audio")
        duration=wav.getnframes()*1000/wav.getframerate()
    tr=json.loads(transcript_bytes)
    # Factory flattens bilingual sentence breaks to spaces for transcription.
    # Only whitespace normalization is permitted; all words/math must remain exact.
    source_text=tr.get("source_text","")
    require(tr.get("schema_version")==1 and tr.get("type")=="word_timestamps" and
            isinstance(source_text,str) and
            " ".join(source_text.split())==" ".join(clip["script"].split()),
            "Transcript source words differ from canonical spoken script")
    require(isinstance(tr.get("alignment_mode"),str) and tr["alignment_mode"] and
            isinstance(tr.get("recognized_text"),str) and tr["recognized_text"].strip(),
            "Missing ASR evidence/provenance")
    words=tr.get("words")
    require(isinstance(words,list) and words and tr.get("word_count")==len(words),
            "Missing/invalid ASR words")
    td=tr.get("duration_ms")
    require(isinstance(td,(int,float)) and not isinstance(td,bool) and
            math.isfinite(td) and 0<td<=duration+1,"Transcript extends past real WAV")
    previous=-1
    for i,word in enumerate(words):
        start,end=word.get("start_ms"),word.get("end_ms")
        require(isinstance(start,(int,float)) and isinstance(end,(int,float)) and
                math.isfinite(start) and math.isfinite(end) and
                0<=start<end<=td and start>=previous,
                "Invalid ASR word offset "+str(i))
        require(isinstance(word.get("text"),str) and word["text"].strip(),"Blank ASR word")
        previous=start
    require(vtt_bytes.decode("utf-8-sig").startswith("WEBVTT"),"Invalid VTT header")
    latin=lambda v:set(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?",v.casefold()))
    missing=sorted(latin(clip["script"])-latin(" ".join(w["text"] for w in words)))
    warnings=[]
    if missing: warnings.append("ASR_UNTIMED_ENGLISH_CHECK_AUDIO_NOT_SILENCE")
    if duration-td>250: warnings.append("TRAILING_WAV_AUDIO_REVIEW")
    if words[0]["start_ms"]>3000: warnings.append("LATE_ASR_START_REVIEW")
    return {"lessonId":row["lessonId"],"clipId":row["clipId"],"jobId":row["jobId"],
            "wavDurationMs":round(duration,3),"transcriptDurationMs":td,
            "scriptHash":sha256(clip["script"]),
            "audioHash":hashlib.sha256(wav_bytes).hexdigest(),
            "transcriptHash":hashlib.sha256(transcript_bytes).hexdigest(),
            "vttHash":hashlib.sha256(vtt_bytes).hexdigest(),
            "wordCount":len(words),"sourceWhitespaceNormalized":source_text!=clip["script"],
            "missingEnglishTokensInASR":missing,
            "warnings":warnings,"technicalDeliveryVerified":True,
            "humanListening":"untested","wordCuesReviewed":False}


def audit_remote(row,clip,downloader=fetch):
    return audit_clip(row,clip,downloader(row["wav"],MAX_WAV),
                      downloader(row["transcript"],MAX_TEXT),
                      downloader(row["vtt"],MAX_TEXT))


def run(root=ROOT,output=None,workers=6,downloader=fetch):
    index,clips=manifest(root)
    completed,errors=[],[]
    with ThreadPoolExecutor(max_workers=workers) as executor:
        tasks={executor.submit(audit_remote,row,clips[(row["lessonId"],row["clipId"])],downloader):
               row for row in index["assets"]}
        for task in as_completed(tasks):
            row=tasks[task]
            try: completed.append(task.result())
            except Exception as error:
                errors.append({"lessonId":row["lessonId"],"clipId":row["clipId"],"error":str(error)})
    completed.sort(key=lambda v:(v["lessonId"],v["clipId"]))
    errors.sort(key=lambda v:(v["lessonId"],v["clipId"]))
    report={"schemaVersion":1,"kind":"B01-stage06-preflight-not-human-review",
            "sourceCommit":index["sourceCommit"],"expected":69,"checked":len(completed),
            "failed":len(errors),"valid":len(completed)==69 and not errors,
            "warningClips":sum(bool(c["warnings"]) for c in completed),
            "asrEnglishWarningClips":sum(bool(c["missingEnglishTokensInASR"]) for c in completed),
            "wavDurationTotalMs":round(sum(c["wavDurationMs"] for c in completed),3),
            "audioReceiptsSelected":False,"timingReviewed":False,
            "visualPlaybackReviewed":False,"publicationApproved":False,
            "clips":completed,"errors":errors}
    if output:write_json(output,report)
    return report


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--workers",type=int,default=6)
    args=p.parse_args()
    try:
        r=run(output=args.output,workers=args.workers)
        print(json.dumps({k:r[k] for k in ("expected","checked","failed","valid",
            "warningClips","asrEnglishWarningClips","wavDurationTotalMs",
            "audioReceiptsSelected","timingReviewed","publicationApproved")},indent=2))
        sys.exit(0 if r["valid"] else 1)
    except Exception as exc:
        print("STAGE06 PREFLIGHT ERROR: "+str(exc),file=sys.stderr)
        sys.exit(1)
