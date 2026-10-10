"""Validate 69 durable B01 selections against exact source, not absent WAV bytes."""
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from common import clips_for,load_lesson,read_json,sha256

COURSE="engineering-mechanics-statics-y1"

class StaticsB01SourceBoundSelectedMedia(unittest.TestCase):
    def test_all_69_factory_results_and_receipts_are_pinned(self):
        block=ROOT/"curricula"/COURSE/"blocks"/"B01"
        index=read_json(block/"AUDIO_ASSETS.json")
        count=0
        for lesson_id in ("ems-y1-foundations-models","ems-y1-newton-gravity",
                          "ems-y1-units-conversions"):
            folder,lesson,scenes=load_lesson(ROOT,COURSE,lesson_id)
            rows={r["clipId"]:r for r in index["assets"] if r["lessonId"]==lesson_id}
            expected={c["id"]:c for c in clips_for(scenes)}
            self.assertEqual(set(rows),set(expected))
            for clip_id,clip in expected.items():
                row=rows[clip_id]
                media=folder/"media"/clip_id
                receipt=read_json(media/"receipt.json")
                self.assertEqual(receipt["schemaVersion"],1)
                self.assertEqual(receipt["clipId"],clip_id)
                self.assertEqual(receipt["jobId"],row["jobId"])
                self.assertEqual(receipt["scriptHash"],sha256(clip["script"]))
                self.assertRegex(receipt["audioHash"],"^[0-9a-f]{64}$")
                self.assertRegex(receipt["transcriptHash"],"^[0-9a-f]{64}$")
                self.assertGreater(receipt["durationMs"],0)
                self.assertEqual(receipt["files"]["audio"],
                                 "takes/"+row["jobId"]+"/audio.wav")
                self.assertEqual(receipt["files"]["transcript"],
                                 "takes/"+row["jobId"]+"/transcript.json")
                result=read_json(media/receipt["files"]["result"])
                self.assertEqual(result["id"],row["jobId"])
                self.assertEqual(result["status"],"completed")
                self.assertEqual(result["audio_url"],row["wav"])
                self.assertEqual(result["transcript_url"],row["transcript"])
                self.assertEqual(result["metadata"]["clipId"],clip_id)
                self.assertEqual(result["metadata"]["lessonId"],lesson_id)
                self.assertEqual(result["metadata"]["scriptHash"],receipt["scriptHash"])
                self.assertEqual(result["metadata"]["role"],clip["role"])
                count+=1
        self.assertEqual(count,69)

    def test_binaries_are_not_committed_or_misrepresented_as_handoff(self):
        # The real selected WAV/ASR bytes were verified in the separate CI hydrate
        # artifact, and are restored into a checkout only during Stage06 work.
        for media in (ROOT/"curricula"/COURSE/"lessons").glob("*/media"):
            self.assertFalse(any(media.rglob("audio.wav")))
            self.assertFalse(any(media.rglob("transcript.json")))
            self.assertFalse(any(media.rglob("timing.json")))

if __name__=="__main__":unittest.main()
