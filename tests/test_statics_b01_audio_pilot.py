"""Dry-run-only B01 TTS pilot contract; never sends a paid request."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from audio import dispatch, job_for, prepare  # noqa: E402
from common import read_json, sha256  # noqa: E402

COURSE = "engineering-mechanics-statics-y1"
PILOT_INDEX = ROOT / "curricula" / COURSE / "blocks" / "B01" / "PILOT_REQUESTS.json"


class StaticsB01AudioPilot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = read_json(PILOT_INDEX)
        cls.defaults = read_json(ROOT / "production.json")["audio"]

    def test_exactly_five_real_saved_requests_have_current_scripts(self):
        jobs = self.plan["jobs"]
        self.assertEqual(len(jobs), 5)
        self.assertEqual(len({j["jobId"] for j in jobs}), 5)
        self.assertEqual({j["clipId"] for j in jobs}, {"N02", "N13", "N09", "F02", "N12"})
        roles = []
        for item in jobs:
            with self.subTest(clip=item["clipId"], lesson=item["lessonId"]):
                relpath = item["path"]
                absolute = ROOT / relpath
                self.assertTrue(absolute.is_file())
                loaded_path, saved, _, clip = job_for(ROOT, relpath)
                self.assertEqual(loaded_path, absolute)
                self.assertEqual(saved["event_type"], "tts.generate")
                self.assertEqual(saved["client_payload"]["job_id"], item["jobId"])
                req = saved["client_payload"]["request"]
                self.assertEqual(req["text"], clip["script"])
                self.assertEqual(req["metadata"]["scriptHash"], sha256(clip["script"]))
                self.assertEqual(item["scriptHash"], sha256(clip["script"]))
                self.assertEqual(req["metadata"]["role"], clip["role"])
                self.assertEqual(req["voice"], self.defaults["voice"])
                self.assertEqual(req["style"], self.defaults["style"])
                self.assertEqual(req["routing"], "quality")
                self.assertEqual(req["format"], "wav")
                self.assertEqual(req["sample_rate"], 24000)
                self.assertEqual(req["transcript"], {"language_codes": [], "write_vtt": True})
                self.assertFalse(absolute.with_suffix(".dispatch.json").exists())
                roles.append(clip["role"])
        self.assertEqual(sorted(roles), ["feedback", "question", "teaching", "teaching", "teaching"])

    def test_actual_factory_dispatch_function_reports_dry_run_only(self):
        # Prevent any real subprocess call even if someone regresses the send=False path.
        with patch("audio.subprocess.run", side_effect=AssertionError("No dispatch permitted")):
            for item in self.plan["jobs"]:
                with self.subTest(clip=item["clipId"]):
                    status = dispatch(ROOT, item["path"], send=False)
                    self.assertEqual(status["status"], "dry-run")
                    self.assertEqual(status["jobId"], item["jobId"])
                    self.assertFalse(status["paidCall"])
                    self.assertEqual(status["repository"], self.defaults["repository"])
                    self.assertFalse((ROOT / item["path"]).with_suffix(".dispatch.json").exists())

    def test_actual_prepare_and_dry_run_are_consistent_with_saved_payload(self):
        # Create one short-lived CI fixture from the actual audio.prepare() path;
        # remove it even on assertion failure. Never sends or creates a media receipt.
        sample = self.plan["jobs"][2]  # bilingual question
        fixture = None
        try:
            with patch("audio.uuid4", return_value=SimpleNamespace(hex="cafe" * 8)):
                fixture = prepare(ROOT, COURSE, sample["lessonId"], sample["clipId"], "ci-probe")
            produced = read_json(fixture)
            saved = read_json(ROOT / sample["path"])
            self.assertEqual(produced["client_payload"]["request"],
                             saved["client_payload"]["request"])
            with patch("audio.subprocess.run", side_effect=AssertionError("No dispatch permitted")):
                report = dispatch(ROOT, str(fixture.relative_to(ROOT)), send=False)
            self.assertEqual(report["status"], "dry-run")
            self.assertFalse(report["paidCall"])
        finally:
            if fixture is not None:
                fixture.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
