"""Authoring validation, independent of playback and database services."""
import math
from common import clips_for, identity, load_lesson, read_json, require, safe_path, source_hash
from runtime_review import sdk_identity, check_runtime_review

STAGES = ("draft", "script", "media", "timed")
ACCESS = {"available", "reviewed-notes", "unavailable"}


def text(value):
    return isinstance(value, str) and bool(value.strip())


def unique(values, label):
    require(isinstance(values, list), f"{label} must be a list")
    for value in values:
        identity(value)
    require(len(values) == len(set(values)), f"Duplicate {label}")


def validate_course(folder):
    course = read_json(folder / "course.json")
    require(course.get("schemaVersion") == 1, "Unsupported course schema")
    identity(course["id"])
    require(course["id"] == folder.name and text(course["title"]), "Course identity/title mismatch")
    require(isinstance(course.get("language"), dict), "Missing language policy")
    sources = course.get("sources")
    require(isinstance(sources, list), "Sources must be a list")
    unique([s["id"] for s in sources], "source IDs")
    for source in sources:
        require(text(source.get("title")) and source.get("access") in ACCESS, "Invalid source record")
        if source.get("file"):
            require(safe_path(folder, source["file"]).is_file(), "Missing local source")
    return course


def validate_unit(clip, complete):
    identity(clip["id"])
    require(clip.get("role") in {"teaching", "question", "feedback"}, "Invalid clip role")
    require(isinstance(clip.get("script"), str), "Script must be text")
    require(isinstance(clip.get("units"), list), "Semantic units must be a list")
    unique([u["id"] for u in clip["units"]], "unit IDs")
    if complete:
        require(text(clip["script"]) and clip["units"], f"Incomplete script/units: {clip['id']}")
    for unit in clip["units"]:
        require(text(unit.get("text")) and unit["text"] in clip["script"], "Unit anchor not in script")
        require(text(unit.get("visualIntent")), "Missing semantic visual intention")
        occurrence = unit.get("occurrence", 1)
        require(type(occurrence) is int and 0 < occurrence <= clip["script"].count(unit["text"]),
                "Invalid occurrence-qualified anchor")


def validate_question(question, scene, complete, language):
    identity(question["id"])
    require(scene["narration"]["role"] == "question", "Question needs a question narration clip")
    require(question.get("attempt") in {"written", "choice", "choice-and-written"}, "Invalid attempt policy")
    require(question["feedback"]["role"] == "feedback", "Feedback role must be feedback")
    validate_unit(question["feedback"], complete)
    if not complete:
        return
    english = language.get("exam") == "en"
    required = ["english"] if english else []
    if language.get("arabicSupport", True) or language.get("exam") == "ar":
        required.append("arabic")
    for field in required:
        require(text(question.get(field)), "Question needs English and Arabic support")
    for field in [*required, "reasoning"]:
        require(text(question.get("answer", {}).get(field)), "Model answer/reasoning missing")
    for field in required:
        require(question[field] in scene["narration"]["script"], f"{field} question absent from spoken clip")
    if question["attempt"] != "written":
        options = question.get("options")
        require(isinstance(options, list) and len(options) >= 2 and all(text(o) for o in options),
                "Choice options missing")
        answer = question.get("correctIndex")
        require(type(answer) is int and 0 <= answer < len(options), "Choice answer invalid")


def validate_lesson(root, course_id, lesson_id, stage="draft"):
    require(stage in STAGES, "Unknown validation stage")
    folder, lesson, scenes = load_lesson(root, course_id, lesson_id)
    course = validate_course(folder.parents[1])
    require(lesson.get("schemaVersion") == 1 and lesson.get("kind") == "learn-authoring", "Unsupported authoring schema")
    require(lesson["id"] == lesson_id and lesson["curriculumId"] == course_id, "Lesson identity mismatch")
    require(type(lesson["order"]) is int and lesson["order"] > 0, "Invalid lesson order")
    require(text(lesson["title"]) and text(lesson["scriptRevision"]), "Lesson metadata missing")
    unique(lesson["scenes"], "scene IDs")
    require(scenes, "No scenes")
    objectives = lesson.get("objectives")
    require(isinstance(objectives, list) and objectives, "Objectives missing")
    unique([o["id"] for o in objectives], "objective IDs")
    unique([q["question"]["id"] for q in scenes if q.get("question")], "question IDs")
    sources = {s["id"]: s for s in course["sources"]}
    objective_ids = {o["id"] for o in objectives}
    questions = {s["question"]["id"]: s for s in scenes if s.get("question")}
    complete = stage != "draft"
    for expected, scene in zip(lesson["scenes"], scenes):
        require(scene["id"] == expected and text(scene.get("title")), "Scene identity/title mismatch")
        require(isinstance(scene.get("objectiveIds"), list) and set(scene["objectiveIds"]) <= objective_ids,
                "Unknown objective in scene")
        refs = scene.get("sources")
        require(isinstance(refs, list), "Scene sources must be a list")
        for ref in refs:
            require(ref.get("sourceId") in sources and text(ref.get("locator")), "Invalid source locator")
        validate_unit(scene["narration"], complete)
        if scene.get("question"):
            validate_question(scene["question"], scene, complete, course["language"])
        else:
            require(scene["narration"]["role"] == "teaching", "Orphan question/feedback narration")
        visual = scene.get("visual")
        require(isinstance(visual, dict) and isinstance(visual.get("params"), dict), "Visual metadata missing")
        if visual.get("module"):
            require(safe_path(folder, visual["module"]).is_file(), "Visual module missing")
        if complete:
            require(refs, "Scene needs source evidence or an explicit authored-example source")
            require(text(visual.get("landscape")) and text(visual.get("portrait")), "Both storyboard layouts required")
            if course["language"].get("exam") == "en":
                require(text(lesson.get("englishTitle")), "English lesson title missing")
    scene_map = {s["id"]: s for s in scenes}
    for objective in objectives:
        taught, assessed = objective.get("taughtIn"), objective.get("assessedIn")
        require(isinstance(taught, list) and isinstance(assessed, list), "Objective mappings must be lists")
        require(all(s in scene_map and objective["id"] in scene_map[s]["objectiveIds"] for s in taught),
                "Broken teaching objective mapping")
        require(all(q in questions and objective["id"] in questions[q]["objectiveIds"] for q in assessed),
                "Broken assessment objective mapping")
        if complete:
            require(text(objective.get("description")) and taught and assessed, "Objective lacks independent assessment")
            teaching = [s for s in taught if not scene_map[s].get("question")]
            require(teaching, "Objective needs teaching before the question")
            first_teaching = min(lesson["scenes"].index(s) for s in teaching)
            require(all(first_teaching < lesson["scenes"].index(questions[q]["id"]) for q in assessed),
                    "Assessment precedes teaching")
    clips = clips_for(scenes)
    unique([c["id"] for c in clips], "clip IDs")
    if stage in {"media", "timed"}:
        from media import check_receipt, check_timing
        for clip in clips:
            check_receipt(folder, clip)
            if stage == "timed":
                check_timing(folder, clip)
    review = read_json(folder / "review.json")
    require(review.get("schemaVersion") == 1 and isinstance(review.get("checks"), dict), "Review metadata missing")
    for key in ("sources", "teaching", "audio", "timing", "visual", "runtime"):
        check = review["checks"].get(key, {})
        require(check.get("status") in {"passed", "failed", "untested"}, "Invalid review status")
        if check["status"] == "passed":
            require(text(check.get("reviewer")) and text(check.get("evidence")), "Passed review needs evidence/reviewer")
            require(review.get("sourceHash") == source_hash(folder), "Stale editorial review")
        if key == "runtime":
            check_runtime_review(root, check)
    sdk = sdk_identity(root)
    return {"courseId": course_id, "lessonId": lesson_id, "stage": stage, "valid": True,
            "sourceHash": source_hash(folder), "clipCount": len(clips),
            "preview": "sdk-available" if sdk else "pending-sdk",
            "runtimeVersion": sdk["version"] if sdk else None,
            "runtimeVerified": review["checks"]["runtime"]["status"] == "passed", "publicationApproved": False}


def validate_curriculum(root, course_id, stage="draft"):
    folder = safe_path(root, f"curricula/{identity(course_id)}")
    course = validate_course(folder)
    reports, orders = [], set()
    for lesson_file in sorted((folder / "lessons").glob("*/lesson.json")):
        data = read_json(lesson_file)
        require(data["order"] not in orders, "Duplicate lesson order in curriculum")
        orders.add(data["order"])
        reports.append(validate_lesson(root, course["id"], lesson_file.parent.name, stage))
    return reports


def validate_all(root, stage="draft"):
    reports, ids = [], set()
    for course_file in sorted((root / "curricula").glob("*/course.json")):
        course = validate_course(course_file.parent)
        for lesson_file in sorted((course_file.parent / "lessons").glob("*/lesson.json")):
            data = read_json(lesson_file)
            require(data["id"] not in ids, "Lesson ID must be globally unique")
            ids.add(data["id"])
        reports.extend(validate_curriculum(root, course["id"], stage))
    return reports
