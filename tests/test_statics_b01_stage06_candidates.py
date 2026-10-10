import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from statics_b01_stage06_candidates import find_spans,propose

class B01CueCandidateTests(unittest.TestCase):
    def test_exact_spans_and_repeated_anchors_are_candidates_not_reviews(self):
        words=[{"text":"Statics","start_ms":300},{"text":"is","start_ms":800},
               {"text":"Statics","start_ms":2000},{"text":"is","start_ms":2600}]
        self.assertEqual(find_spans(words,"Statics is"),[(0,1),(2,3)])
        clip={"id":"N01","script":"Statics is Statics is",
              "units":[{"id":"U01","text":"Statics is","occurrence":2}]}
        receipt={"jobId":"j","audioHash":"h","transcriptHash":"t"}
        r=propose(clip,receipt,{"words":words})
        self.assertEqual(r["units"][0]["wordStart"],2)
        self.assertEqual(r["units"][0]["atMs"],2000)
        self.assertTrue(r["units"][0]["requiresHumanReview"])
        self.assertEqual(r["units"][0]["candidateStatus"],"asr-exact-candidate-unreviewed")
    def test_missing_terms_never_produce_guessed_word_offset(self):
        clip={"id":"N02","script":"Newton's Law","units":[{"id":"U1","text":"Newton's Law"}]}
        receipt={"jobId":"j","audioHash":"h","transcriptHash":"t"}
        r=propose(clip,receipt,{"words":[{"text":"قانون","start_ms":0}]})
        self.assertEqual(r["units"][0]["candidateStatus"],"needs-human-alignment")
        self.assertNotIn("atMs",r["units"][0])

if __name__=="__main__":unittest.main()
