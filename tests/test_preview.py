from pathlib import Path
from preview_support import PreviewCase
from preview import prepare_preview
from preview_package import adapt_lesson
from common import read_json, sha256, write_json
from alignment import import_alignment


class PreviewTests(PreviewCase):
    def setUp(self):
        super().setUp()
        self.deliver_all()
        self.preview = self.root / "preview-sdk"
        self.preview.mkdir()
        write_json(self.preview / "sdk-version.json", {"version": "0.2.0", "sha256": "a" * 64})

    def test_selected_bytes_bilingual_onsets_and_custom_modules_survive_adapter(self):
        report = prepare_preview(self.root, self.preview)
        self.assertEqual(report["ready"], 1)
        payload = read_json(self.preview / ".generated/public/packages/counting/counting-add.json")
        lesson = payload["lesson"]
        self.assertFalse(payload["provenance"]["publicationApproved"])
        self.assertEqual(lesson["scenes"][1]["question"]["readingParts"][1]["atMs"], 600)
        self.assertEqual(lesson["scenes"][1]["question"]["readingVisual"]["renderer"], "counting-probe")
        self.assertEqual(lesson["scenes"][1]["question"]["feedbackVisual"]["renderer"], "counting-probe")
        for recording in lesson["recordings"]:
            actual = self.preview / ".generated/public" / recording["file"].lstrip("/")
            self.assertEqual(sha256(actual.read_bytes()), recording["audioHash"])
        self.assertIn("Probe.tsx", (self.preview / ".generated/modules.ts").read_text())

    def test_missing_translation_anchor_is_a_blocker_not_an_estimate(self):
        self.question["narration"]["units"].pop()
        self.save_scenes()
        path = self.folder / "media/Q01/timing.json"
        timing = read_json(path)
        timing["cues"].pop()
        write_json(path, timing)
        report = prepare_preview(self.root, self.preview)
        self.assertEqual(report["ready"], 0)
        catalog = read_json(self.preview / ".generated/catalog.json")
        self.assertIn("full arabic", catalog["entries"][0]["blocker"])

    def test_stale_scripts_remove_previously_ready_package(self):
        prepare_preview(self.root, self.preview)
        self.teaching["narration"]["script"] += " changed"
        self.save_scenes()
        self.assertEqual(prepare_preview(self.root, self.preview)["ready"], 0)
        self.assertFalse((self.preview / ".generated/public/packages/counting/counting-add.json").exists())

    def test_reviewed_corrected_transcript_is_selected_without_rewriting_original(self):
        base = self.folder / "media/Q01"
        receipt = read_json(base / "receipt.json")
        original_path = base / receipt["files"]["transcript"]
        original = original_path.read_bytes()
        corrected = read_json(original_path)
        corrected["words"][3]["start_ms"] = 650
        write_json(self.root / "corrected.json", corrected)
        alignment = import_alignment(self.root, "counting", "counting-add", "Q01", self.root / "corrected.json",
                                     "manual-measured-reviewed", "test reviewer", "Synthetic correction only")
        timing = read_json(base / "timing.json")
        timing["transcriptHash"] = alignment["transcriptHash"]
        timing["cues"][1]["atMs"] = 650
        write_json(base / "timing.json", timing)
        package, _, provenance = adapt_lesson(self.root, "counting", "counting-add", self.preview / "public", "0.2.0")
        self.assertEqual(package["scenes"][1]["question"]["readingParts"][1]["atMs"], 650)
        self.assertEqual(provenance["bindings"][1]["transcriptHash"], alignment["transcriptHash"])
        self.assertEqual(original_path.read_bytes(), original)

    def test_missing_or_escaping_visual_cannot_be_loaded(self):
        self.teaching["visual"]["module"] = "../Outside.tsx"
        self.save_scenes()
        self.assertEqual(prepare_preview(self.root, self.preview)["ready"], 0)
