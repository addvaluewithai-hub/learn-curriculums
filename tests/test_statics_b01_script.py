"""Contract test for first-year Statics B01 Stage 04: no claimed academic approval."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CID = "engineering-mechanics-statics-y1"
LESSONS = ("ems-y1-foundations-models", "ems-y1-newton-gravity", "ems-y1-units-conversions")


class StaticsB01ScriptGate(unittest.TestCase):
    def test_each_lesson_passes_real_script_validator(self):
        for lesson in LESSONS:
            with self.subTest(lesson=lesson):
                result = subprocess.run([
                    sys.executable, str(ROOT / "tools/cli.py"), "validate",
                    "--course", CID, "--lesson", lesson, "--stage", "script"
                ], cwd=ROOT, capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
                payload = json.loads(result.stdout)
                self.assertTrue(payload["valid"])
                self.assertEqual(payload["lessonId"], lesson)
                self.assertFalse(payload["publicationApproved"])

    def test_question_feedback_not_pre_exposed(self):
        for lesson in LESSONS:
            folder = ROOT / "curricula" / CID / "lessons" / lesson
            data = json.loads((folder / "lesson.json").read_text(encoding="utf-8"))
            self.assertTrue(data["scenes"])
            for sid in data["scenes"]:
                scene = json.loads((folder / "scenes" / f"{sid}.json").read_text(encoding="utf-8"))
                self.assertTrue(scene["visual"]["landscape"])
                self.assertTrue(scene["visual"]["portrait"])
                if "question" not in scene:
                    continue
                question = scene["question"]
                spoken = scene["narration"]["script"]
                previsual = str(scene["visual"]["params"])
                self.assertEqual(scene["narration"]["role"], "question")
                self.assertNotIn(question["answer"]["english"], spoken)
                self.assertNotIn(question["answer"]["arabic"], spoken)
                self.assertNotIn(question["answer"]["english"], previsual)
                self.assertNotIn(question["answer"]["arabic"], previsual)
                self.assertNotIn(question["feedback"]["script"], spoken)
                self.assertEqual(question["attempt"], "written")
                self.assertEqual(question["feedback"]["role"], "feedback")


if __name__ == "__main__":
    unittest.main()
