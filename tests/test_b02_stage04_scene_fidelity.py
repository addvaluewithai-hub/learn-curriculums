"""Compare B02 Stage 04 canonical scenes against all eight Stage 03 manuscripts.

This is technical/source-word parity, NOT specialist pedagogy, audio or playback approval.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curricula" / "engineering-math-1"
BLOCK = COURSE / "blocks" / "B02" / "final-scripts"
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
QUEST = re.compile(r"^## Independent attempt Q-([A-E]\d+)\b")
FEED = re.compile(r"^### Post-attempt feedback ([A-E]\d+)\b")
FIELDS = {
    "question": {
        "en": "**Question spoken (English):** ",
        "ar": "**Question spoken (Arabic support):** ",
    },
    "feedback": {
        "ans": "**Model answer (English):** ",
        "exp": "**Feedback spoken:** ",
    },
}


def parsed_source(source: str) -> list[dict]:
    output = []
    mode = ""
    buff = []
    current = None

    def flush() -> None:
        if buff:
            output.append({"type": "teach", "script": " ".join(buff).replace("**", "")})
            buff.clear()

    for line in source.splitlines():
        if line.startswith(("## Complete connected spoken script", "## Connected spoken continuation",
                            "## Closing spoken recap")):
            flush()
            mode = "teach"
            continue
        if line.startswith("## Rough visual"):
            flush()
            mode = ""
            continue
        q = QUEST.match(line)
        if q:
            flush()
            current = {"type": "question", "id": q.group(1)}
            output.append(current)
            mode = "question"
            continue
        f = FEED.match(line)
        if f:
            if not current or current["id"] != f.group(1):
                raise AssertionError("Feedback ID does not match question")
            mode = "feedback"
            continue
        if mode == "teach":
            if line.strip():
                buff.append(line.strip())
            else:
                flush()
        elif mode in FIELDS:
            for key, prefix in FIELDS[mode].items():
                if line.startswith(prefix):
                    current[key] = line[len(prefix):]
    flush()
    return output


class B02Stage04FidelityTests(unittest.TestCase):
    def test_canonical_scenes_match_every_spoken_source_word(self):
        questions = scenes = clips = 0
        runtime_orders = []
        for block_index, lesson_id in enumerate(IDS, start=1):
            with self.subTest(lesson=lesson_id):
                folder = COURSE / "lessons" / lesson_id
                lesson = json.loads((folder / "lesson.json").read_text(encoding="utf-8"))
                original = parsed_source((BLOCK / (lesson_id + ".md")).read_text(encoding="utf-8"))
                current = [json.loads((folder / "scenes" / (sid + ".json")).read_text(
                    encoding="utf-8")) for sid in lesson["scenes"]]
                self.assertEqual(len(original), len(current))
                self.assertEqual(lesson["id"], lesson_id)
                self.assertEqual(lesson["order"], block_index + 5)
                runtime_orders.append(lesson["order"])
                self.assertNotEqual(lesson["scriptRevision"], "script-v1")
                self.assertTrue((folder / "scenes" / "ConceptBoard.tsx").is_file())
                board = (folder / "STORYBOARDS.md").read_text(encoding="utf-8")
                self.assertIn("16:9", board)
                self.assertIn("9:16", board)
                review = json.loads((folder / "review.json").read_text(encoding="utf-8"))
                self.assertIsNone(review["sourceHash"])
                self.assertTrue(all(v["status"] == "untested"
                                    for v in review["checks"].values()))
                qscene = {}
                indices = {scene["id"]: i for i, scene in enumerate(current)}
                for expected, scene in zip(original, current):
                    narration = scene["narration"]
                    self.assertTrue(scene["sources"][0]["locator"])
                    self.assertTrue(scene["visual"]["landscape"])
                    self.assertTrue(scene["visual"]["portrait"])
                    if expected["type"] == "teach":
                        self.assertEqual(narration["role"], "teaching")
                        self.assertEqual(narration["script"], expected["script"])
                        clips += 1
                    else:
                        questions += 1
                        clips += 2
                        question = scene["question"]
                        qscene[question["id"]] = scene
                        self.assertEqual(question["id"], expected["id"])
                        self.assertEqual(question["attempt"], "written")
                        self.assertEqual(narration["role"], "question")
                        self.assertEqual(narration["script"], expected["en"] + "\n" + expected["ar"])
                        self.assertEqual(question["english"], expected["en"])
                        self.assertEqual(question["arabic"], expected["ar"])
                        self.assertEqual(question["answer"]["english"], expected["ans"])
                        self.assertEqual(question["answer"]["arabic"], expected["exp"])
                        self.assertEqual(question["feedback"]["script"],
                                         expected["ans"] + "\n" + expected["exp"])
                        self.assertNotIn(expected["ans"], narration["script"])
                        self.assertEqual(question["readingUnitIds"],
                                         {"english": "QEN", "arabic": "QAR"})
                        self.assertEqual(question["feedback"]["answerUnitIds"],
                                         {"english": "AEN", "arabic": "AAR"})
                    for clip in (narration, [scene["question"]["feedback"]]
                                 if scene.get("question") else []):
                        if isinstance(clip, list):
                            items = clip
                        else:
                            items = [clip]
                        for part in items:
                            self.assertTrue(part["units"])
                            for u in part["units"]:
                                self.assertIn(u["text"], part["script"])
                                self.assertGreaterEqual(part["script"].count(u["text"]),
                                                        u["occurrence"])
                    scenes += 1
                for objective in lesson["objectives"]:
                    self.assertTrue(objective["taughtIn"])
                    self.assertTrue(objective["assessedIn"])
                    before = min(indices[x] for x in objective["taughtIn"])
                    for qid in objective["assessedIn"]:
                        self.assertLess(before, indices[qscene[qid]["id"]])
        self.assertEqual(26, questions)
        self.assertEqual(106, scenes)
        self.assertEqual(132, clips)
        self.assertEqual(list(range(6, 14)), runtime_orders)


if __name__ == "__main__":
    unittest.main()
