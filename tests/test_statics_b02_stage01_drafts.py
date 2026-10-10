import sys
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"curricula"/"engineering-mechanics-statics-y1"/"blocks"/"B02"

class B02Stage01DraftGate(unittest.TestCase):
    def test_all_provisional_spoken_scripts_have_separate_attempts(self):
        scripts=[
          "01-scalars-vectors-operations.md",
          "02-planar-resultants-trigonometry.md",
          "03-force-resolution-rectangular-intro.md"
        ]
        for name in scripts:
            text=(BASE/"drafts"/name).read_text(encoding="utf-8")
            self.assertGreater(len(text.split()),500)
            self.assertIn("Independent attempt",text)
            self.assertIn("Separate post-attempt feedback",text)
            self.assertLess(text.index("Independent attempt"),
                            text.index("Separate post-attempt feedback"))
            self.assertIn("No stable lesson ID",text)
    def test_source_boundary_and_no_premature_scenes(self):
        src=(BASE/"STAGE_01_SOURCE_MAP.md").read_text(encoding="utf-8")
        self.assertIn("pp.9–18",src)
        self.assertIn("§2.5",src)
        self.assertFalse((BASE/"scenes").exists())
        self.assertFalse((BASE/"lessons").exists())

if __name__=="__main__":
    unittest.main()
