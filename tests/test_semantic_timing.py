"""Synthetic deliveries exercise AI cue contracts, not real listening approval."""
from copy import deepcopy
import json
from audio import collect
from common import read_json, write_json
from media import check_timing
from support import ProductionCase
import test_audio


class SemanticTimingTests(ProductionCase):
    job = test_audio.AudioTests.job
    delivery = test_audio.AudioTests.delivery

    def deliver(self, repeated=False):
        if repeated:
            self.teaching["narration"]["script"] += " Two plus three"
            self.teaching["narration"]["units"][0]["occurrence"] = 2
            self.save_scenes()
        job = self.job()
        result, audio, transcript_path = self.delivery(job)
        transcript = read_json(transcript_path)
        # Different observed spelling supplied BEFORE immutable receipt collection.
        for index, value in enumerate(["تو", "بلس", "ثري"]):
            transcript["words"][index]["text"] = value
        if repeated:
            for index, value in enumerate(["تو", "بلس", "ثري"], 8):
                transcript["words"][index]["text"] = value
        transcript["recognized_text"] = " ".join(w["text"] for w in transcript["words"])
        write_json(transcript_path, transcript)
        collect(self.root, str(job.relative_to(self.root)), result, audio, transcript_path)
        base = self.folder / "media/N01"
        receipt = read_json(base / "receipt.json")
        first = 8 if repeated else 0
        self.timing = {
            "audioHash": receipt["audioHash"], "scriptHash": receipt["scriptHash"],
            "transcriptHash": receipt["transcriptHash"], "method": "semantic-word-anchors",
            "author": "ai:synthetic-test", "cues": [{"unitId": "U1", "wordStart": first,
                "wordEnd": first + 2, "atMs": transcript["words"][first]["start_ms"],
                "reason": "The observed transliteration names the intended counter groups in context."}],
        }
        self.path = base / "timing.json"
        self.transcript_path = base / receipt["files"]["transcript"]

    def check(self, timing=None):
        write_json(self.path, self.timing if timing is None else timing)
        return check_timing(self.folder, self.teaching["narration"])

    def test_transliteration_needs_author_decision_not_human_approval_or_asr_rewrite(self):
        self.deliver()
        original = self.transcript_path.read_bytes()
        review = (self.folder / "review.json").read_bytes()
        result = self.check()
        self.assertNotIn("reviewer", result)
        self.assertEqual(self.transcript_path.read_bytes(), original)
        self.assertEqual((self.folder / "review.json").read_bytes(), review)

    def test_author_selects_second_spoken_occurrence_using_observed_indices(self):
        self.deliver(repeated=True)
        self.assertEqual(self.check()["cues"][0]["atMs"], 400)

    def test_cannot_detach_a_cue_from_real_word_time_or_selected_take(self):
        self.deliver()
        variants = [
            (lambda t: t["cues"][0].update(atMs=24), "first spoken word"),
            (lambda t: t["cues"][0].update(atMs=-1), "outside recording"),
            (lambda t: t["cues"][0].update(atMs=float("inf")), "outside recording"),
            (lambda t: t["cues"][0].update(wordStart=True), "word range"),
            (lambda t: t["cues"][0].update(wordEnd=999), "word range"),
            (lambda t: t.update(audioHash="0" * 64), "Stale cue"),
            (lambda t: t.update(transcriptHash="0" * 64), "different transcript"),
        ]
        for mutate, message in variants:
            with self.subTest(message=message):
                timing = deepcopy(self.timing)
                mutate(timing)
                if message == "outside recording" and timing["cues"][0]["atMs"] == float("inf"):
                    # Deliberately malformed external JSON, bypass writer's finite-number guard.
                    self.path.write_text(json.dumps(timing))
                    with self.assertRaisesRegex(ValueError, message):
                        check_timing(self.folder, self.teaching["narration"])
                else:
                    with self.assertRaisesRegex(ValueError, message):
                        self.check(timing)

    def test_missing_unknown_duplicate_cues_and_unexplained_authoring_fail(self):
        self.deliver()
        variants = [
            (lambda t: t.update(cues=[]), "coverage"),
            (lambda t: t["cues"][0].update(unitId="UNKNOWN"), "coverage"),
            (lambda t: t["cues"].append(deepcopy(t["cues"][0])), "Duplicate"),
            (lambda t: t["cues"][0].update(reason=""), "reason"),
            (lambda t: t.update(author=""), "author"),
        ]
        for mutate, message in variants:
            with self.subTest(message=message):
                timing = deepcopy(self.timing)
                mutate(timing)
                with self.assertRaisesRegex(ValueError, message):
                    self.check(timing)
