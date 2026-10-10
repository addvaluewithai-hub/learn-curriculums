"""Regression checks for the authorized B02 Stage 02 editorial manuscript gate.

These checks validate the saved writing and selected examples; they do NOT
approve textbook fidelity, learner comprehension, audio, or published lessons.
"""
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / "curricula" / "engineering-math-1" / "blocks" / "B02" / "working-drafts"
FILES = {
    "A": ("01-functions.md", 4),
    "B": ("02-function-families.md", 5),
    "C": ("03-monotonicity-limits.md", 4),
    "D": ("04-calculating-limits.md", 4),
    "E": ("05-continuity.md", 4),
}
QUESTION = re.compile(r"^## Independent attempt Q-([A-E]\d+)\b", re.M)
FEEDBACK = re.compile(r"^### Post-attempt feedback ([A-E]\d+)\b", re.M)


class B02Stage02ManuscriptTests(unittest.TestCase):
    def test_complete_provisional_drafts_and_delayed_explanation(self):
        question_count = feedback_count = 0
        for label, (filename, expected) in FILES.items():
            with self.subTest(draft=label):
                script = (DRAFTS / filename).read_text(encoding="utf-8")
                questions = list(QUESTION.finditer(script))
                feedbacks = list(FEEDBACK.finditer(script))
                self.assertIn("**Stage:** B02 **Stage 02**", script)
                self.assertIn("## Complete connected spoken draft", script)
                self.assertIn("## Closing spoken recap", script)
                self.assertLessEqual(len(script.splitlines()), 300)
                self.assertEqual(expected, len(questions))
                self.assertEqual(expected, len(feedbacks))
                self.assertEqual(len(questions), len(set(q.group(1) for q in questions)))
                for index, (question, feedback) in enumerate(zip(questions, feedbacks)):
                    self.assertEqual(question.group(1), feedback.group(1))
                    self.assertLess(question.start(), feedback.start())
                    if index + 1 < len(questions):
                        self.assertLess(feedback.start(), questions[index + 1].start())
                for label_text in (
                    "**Question spoken (English):",
                    "**Question spoken (Arabic support):",
                    "**Model answer (English):",
                    "**Feedback spoken:",
                ):
                    self.assertEqual(expected, script.count(label_text))
                for line in script.splitlines():
                    self.assertEqual(0, line.count("$") % 2)
                question_count += len(questions)
                feedback_count += len(feedbacks)
        self.assertEqual((21, 21), (question_count, feedback_count))

    def test_new_transfer_examples_arithmetic(self):
        self.assertEqual({1, 2, 5}, {x*x+1 for x in (-1, 0, 2)})
        for k in (-3, -2, -1, 0, 1, 2, 3):
            x = math.pi/4 + k*math.pi/2
            self.assertAlmostEqual(0, math.cos(2*x), places=12)
        for x in (3 - 0.00001, 3 + 0.00001):
            self.assertAlmostEqual(x+3, (x*x-9)/(x-3), places=8)
        self.assertNotEqual(6, -7)
        for x in (2 - 0.000001, 2 + 0.000001):
            self.assertLess(abs(x-2), 0.00001)
        self.assertEqual(0, abs(2-2))
        self.assertAlmostEqual(2.5, math.sin(5e-6)/(2e-6), places=8)


if __name__ == "__main__":
    unittest.main()
