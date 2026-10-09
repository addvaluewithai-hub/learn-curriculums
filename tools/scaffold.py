"""Create a curriculum or lesson without touching another editor's files."""
from datetime import date
from common import identity, lesson_folder, read_json, require, safe_path, write_json

CHECKS = ("sources", "teaching", "audio", "timing", "visual", "runtime")


def new_course(root, course, title):
    folder = safe_path(root, "curricula/" + identity(course))
    require(title.strip(), "Course title is required")
    folder.mkdir(parents=True, exist_ok=False)
    write_json(folder / "course.json", {
        "schemaVersion": 1, "id": course, "title": title,
        "revision": "outline-v1", "description": "",
        "language": {"explanation": "ar-EG", "exam": "en", "arabicSupport": True},
        "sources": [], "teacher": {},
    })
    (folder / "OUTLINE.md").write_text(
        "# خطة المنهج\n\nحدد المستوى والمصدر والأهداف وتسلسل الدروس والمتطلبات السابقة.\n"
        "احتفظ بمعرفات الدروس ثابتة؛ ترتيبها ليس هويتها.\n", encoding="utf-8")
    return folder


def new_lesson(root, course, lesson, order, title):
    course_data = read_json(safe_path(root, f"curricula/{identity(course)}/course.json"))
    require(course_data["id"] == course, "Course identity mismatch")
    require(isinstance(order, int) and order > 0, "Lesson order must be positive")
    require(title.strip(), "Lesson title is required")
    folder = lesson_folder(root, course, lesson)
    for sibling in folder.parent.glob("*/lesson.json"):
        require(read_json(sibling)["order"] != order, "Lesson order already reserved")
    folder.mkdir(parents=True, exist_ok=False)
    write_json(folder / "lesson.json", {
        "schemaVersion": 1, "kind": "learn-authoring", "id": lesson,
        "curriculumId": course, "order": order, "title": title, "englishTitle": "",
        "scriptRevision": "script-v1", "prerequisites": [],
        "objectives": [{"id": "O1", "description": "", "taughtIn": ["S01"], "assessedIn": []}],
        "scenes": ["S01"], "glossary": [],
    })
    write_json(folder / "scenes/S01.json", {
        "id": "S01", "title": title, "objectiveIds": ["O1"], "sources": [],
        "narration": {"id": "N01", "role": "teaching", "script": "", "units": []},
        "visual": {"renderer": "", "module": None, "params": {},
                   "landscape": "", "portrait": ""},
    })
    write_json(folder / "review.json", {
        "schemaVersion": 1, "sourceHash": None,
        "checks": {name: {"status": "untested", "reviewer": "", "evidence": ""} for name in CHECKS},
    })
    (folder / "STATUS.md").write_text(
        f"# حالة الدرس\n\n- التاريخ: {date.today()}\n- المسؤول: غير محدد\n"
        "- المرحلة: تأليف\n- المعاينة: تحتاج تسجيلات وتوقيتات ومكونات\n- النشر: لم ينشر\n"
        "- الخطوة التالية: تثبيت الأهداف والمصادر ثم كتابة المشاهد.\n", encoding="utf-8")
    return folder
