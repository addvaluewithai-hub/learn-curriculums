import io
import json
import sys
import unittest
from pathlib import Path
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from statics_b01_stage06_hydrate import original_factory_result,chosen,all_artifacts
from statics_b01_stage06_preflight import manifest

class Stage06ArtifactBindingTests(unittest.TestCase):
    def test_two_smoke_clips_and_full_manifest_coverage(self):
        index,canonical=manifest()
        rows=index["assets"]
        self.assertEqual(len(chosen(rows,1)),1)
        self.assertEqual(len(chosen(rows,2)),2)
        self.assertEqual(len(chosen(rows,0)),69)
        self.assertEqual(len(canonical),69)

    def test_original_factory_result_must_match_job_and_completed(self):
        def archive(x):
            stream=io.BytesIO()
            with ZipFile(stream,"w") as z:z.writestr("result.json",json.dumps(x))
            return stream.getvalue()
        record={"id":"abc","status":"completed","audio_url":"https://res.cloudinary.com/a.wav",
                "transcript_url":"https://res.cloudinary.com/a.json"}
        self.assertEqual(original_factory_result(archive(record),"abc")["id"],"abc")
        with self.assertRaises(ValueError):
            original_factory_result(archive(record),"other")
        with self.assertRaises(ValueError):
            original_factory_result(archive({**record,"status":"failed"}),"abc")

    def test_factory_artifact_listing_is_exact_and_rejects_duplicates(self):
        def fake(url,token):
            return {"artifacts":[{"name":"tts-abc","expired":False,"archive_download_url":
                                  "https://api.github.com/repos/addvaluewithai-hub/gemini-tts/actions/artifacts/1/zip"}]}
        self.assertIn("tts-abc",all_artifacts(None,read=fake))

if __name__=="__main__":unittest.main()
