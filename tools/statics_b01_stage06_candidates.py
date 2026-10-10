#!/usr/bin/env python3
"""B01 exact ASR cue *candidates*, never reviewed timing.json."""
import argparse
import json
from pathlib import Path
import shutil
from common import ROOT, clips_for, load_lesson, read_json, require, sha256, write_json
from media import check_receipt, tokens
from validate import validate_lesson

COURSE="engineering-mechanics-statics-y1"
LESSONS=["ems-y1-foundations-models","ems-y1-newton-gravity","ems-y1-units-conversions"]

def find_spans(words,phrase):
    """Find exact normalized token sequences among contiguous ASR word spans."""
    wanted=tokens(phrase)
    if not wanted:return []
    matches=[]
    for start in range(len(words)):
        actual=[]
        for end in range(start,min(len(words),start+len(wanted)+5)):
            actual.extend(tokens(words[end]["text"]))
            if actual==wanted:
                matches.append((start,end))
                break
            if len(actual)>=len(wanted):break
    return matches

def propose(clip,receipt,transcript):
    proposals=[]
    for unit in clip["units"]:
        wanted=tokens(unit["text"])
        found=find_spans(transcript["words"],unit["text"])
        occurrence=unit.get("occurrence",1)
        good=bool(wanted) and len(found)>=occurrence
        proposal={
            "unitId":unit["id"],"scriptAnchor":unit["text"],
            "occurrence":occurrence,"matches":len(found),
            "candidateStatus":"asr-exact-candidate-unreviewed" if good else "needs-human-alignment",
            "requiresHumanReview":True
        }
        if good:
            first,last=found[occurrence-1]
            proposal.update(wordStart=first,wordEnd=last,
                            atMs=transcript["words"][first]["start_ms"])
        proposals.append(proposal)
    return {"clipId":clip["id"],"jobId":receipt["jobId"],
            "audioHash":receipt["audioHash"],"transcriptHash":receipt["transcriptHash"],
            "scriptHash":sha256(clip["script"]),"units":proposals}

def stage_artifact(root,artifact_dir):
    """Copy verified artifact into throwaway checkout; refuse duplicates/incomplete set."""
    roots={}
    for p in Path(artifact_dir).rglob("receipt.json"):
        if p.parent.parent.name!="media":continue
        lesson=p.parents[2].name
        if lesson not in LESSONS:continue
        source=p.parent.parent
        if lesson in roots and roots[lesson]!=source:raise ValueError("Ambiguous lesson media roots")
        roots[lesson]=source
    require(len(roots)==3,"Missing one or more original lesson-media directories")
    for lesson,source in roots.items():
        target=Path(root)/"curricula"/COURSE/"lessons"/lesson/"media"
        require(not target.exists(),"Refusing to replace existing selected lesson media")
        shutil.copytree(source,target)
    return roots

def report(root=ROOT,artifact_dir=None,log_original_results=False):
    if artifact_dir:stage_artifact(root,artifact_dir)
    output=[];total_units=0;matched=0
    for lesson_id in LESSONS:
        media=validate_lesson(root,COURSE,lesson_id,"media")
        require(media["valid"],"Actual selected-media stage validation failed")
        folder,lesson,scenes=load_lesson(root,COURSE,lesson_id)
        for clip in clips_for(scenes):
            receipt,transcript=check_receipt(folder,clip)
            record=propose(clip,receipt,transcript)
            record["lessonId"]=lesson_id
            output.append(record)
            total_units+=len(record["units"])
            matched+=sum(u["candidateStatus"]=="asr-exact-candidate-unreviewed"
                         for u in record["units"])
            if log_original_results:
                result_path=folder/"media"/clip["id"]/receipt["files"]["result"]
                original=read_json(result_path)
                require(original["id"]==receipt["jobId"] and
                        original.get("metadata",{}).get("scriptHash")==receipt["scriptHash"],
                        "Factory original result does not match selected receipt")
                # The exact semantic original result, not a reconstructed proxy.
                print("B01_ORIGINAL_RESULT|"+lesson_id+"|"+clip["id"]+"|"+
                      json.dumps(original,ensure_ascii=False,separators=(",",":")))
    require(len(output)==69,"Expected 69 selected clips")
    return {"schemaVersion":1,"kind":"unreviewed-word-cue-candidates",
            "allMediaValid":True,"clipCount":len(output),"unitCount":total_units,
            "asrExactCandidateCount":matched,"humanAlignmentNeeded":total_units-matched,
            "method":"exact-normalized-ASR-word-span-match-NOT-REVIEWED",
            "timingJsonProduced":False,"humanTimingApproved":False,
            "publicationApproved":False,"clips":output}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-dir",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--print-results-for-durable-import",action="store_true")
    args=parser.parse_args()
    result=report(ROOT,args.artifact_dir,args.print_results_for_durable_import)
    write_json(args.output,result)
    print(json.dumps({k:result[k] for k in ("clipCount","unitCount",
        "asrExactCandidateCount","humanAlignmentNeeded","timingJsonProduced",
        "humanTimingApproved")},ensure_ascii=False))
