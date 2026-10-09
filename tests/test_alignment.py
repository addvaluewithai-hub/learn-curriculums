import test_audio
from support import ProductionCase
from common import read_json, write_json
from alignment import import_alignment, selected_words
from media import check_receipt, check_timing


class AlignmentTests(ProductionCase):
    job = test_audio.AudioTests.job
    delivery = test_audio.AudioTests.delivery
    collect_job = test_audio.AudioTests.collect_job
    def test_corrected_alignment_preserves_original_and_uses_new_hash(self):
        job = self.job()
        self.collect_job(job)
        receipt, original = check_receipt(self.folder, self.teaching["narration"])
        base = self.folder / "media/N01"
        raw_original = (base / receipt["files"]["transcript"]).read_bytes()
        corrected = read_json(base / receipt["files"]["transcript"])
        corrected["alignment_mode"] = "reviewed-correction-fixture"
        corrected["words"][0].update(start_ms=10, end_ms=45)
        corrected_path = self.root / "corrected.json"
        write_json(corrected_path, corrected)
        aligned = import_alignment(self.root, "counting", "counting-add", "N01", corrected_path,
                                   "manual-measured-reviewed", "fixture reviewer", "Synthetic test only")
        self.assertEqual((base / receipt["files"]["transcript"]).read_bytes(), raw_original)
        self.assertFalse(aligned["publicationApproved"])
        self.assertNotEqual(aligned["transcriptHash"], receipt["transcriptHash"])
        timing = {"audioHash": receipt["audioHash"], "scriptHash": receipt["scriptHash"],
                  "transcriptHash": aligned["transcriptHash"], "method": "word-anchors-reviewed",
                  "reviewer": "fixture reviewer", "evidence": "Synthetic test only",
                  "cues": [{"unitId": "U1", "wordStart": 0, "wordEnd": 2, "atMs": 10}]}
        write_json(base / "timing.json", timing)
        check_timing(self.folder, self.teaching["narration"])
        self.collect_job(self.job(), True)
        new_receipt, new_original = check_receipt(self.folder, self.teaching["narration"])
        # Identical audio/transcript/script is compatible; a different WAV is not.
        new_receipt["audioHash"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "Stale corrected"):
            selected_words(self.folder, self.teaching["narration"], new_receipt, new_original)

    def test_correction_rejects_unreviewed_and_out_of_audio_words(self):
        job = self.job()
        self.collect_job(job)
        receipt, original = check_receipt(self.folder, self.teaching["narration"])
        path = self.root / "corrected.json"
        write_json(path, original)
        with self.assertRaisesRegex(ValueError, "review evidence"):
            import_alignment(self.root, "counting", "counting-add", "N01", path,
                             "manual-measured-reviewed", "", "")
        original["words"][0]["end_ms"] = 9000
        write_json(path, original)
        with self.assertRaisesRegex(ValueError, "bounds/order"):
            import_alignment(self.root, "counting", "counting-add", "N01", path,
                             "manual-measured-reviewed", "fixture", "Synthetic test only")
