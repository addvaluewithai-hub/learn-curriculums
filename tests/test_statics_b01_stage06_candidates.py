import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from statics_b01_stage06_candidates import find_spans,normalized_spans,partial_search_evidence,propose

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


    def test_conservative_arabic_orthography_has_unapproved_full_phrase_time(self):
        words=[{"text":"تخيل","start_ms":100},{"text":"ان","start_ms":300},
               {"text":"قدامك","start_ms":600},{"text":"كوبري","start_ms":1000}]
        self.assertEqual(normalized_spans(words,"تخيّل إن قدامك كوبري،"),[(0,3)])
        clip={"id":"N01","script":"تخيّل إن قدامك كوبري",
              "units":[{"id":"U01","text":"تخيّل إن قدامك كوبري"}]}
        item=propose(clip,{"jobId":"j","audioHash":"a","transcriptHash":"b"},
                    {"words":words})["units"][0]
        self.assertEqual(item["candidateStatus"],"asr-orthographic-candidate-unreviewed")
        self.assertEqual(item["atMs"],100)
        self.assertTrue(item["requiresHumanReview"])

    def test_partial_search_is_evidence_not_cue(self):
        words=[{"text":"تخيل","start_ms":100},{"text":"انه","start_ms":300},
               {"text":"قدامك","start_ms":600},{"text":"كوبري","start_ms":1000}]
        clip={"id":"N01","script":"تخيّل إن قدامك كوبري",
              "units":[{"id":"U01","text":"تخيّل إن قدامك كوبري"}]}
        item=propose(clip,{"jobId":"j","audioHash":"a","transcriptHash":"b"},
                    {"words":words})["units"][0]
        self.assertEqual(item["candidateStatus"],"asr-partial-search-hint-unreviewed")
        self.assertNotIn("atMs",item)
        self.assertIn("reviewSeekMs",item["searchHint"])

    def test_unheard_single_word_term_never_receives_offset(self):
        words=[{"text":"ستاتيكس","start_ms":1000}]
        self.assertIsNone(partial_search_evidence(words,"Statics"))
        clip={"id":"N02","script":"Statics","units":[{"id":"U2","text":"Statics"}]}
        item=propose(clip,{"jobId":"j","audioHash":"a","transcriptHash":"b"},
                    {"words":words})["units"][0]
        self.assertEqual(item["candidateStatus"],"needs-human-alignment")
        self.assertNotIn("atMs",item)

if __name__=="__main__":unittest.main()
