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

import difflib
import re
import unicodedata

def speech_tokens(value):
    value=unicodedata.normalize("NFKC",value.casefold())
    value="".join(c for c in value if c!="ـ" and not
        (unicodedata.combining(c) and "ARABIC" in unicodedata.name(c,"")))
    value=value.translate(str.maketrans({"أ":"ا","إ":"ا","آ":"ا","ٱ":"ا",
        "ى":"ي","ة":"ه","ؤ":"و","ئ":"ي"}))
    return re.findall(r"[^\W_]+",value,flags=re.UNICODE)

def normalized_spans(words,phrase):
    target=speech_tokens(phrase)
    if not target:return []
    out=[]
    for start in range(len(words)):
        observed=[]
        for end in range(start,min(len(words),start+len(target)+5)):
            observed.extend(speech_tokens(words[end]["text"]))
            if observed==target:
                out.append((start,end));break
            if len(observed)>=len(target):break
    return out

def partial_search_evidence(words,phrase):
    """Only an observed ASR fragment's time; never claim a full spoken cue."""
    target=speech_tokens(phrase)
    if len(target)<3:return None
    indexed=[(token,index) for index,word in enumerate(words)
             for token in speech_tokens(word["text"])]
    observed=[token for token,_ in indexed]
    options=[]
    for start in range(len(observed)-1):
        for position in range(len(target)-1):
            if observed[start:start+2]!=target[position:position+2]:continue
            left=max(0,start-position)
            context=observed[left:min(len(observed),left+len(target)+3)]
            align=difflib.SequenceMatcher(None,target,context,autojunk=False)
            cover=sum(b.size for b in align.get_matching_blocks())/len(target)
            score=align.ratio()
            if cover>=0.55 and score>=0.47:
                options.append((cover,score,words[indexed[start][1]]["start_ms"],start,position))
    if not options:return None
    coverage,score,at,start,pos=max(options)
    return {"reviewSeekMs":at,"matchedASRToken":observed[start],
            "sourceTokenIndex":pos,"sourceCoverage":round(coverage,3),
            "searchScore":round(score,3),
            "warning":"Observed fragment time only; NOT an approved cue start"}

def propose(clip,receipt,transcript):
    proposals=[]
    for unit in clip["units"]:
        wanted=tokens(unit["text"])
        words=transcript["words"]
        found=find_spans(words,unit["text"])
        occurrence=unit.get("occurrence",1)
        strict=bool(wanted) and len(found)>=occurrence
        normal=normalized_spans(words,unit["text"]) if not strict else []
        whole=strict or len(normal)>=occurrence
        proposal={
            "unitId":unit["id"],"scriptAnchor":unit["text"],
            "occurrence":occurrence,"matches":len(found) if strict else len(normal),
            "candidateStatus":("asr-exact-candidate-unreviewed" if strict else
                "asr-orthographic-candidate-unreviewed" if whole else
                "needs-author-alignment"),
            "requiresAuthorDecision":True,
            "requiresHumanReview":False
        }
        if whole:
            first,last=(found if strict else normal)[occurrence-1]
            proposal.update(wordStart=first,wordEnd=last,
                            atMs=words[first]["start_ms"],
                            observedText=" ".join(w["text"] for w in words[first:last+1]))
        else:
            hint=partial_search_evidence(words,unit["text"])
            if hint:
                proposal["candidateStatus"]="asr-partial-search-hint-unreviewed"
                proposal["searchHint"]=hint
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
        if target.exists():
            # Durable receipt/result metadata may have been committed after review.
            # Hydrate missing binaries but never overwrite an existing selected take.
            for incoming in source.rglob("*"):
                require(not incoming.is_symlink(),"Artifact symlink rejected")
                if incoming.is_dir():continue
                output=target/incoming.relative_to(source)
                if output.is_file():
                    # Git stores canonical JSON serialized with indentation; GitHub
                    # factory artifact may serialize the SAME values differently.
                    # Compare immutable JSON values for receipts/original results,
                    # but require byte-for-byte matches for WAV and ASR assets.
                    if incoming.name in {"receipt.json","result.json"}:
                        require(read_json(output)==read_json(incoming),
                                "Stored receipt/result values differ from original factory")
                    else:
                        require(output.read_bytes()==incoming.read_bytes(),
                                "Stored media bytes differ from original factory selection")
                else:
                    require(not output.exists(),"Existing non-file media target")
                    output.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copyfile(incoming,output)
        else:
            shutil.copytree(source,target)
    return roots

def report(root=ROOT,artifact_dir=None,log_original_results=False):
    if artifact_dir:stage_artifact(root,artifact_dir)
    output=[];total_units=0;matched=0;orthographic=0;hints=0
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
            orthographic+=sum(u["candidateStatus"]=="asr-orthographic-candidate-unreviewed"
                              for u in record["units"])
            hints+=sum(u["candidateStatus"]=="asr-partial-search-hint-unreviewed"
                       for u in record["units"])
            if log_original_results:
                result_path=folder/"media"/clip["id"]/receipt["files"]["result"]
                original=read_json(result_path)
                require(original["id"]==receipt["jobId"] and
                        original.get("metadata",{}).get("scriptHash")==receipt["scriptHash"],
                        "Factory original result does not match selected receipt")
                # The exact semantic original result and SHA-verified selected
                # receipt, both from the factory-linked take, never fabricated.
                print("B01_ORIGINAL_RESULT|"+lesson_id+"|"+clip["id"]+"|"+
                      json.dumps(original,ensure_ascii=False,separators=(",",":")))
                print("B01_ORIGINAL_RECEIPT|"+lesson_id+"|"+clip["id"]+"|"+
                      json.dumps(receipt,ensure_ascii=False,separators=(",",":")))
    require(len(output)==69,"Expected 69 selected clips")
    return {"schemaVersion":1,"kind":"unreviewed-word-cue-candidates",
            "allMediaValid":True,"clipCount":len(output),"unitCount":total_units,
            "asrExactCandidateCount":matched,"orthographicWholePhraseCount":orthographic,
            "partialFragmentSearchCount":hints,
            "noASRSearchEvidenceCount":total_units-matched-orthographic-hints,
            "authorAlignmentNeeded":total_units-matched-orthographic,
            "method":"ASR-word-span-and-search-evidence-NOT-REVIEWED",
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
        "asrExactCandidateCount","orthographicWholePhraseCount",
        "partialFragmentSearchCount","noASRSearchEvidenceCount",
        "authorAlignmentNeeded","timingJsonProduced",
        "humanTimingApproved")},ensure_ascii=False))
