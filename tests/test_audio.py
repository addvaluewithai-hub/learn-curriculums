from pathlib import Path
import subprocess
from unittest.mock import patch
import wave
from support import ProductionCase
from audio import collect, dispatch, prepare
from common import read_json, sha256, write_json
from media import check_receipt, check_timing


class AudioTests(ProductionCase):
    def job(self, clip="N01"):
        return prepare(self.root, "counting", "counting-add", clip, "t01")

    def delivery(self, job):
        payload = read_json(job)["client_payload"]
        audio = self.root / "delivered.wav"
        with wave.open(str(audio), "wb") as handle:
            handle.setnchannels(1)
            handle.setsampwidth(2)
            handle.setframerate(8000)
            handle.writeframes(b"\0\0" * 8000)
        texts = payload["request"]["text"].split()
        words = [{"text": value, "start_ms": index * 50, "end_ms": (index + 1) * 50}
                 for index, value in enumerate(texts)]
        transcript = {"schema_version": 1, "type": "word_timestamps", "alignment_mode": "fixture-asr",
                      "source_text": payload["request"]["text"], "recognized_text": " ".join(texts),
                      "duration_ms": len(words) * 50, "word_count": len(words), "words": words}
        result = {"id": payload["job_id"], "status": "completed", "audio_url": "https://example.test/audio.wav",
                  "transcript_url": "https://example.test/transcript.json", "metadata": payload["request"]["metadata"],
                  "transcript": {"status": "completed", "word_count": len(words), "duration_ms": transcript["duration_ms"]}}
        result_path, transcript_path = self.root / "result.json", self.root / "transcript.json"
        write_json(result_path, result)
        write_json(transcript_path, transcript)
        return result_path, audio, transcript_path

    def collect_job(self, job, select=False):
        result, audio, transcript = self.delivery(job)
        return collect(self.root, str(job.relative_to(self.root)), result, audio, transcript, select)

    def test_unique_jobs_and_no_generation_on_prepare_or_dry_run(self):
        first, second = self.job(), self.job()
        self.assertNotEqual(read_json(first)["client_payload"]["job_id"], read_json(second)["client_payload"]["job_id"])
        with patch("audio.subprocess.run") as call:
            report = dispatch(self.root, str(first.relative_to(self.root)))
            self.assertFalse(report["paidCall"])
            call.assert_not_called()

    def test_dispatch_intent_prevents_blind_retry_after_unknown_outcome(self):
        job = self.job()
        with patch("audio.shutil.which", return_value="gh"), patch("audio.subprocess.run", side_effect=subprocess.CalledProcessError(1, "gh")):
            with self.assertRaises(subprocess.CalledProcessError):
                dispatch(self.root, str(job.relative_to(self.root)), True)
        self.assertEqual(read_json(job.with_suffix(".dispatch.json"))["status"], "dispatch-started-outcome-unknown")
        with patch("audio.shutil.which", return_value="gh"), self.assertRaisesRegex(ValueError, "Already dispatched"):
            dispatch(self.root, str(job.relative_to(self.root)), True)

    def test_changed_script_rejects_prepared_job(self):
        job = self.job()
        self.teaching["narration"]["script"] += " changed"
        self.save_scenes()
        with self.assertRaisesRegex(ValueError, "Stale audio request"):
            dispatch(self.root, str(job.relative_to(self.root)))

    def test_actual_waveform_duration_and_never_automatic_publication(self):
        job = self.job()
        report = self.collect_job(job)
        self.assertEqual(report["durationMs"], 1000)
        self.assertFalse(report["publicationApproved"])
        receipt, transcript = check_receipt(self.folder, self.teaching["narration"])
        self.assertGreater(receipt["durationMs"], transcript["duration_ms"])
        self.assertTrue(report["warnings"])
        self.collect_job(job)

    def test_changed_take_requires_selection_and_old_take_survives(self):
        first, second = self.job(), self.job()
        self.collect_job(first)
        old = read_json(self.folder / "media/N01/receipt.json")
        with self.assertRaisesRegex(ValueError, "Different take"):
            self.collect_job(second)
        self.collect_job(second, True)
        self.assertTrue((self.folder / "media/N01" / old["files"]["audio"]).is_file())

    def test_wrong_result_and_transcript_hash_fail(self):
        job = self.job()
        result, audio, transcript = self.delivery(job)
        wrong = read_json(result)
        wrong["id"] = "another-job"
        write_json(result, wrong)
        with self.assertRaisesRegex(ValueError, "Wrong/incomplete"):
            collect(self.root, str(job.relative_to(self.root)), result, audio, transcript)
        self.collect_job(job)
        receipt = read_json(self.folder / "media/N01/receipt.json")
        path = self.folder / "media/N01" / receipt["files"]["transcript"]
        data = read_json(path)
        data["recognized_text"] += " changed"
        write_json(path, data)
        with self.assertRaisesRegex(ValueError, "Transcript changed"):
            check_receipt(self.folder, self.teaching["narration"])

    def test_timed_anchors_fail_on_wrong_phrase_or_timestamp(self):
        job = self.job()
        self.collect_job(job)
        receipt = read_json(self.folder / "media/N01/receipt.json")
        timing = {"audioHash": receipt["audioHash"], "scriptHash": receipt["scriptHash"],
                  "transcriptHash": receipt["transcriptHash"], "method": "word-anchors-reviewed",
                  "reviewer": "fixture reviewer", "evidence": "Synthetic test data only",
                  "cues": [{"unitId": "U1", "wordStart": 0, "wordEnd": 2, "atMs": 0}]}
        path = self.folder / "media/N01/timing.json"
        write_json(path, timing)
        check_timing(self.folder, self.teaching["narration"])
        timing["cues"][0]["atMs"] = 24
        write_json(path, timing)
        with self.assertRaisesRegex(ValueError, "first spoken word"):
            check_timing(self.folder, self.teaching["narration"])
        timing["cues"][0].update(atMs=0, wordEnd=3)
        write_json(path, timing)
        with self.assertRaisesRegex(ValueError, "do not match"):
            check_timing(self.folder, self.teaching["narration"])

    def test_same_job_cannot_replace_served_bytes(self):
        job = self.job()
        self.collect_job(job)
        result, audio, transcript = self.delivery(job)
        with wave.open(str(audio), "wb") as handle:
            handle.setnchannels(1)
            handle.setsampwidth(2)
            handle.setframerate(8000)
            handle.writeframes(b"\1\0" * 8000)
        with self.assertRaisesRegex(ValueError, "immutable take collision"):
            collect(self.root, str(job.relative_to(self.root)), result, audio, transcript, True)
