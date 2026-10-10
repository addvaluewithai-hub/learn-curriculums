import io
import json
import sys
from pathlib import Path
import unittest
import wave

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from statics_b01_stage06_preflight import manifest,valid_url,audit_clip


class B01Stage06PreflightTest(unittest.TestCase):
    def test_manifest_covers_all_canonical_clips_without_audio_approval(self):
        index,clips=manifest()
        self.assertEqual(len(index["assets"]),69)
        self.assertEqual(len(clips),69)
        self.assertEqual(sum(a["kind"]=="pilot" for a in index["assets"]),5)
        self.assertEqual(sum(a["kind"]=="bulk" for a in index["assets"]),64)
        self.assertTrue(all(a["reviewStatus"]=="untested" for a in index["assets"]))

    def test_reject_other_https_hosts_and_cloudinary_query_params(self):
        with self.assertRaises(ValueError):
            valid_url("https://example.com/as9o12al/file.wav",".wav")
        with self.assertRaises(ValueError):
            valid_url("https://res.cloudinary.com/as9o12al/file.wav?x=1",".wav")

    def test_wav_word_bounds_and_missing_asr_not_equivalent_to_silence(self):
        stream=io.BytesIO()
        with wave.open(stream,"wb") as w:
            w.setnchannels(1);w.setsampwidth(2);w.setframerate(24000)
            w.writeframes(b"\0\0"*24000)
        audio=stream.getvalue()
        source={"script":"Start الميكانيكا."}
        tr={"schema_version":1,"type":"word_timestamps",
            "alignment_mode":"automatic","source_text":source["script"],
            "recognized_text":"ستارت الميكانيكا","word_count":2,"duration_ms":950,
            "words":[{"text":"ستارت","start_ms":200,"end_ms":400},
                     {"text":"الميكانيكا","start_ms":410,"end_ms":850}]}
        row={"lessonId":"A","clipId":"N01","jobId":"j","audioBytes":len(audio)}
        vtt=b"WEBVTT\n\n00:00:00.000 --> 00:00:01.000\nword\n"
        report=audit_clip(row,source,audio,json.dumps(tr).encode(),vtt)
        self.assertTrue(report["technicalDeliveryVerified"])
        self.assertEqual(report["wavDurationMs"],1000)
        self.assertEqual(report["humanListening"],"untested")
        self.assertFalse(report["wordCuesReviewed"])
        self.assertEqual(report["missingEnglishTokensInASR"],["start"])
        tr["words"][1]["start_ms"]=2000
        with self.assertRaises(ValueError):
            audit_clip(row,source,audio,json.dumps(tr).encode(),vtt)


if __name__=="__main__":
    unittest.main()
