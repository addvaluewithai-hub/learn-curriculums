"""Prepare a preview package from verified takes; never approve publication."""
import shutil
import json
from common import clips_for, load_lesson, read_json, require, safe_path, sha256, walk_files
from validate import validate_lesson
from media import check_receipt, check_timing
from alignment import selected_words
from preview_questions import adapt_question, reading_parts


def adapt_lesson(root, course_id, lesson_id, public, sdk_version):
    report = validate_lesson(root, course_id, lesson_id, "timed")
    folder, lesson, scenes = load_lesson(root, course_id, lesson_id)
    course = read_json(folder.parents[1] / "course.json")
    asset_base = f"/lesson-assets/{course_id}/{lesson_id}"
    modules, recordings, timings, bindings = {}, [], {}, []
    assets = safe_path(folder, "assets")
    if assets.exists():
        for asset in walk_files(assets):
            target = public / asset_base.lstrip("/") / "assets" / asset.relative_to(assets)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(asset, target)

    def visual(spec):
        require(isinstance(spec, dict) and spec.get("renderer") and spec.get("module"), "Preview needs a visual renderer and module")
        module = safe_path(folder, spec["module"])
        require(module.is_file() and module.suffix in {".tsx", ".jsx", ".ts", ".js"}, "Visual module must be local React code")
        previous = modules.get(spec["renderer"])
        require(previous is None or previous == module, "One renderer ID maps to different modules in this lesson")
        modules[spec["renderer"]] = module
        return {"renderer": spec["renderer"], "params": {**spec["params"], "assetBase": asset_base}}

    for clip in clips_for(scenes):
        receipt, original = check_receipt(folder, clip)
        transcript, transcript_hash = selected_words(folder, clip, receipt, original)
        timing = check_timing(folder, clip)
        timings[clip["id"]] = timing
        audio = safe_path(folder, f"media/{clip['id']}/{receipt['files']['audio']}")
        filename = receipt["audioHash"] + ".wav"
        target = public / "lesson-assets" / course_id / lesson_id / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(audio, target)
        require(sha256(target.read_bytes()) == receipt["audioHash"], "Audio changed during preview preparation")
        recordings.append({
            "id": clip["id"], "file": asset_base + "/" + filename,
            "audioHash": receipt["audioHash"], "durationMs": receipt["durationMs"], "words": transcript["words"],
            "cues": [{"id": c["unitId"], "atMs": c["atMs"]} for c in timing["cues"]],
            "contentAudit": {"faithful": False, "issues": ["Preview generation does not establish listening or publication approval."]},
        })
        bindings.append({"clipId": clip["id"], "jobId": receipt["jobId"], "audioHash": receipt["audioHash"],
                         "scriptHash": receipt["scriptHash"], "transcriptHash": transcript_hash})

    runtime_scenes, sources = [], []
    source_map = {s["id"]: s for s in course["sources"]}
    for scene in scenes:
        spec = visual(scene["visual"])
        result = {"id": scene["id"], "title": scene["title"], "takeaway": "", "tip": "", "check": "",
                  "script": scene["narration"]["script"], "visual": spec, "recordingId": scene["narration"]["id"]}
        if scene.get("question"):
            q = scene["question"]
            feedback_visual = visual(q["feedback"]["visual"]) if q["feedback"].get("visual") else None
            result["question"] = adapt_question(q, scene["narration"], timings[scene["narration"]["id"]], spec, feedback_visual)
            answer_parts = {**q["answer"], "id": q["id"], "readingUnitIds": q["feedback"].get("answerUnitIds", {})}
            result["question"]["feedbackParts"] = reading_parts(answer_parts, q["feedback"], timings[q["feedback"]["id"]])
            recording = next(r for r in recordings if r["id"] == scene["narration"]["id"])
            recording["questionAtMs"] = result["question"]["readingParts"][0]["atMs"]
        runtime_scenes.append(result)
        for ref in scene["sources"]:
            source = source_map[ref["sourceId"]]
            sources.append({"title": source["title"], "locator": ref["locator"], "availability": source["access"]})

    package = {
        "schemaVersion": 1, "delivery": "recorded", "lessonId": lesson_id, "curriculumId": course_id,
        "contentRevision": report["sourceHash"], "recordingVersion": sha256(json.dumps(bindings, sort_keys=True)),
        "title": lesson["title"], "englishTitle": lesson.get("englishTitle") or lesson["title"],
        "curriculumTitle": course["title"], "lessonOrder": lesson["order"], "fps": 30,
        "dimensions": {"landscape": {"width": 960, "height": 540}, "portrait": {"width": 540, "height": 960}},
        "scenes": runtime_scenes, "recordings": recordings, "glossary": lesson["glossary"], "sources": sources,
        "review": {"heading": "الدرس خلص", "summary": "راجع الفكرة والإجابات، وسجّل ملاحظاتك في مراجعة الدرس."},
    }
    return package, modules, {"sourceHash": report["sourceHash"], "runtimeVersion": sdk_version,
                              "bindings": bindings, "runtimeVerified": False, "publicationApproved": False}
