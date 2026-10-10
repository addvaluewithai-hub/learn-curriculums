"""Validate every authored script-stage lesson, without hardcoded course or lesson IDs.

Scaffold default scriptRevision='script-v1' is intentionally a draft;
Stage 04 authoring explicitly advances scriptRevision before requiring script quality.
"""
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from common import read_json
from validate import validate_lesson


class ScriptStageReadinessTests(unittest.TestCase):
    def test_all_non_scaffold_lessons_pass_script_contract(self):
        for lesson_file in sorted((ROOT / "curricula").glob("*/lessons/*/lesson.json")):
            lesson = read_json(lesson_file)
            if lesson.get("scriptRevision") == "script-v1":
                continue  # No premature script-stage check on scaffolds.
            with self.subTest(curriculum=lesson_file.parents[2].name, lesson=lesson_file.parent.name):
                report = validate_lesson(
                    ROOT,
                    lesson_file.parents[2].name,
                    lesson_file.parent.name,
                    "script",
                )
                self.assertTrue(report["valid"])
                self.assertFalse(report["publicationApproved"])


if __name__ == "__main__":
    unittest.main()
