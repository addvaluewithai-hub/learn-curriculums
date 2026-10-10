"""Gate real Stage 04 authored lessons through the repository's script validator.

A Stage 04 script revision opts into script-stage checks on the existing
project CI, while earlier-stage in-progress lessons remain valid drafts.
This is a structural check, NOT academic, speaking, visual or release approval.
"""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from common import read_json
from validate import validate_lesson


class Stage04CurriculumScriptTests(unittest.TestCase):
    def test_committed_stage04_lessons_pass_script_contract(self):
        found = []
        for course_file in sorted((ROOT / "curricula").glob("*/course.json")):
            course_id = course_file.parent.name
            for lesson_file in sorted((course_file.parent / "lessons").glob("*/lesson.json")):
                lesson = read_json(lesson_file)
                if "stage04" not in lesson.get("scriptRevision", ""):
                    continue
                report = validate_lesson(ROOT, course_id, lesson["id"], "script")
                self.assertTrue(report["valid"])
                self.assertEqual(report["stage"], "script")
                self.assertFalse(report["publicationApproved"])
                self.assertFalse(report["runtimeVerified"])
                found.append(lesson["id"])
        self.assertTrue(found, "No committed Stage 04 lesson was validated")


if __name__ == "__main__":
    unittest.main()
