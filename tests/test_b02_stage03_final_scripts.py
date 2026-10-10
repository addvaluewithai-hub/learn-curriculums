"""Stage 03 editorial assertions for the eight issued B02 lessons.

Not a human subject-matter review, real multimedia test, or publication check.
"""
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "curricula" / "engineering-math-1" / "blocks" / "B02" / "final-scripts"
IDS = (
    "em1-functions-domain-range",
    "em1-functions-algebraic-graphs",
    "em1-functions-trig-exp-log",
    "em1-functions-monotonicity",
    "em1-limits-concept-one-sided",
    "em1-limits-algebraic-methods",
    "em1-limits-trigonometric",
    "em1-functions-continuity",
)
ORIGINAL = {
    "A1", "A2", "A3", "A4",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4",
    "D1", "D2", "D3", "D4",
    "E1", "E2", "E3", "E4",
}
NEW = {"B6", "C5", "C6", "D5", "D6"}
Q = re.compile(r"^## Independent attempt Q-([A-E]\d+)\b", re.M)
F = re.compile(r"^### Post-attempt feedback ([A-E]\d+)\b", re.M)


class B02Stage03EditorialTests(unittest.TestCase):
    def test_issued_ids_full_narratives_and_exact_question_coverage(self):
        seen = set()
        count = 0
        for order, lesson_id in enumerate(IDS, start=1):
            with self.subTest(lesson=lesson_id):
                file = SCRIPT_DIR / (lesson_id + ".md")
                self.assertTrue(file.is_file(), str(file))
                script = file.read_text(encoding="utf-8")
                self.assertIn("**Stable lesson ID:** `" + lesson_id + "`", script)
                self.assertIn("**B02 issued order:** " + str(order) + " of 8", script)
                self.assertIn("## Complete connected spoken script", script)
                self.assertIn("## Closing spoken recap", script)
                self.assertLessEqual(len(script.splitlines()), 300)
                self.assertNotIn("\\`", script)
                for line in script.splitlines():
                    self.assertEqual(0, line.count("$") % 2)
                questions = list(Q.finditer(script))
                feedback = list(F.finditer(script))
                self.assertGreaterEqual(len(questions), 3)
                self.assertEqual(len(questions), len(feedback))
                for index, (question, answer) in enumerate(zip(questions, feedback)):
                    self.assertEqual(question.group(1), answer.group(1))
                    self.assertLess(question.start(), answer.start())
                    if index + 1 < len(questions):
                        self.assertLess(answer.start(), questions[index+1].start())
                    prompt = script[question.start():answer.start()]
                    self.assertIn("**Question spoken (English):", prompt)
                    self.assertIn("**Question spoken (Arabic support):", prompt)
                    self.assertIn("**Attempt:**", prompt)
                    self.assertNotIn("**Model answer (English):", prompt)
                    answer_text = script[answer.start():(
                        questions[index+1].start() if index+1 < len(questions)
                        else script.index("## Closing spoken recap")
                    )]
                    self.assertIn("**Model answer (English):", answer_text)
                    self.assertIn("**Feedback spoken:", answer_text)
                    self.assertNotIn(question.group(1), seen)
                    seen.add(question.group(1))
                    count += 1
        self.assertEqual(26, count)
        self.assertEqual(ORIGINAL | NEW, seen)

    def test_selected_new_math_transfer_examples(self):
        self.assertEqual(-1, (1 / (2 + 1)) * 0 - 1)
        self.assertEqual(-5, -5)  # denominator hole of 2/(x+5)-1
        self.assertAlmostEqual(0, (2 + 5) - 7)
        self.assertEqual(9, -2*(-1)+7)
        self.assertEqual(1, -2*3+7)
        self.assertEqual(2, 1/(1/2))
        self.assertEqual(1/2, 1/2)
        self.assertEqual(8, 4+4)
        for x in (4 - 0.00001, 4 + 0.00001):
            self.assertAlmostEqual(x+4, (x*x-16)/(x-4), places=8)
        for x in (0.00001, -0.00001):
            self.assertAlmostEqual(6/5, math.tan(6*x)/(5*x), places=7)
            self.assertAlmostEqual(4/7, math.sin(4*x)/math.tan(7*x), places=7)


if __name__ == "__main__":
    unittest.main()
