"""Original counting fixture, not a curriculum shipped to students."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from common import read_json, write_json
from scaffold import new_course, new_lesson


class ProductionCase(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.course = new_course(self.root, "counting", "Counting")
        self.folder = new_lesson(self.root, "counting", "counting-add", 1, "Combining counters")
        course = read_json(self.course / "course.json")
        course["sources"] = [{"id": "original", "title": "Original counting example", "access": "available", "file": "note.md"}]
        write_json(self.course / "course.json", course)
        (self.course / "note.md").write_text("Two counters plus three counters make five counters. Original example.\n")
        lesson = read_json(self.folder / "lesson.json")
        lesson.update(englishTitle="Combining counters", scenes=["S01", "S02"],
                      objectives=[{"id": "O1", "description": "Combine two groups", "taughtIn": ["S01"], "assessedIn": ["Q1"]}])
        write_json(self.folder / "lesson.json", lesson)
        self.teaching = {
            "id": "S01", "title": "Combine", "objectiveIds": ["O1"],
            "sources": [{"sourceId": "original", "locator": "Counting note, sentence 1"}],
            "narration": {"id": "N01", "role": "teaching", "script": "Two plus three is five. سؤال قصير دلوقتي.",
                          "units": [{"id": "U1", "text": "Two plus three", "visualIntent": "Merge counter groups"}]},
            "visual": {"renderer": "counters", "module": None, "params": {},
                       "landscape": "Groups side by side", "portrait": "Groups above each other"}}
        self.question = {
            "id": "S02", "title": "Try", "objectiveIds": ["O1"],
            "sources": self.teaching["sources"],
            "narration": {"id": "Q01", "role": "question", "script": "How many counters? كام قطعة؟",
                          "units": [{"id": "UQ", "text": "How many counters", "visualIntent": "Show the English question"}]},
            "visual": self.teaching["visual"],
            "question": {"id": "Q1", "english": "How many counters?", "arabic": "كام قطعة؟", "attempt": "written",
                         "answer": {"english": "Five counters.", "arabic": "خمس قطع.", "reasoning": "Two plus three."},
                         "feedback": {"id": "F01", "role": "feedback", "script": "Five counters. خمس قطع.",
                                      "units": [{"id": "UF", "text": "Five counters", "visualIntent": "Reveal the answer"}]}}}
        self.save_scenes()
        write_json(self.root / "production.json", {"audio": {"repository": "addvaluewithai-hub/gemini-tts",
                   "voice": "Gacrux", "style": "Warm calm teacher", "routing": "quality", "sampleRate": 24000, "languageCodes": []}})

    def save_scenes(self):
        write_json(self.folder / "scenes/S01.json", self.teaching)
        write_json(self.folder / "scenes/S02.json", self.question)
