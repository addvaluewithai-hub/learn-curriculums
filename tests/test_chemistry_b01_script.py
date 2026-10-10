"""Stage 04 regression: run the actual script-stage authoring contract on B01."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate import validate_lesson  # noqa: E402

COURSE = "chemistry-preparatory-engineering"
B01_LESSONS = (
    "chem1-states-phase-changes",
    "chem1-boyle-law",
    "chem1-charles-law",
)


class ChemistryB01ScriptContract(unittest.TestCase):
    def test_each_authoring_lesson_passes_script_stage(self):
        """Check full scene, goal, bilingual and source structures, not approval."""
        for lesson_id in B01_LESSONS:
            with self.subTest(lesson_id=lesson_id):
                result = validate_lesson(ROOT, COURSE, lesson_id, "script")
                self.assertTrue(result["valid"])
                self.assertEqual(result["stage"], "script")
                self.assertFalse(result["publicationApproved"])
                self.assertFalse(result["runtimeVerified"])


if __name__ == "__main__":
    unittest.main()
