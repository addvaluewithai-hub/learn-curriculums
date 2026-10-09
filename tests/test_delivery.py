"""Regression tests for artifact integrity, independent of semantic approval."""
import copy
import hashlib
from pathlib import Path
import tempfile
import unittest
import wave
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from verify_delivery import verify


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.audio = Path(self.tmp.name) / "clip.wav"
        with wave.open(str(self.audio), "wb") as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(8000)
            wav.writeframes(b"\0\0" * 80000)
        self.result = {"id": "clip-take-1", "status": "completed",
                       "audio_url": "https://example.test/audio.wav", "transcript_url": "https://example.test/transcript.json",
                       "transcript": {"status": "completed", "word_count": 1, "duration_ms": 8000}}
        self.transcript = {"schema_version": 1, "type": "word_timestamps", "alignment_mode": "asr",
                           "source_text": "Pressure يعني ضغط", "recognized_text": "ضغط", "duration_ms": 8000,
                           "word_count": 1, "words": [{"text": "ضغط", "start_ms": 6000, "end_ms": 8000}]}

    def test_trailing_silence_and_unrecognized_english_are_not_structural_failure(self):
        report = verify(self.result, self.transcript, self.audio, expected_job="clip-take-1")
        self.assertTrue(report["structural_valid"])
        self.assertFalse(report["publication_approved"])
        self.assertEqual(report["measured_duration_ms"], 10000)
        self.assertEqual(report["recognized_speech_end_ms"], 8000)
        self.assertTrue(any("pressure" in w for w in report["warnings"]))
        self.assertTrue(any("opening interval" in w for w in report["warnings"]))

    def test_out_of_waveform_words(self):
        self.transcript["duration_ms"] = 11000
        self.result["transcript"]["duration_ms"] = 11000
        self.transcript["words"][0]["end_ms"] = 11000
        self.assertFalse(verify(self.result, self.transcript, self.audio)["valid"])

    def test_stale_hash_and_job(self):
        self.assertFalse(verify(self.result, self.transcript, self.audio, "0" * 64)["valid"])
        self.assertFalse(verify(self.result, self.transcript, self.audio, expected_job="other")["valid"])
        digest = hashlib.sha256(self.audio.read_bytes()).hexdigest()
        self.assertTrue(verify(self.result, self.transcript, self.audio, digest)["valid"])

    def test_invalid_timed_artifacts(self):
        for mutate in (
            lambda r, t: r.update(status="queued"),
            lambda r, t: t.update(words=[], word_count=0),
            lambda r, t: t["words"][0].update(start_ms=float("nan")),
            lambda r, t: t["words"][0].update(start_ms=-1),
            lambda r, t: r["transcript"].update(duration_ms=9000),
        ):
            r, t = copy.deepcopy(self.result), copy.deepcopy(self.transcript)
            mutate(r, t)
            self.assertFalse(verify(r, t, self.audio)["valid"])

    def test_recognized_end_is_not_forced_to_waveform_end(self):
        self.transcript["duration_ms"] = 10000
        self.result["transcript"]["duration_ms"] = 10000
        self.assertTrue(verify(self.result, self.transcript, self.audio)["valid"])


if __name__ == "__main__":
    unittest.main()
