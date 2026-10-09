from support import ProductionCase
from common import source_hash, read_json, write_json
from validate import validate_lesson
from handoff import export_course


class RuntimeReviewTests(ProductionCase):
    def setUp(self):
        super().setUp()
        write_json(self.root / "preview-sdk/sdk-version.json", {"version": "0.2.0", "sha256": "a" * 64})

    def test_runtime_review_requires_exact_sdk_and_current_source(self):
        review = read_json(self.folder / "review.json")
        review["sourceHash"] = source_hash(self.folder)
        review["checks"]["runtime"] = {"status": "passed", "reviewer": "fixture test", "evidence": "Synthetic declaration for binding test"}
        write_json(self.folder / "review.json", review)
        with self.assertRaisesRegex(ValueError, "different SDK"):
            validate_lesson(self.root, "counting", "counting-add", "script")
        review["checks"]["runtime"].update(runtimeVersion="0.2.0", runtimeArtifactHash="a" * 64)
        write_json(self.folder / "review.json", review)
        self.assertTrue(validate_lesson(self.root, "counting", "counting-add", "script")["runtimeVerified"])
        write_json(self.root / "preview-sdk/sdk-version.json", {"version": "0.2.1", "sha256": "b" * 64})
        with self.assertRaisesRegex(ValueError, "different SDK"):
            validate_lesson(self.root, "counting", "counting-add", "script")

    def test_handoff_identity_changes_with_sdk_even_when_content_does_not(self):
        first = export_course(self.root, "counting", "script")
        self.assertFalse(read_json(first / "handoff.json")["runtimeVerified"])
        write_json(self.root / "preview-sdk/sdk-version.json", {"version": "0.2.1", "sha256": "b" * 64})
        self.assertNotEqual(first, export_course(self.root, "counting", "script"))
