import copy
from support import ProductionCase
from common import read_json, safe_path, source_hash, write_json
from scaffold import new_course, new_lesson
from validate import validate_all, validate_lesson
from handoff import export_course


class AuthoringTests(ProductionCase):
    def test_scaffold_is_draft_not_script_ready(self):
        new_lesson(self.root, "counting", "second", 2, "Second")
        self.assertTrue(validate_lesson(self.root, "counting", "second")["valid"])
        with self.assertRaises(ValueError):
            validate_lesson(self.root, "counting", "second", "script")

    def test_sources_objectives_and_storyboards_are_script_ready_without_sdk(self):
        result = validate_lesson(self.root, "counting", "counting-add", "script")
        self.assertEqual(result["clipCount"], 3)
        self.assertFalse(result["runtimeVerified"])
        self.assertFalse(result["publicationApproved"])

    def test_duplicate_order_and_existing_folder_rejected(self):
        with self.assertRaises(ValueError):
            new_lesson(self.root, "counting", "other", 1, "Other")
        with self.assertRaises(FileExistsError):
            new_course(self.root, "counting", "Other")

    def test_global_identity_collision_detected_across_courses(self):
        new_course(self.root, "another", "Another")
        new_lesson(self.root, "another", "counting-add", 1, "Other")
        with self.assertRaisesRegex(ValueError, "globally unique"):
            validate_all(self.root)

    def test_broken_assessment_and_question_before_teaching(self):
        path = self.folder / "lesson.json"
        lesson = read_json(path)
        lesson["objectives"][0]["assessedIn"] = ["unknown"]
        write_json(path, lesson)
        with self.assertRaisesRegex(ValueError, "assessment"):
            validate_lesson(self.root, "counting", "counting-add", "script")
        lesson["objectives"][0]["assessedIn"] = ["Q1"]
        lesson["scenes"] = ["S02", "S01"]
        write_json(path, lesson)
        with self.assertRaisesRegex(ValueError, "precedes"):
            validate_lesson(self.root, "counting", "counting-add", "script")

    def test_unknown_source_and_anchor_fail(self):
        self.teaching["sources"][0]["sourceId"] = "missing"
        self.save_scenes()
        with self.assertRaisesRegex(ValueError, "source locator"):
            validate_lesson(self.root, "counting", "counting-add", "script")
        self.teaching["sources"][0]["sourceId"] = "original"
        self.teaching["narration"]["units"][0]["text"] = "Not spoken"
        self.save_scenes()
        with self.assertRaisesRegex(ValueError, "anchor"):
            validate_lesson(self.root, "counting", "counting-add", "script")

    def test_paths_and_symlinks_cannot_escape_lesson(self):
        with self.assertRaises(ValueError):
            safe_path(self.folder, "../course.json")
        (self.folder / "escape").symlink_to(self.course)
        with self.assertRaises(ValueError):
            safe_path(self.folder, "escape/course.json")

    def test_bespoke_component_path_is_data_not_hardcoded_renderer_menu(self):
        (self.folder / "scenes/NewShape.tsx").write_text("export const NewShape = () => null;\n")
        self.teaching["visual"] = copy.deepcopy(self.teaching["visual"])
        self.teaching["visual"].update(renderer="brand-new-component", module="scenes/NewShape.tsx")
        self.save_scenes()
        self.assertTrue(validate_lesson(self.root, "counting", "counting-add", "script")["valid"])
        (self.folder / "scenes/NewShape.tsx").unlink()
        with self.assertRaisesRegex(ValueError, "module missing"):
            validate_lesson(self.root, "counting", "counting-add", "script")

    def test_review_cannot_survive_source_changes(self):
        path = self.folder / "review.json"
        review = read_json(path)
        review["sourceHash"] = source_hash(self.folder)
        review["checks"]["sources"] = {"status": "passed", "reviewer": "fixture reviewer", "evidence": "fixture note reviewed"}
        write_json(path, review)
        validate_lesson(self.root, "counting", "counting-add", "script")
        (self.course / "note.md").write_text("Changed source\n")
        with self.assertRaisesRegex(ValueError, "Stale editorial"):
            validate_lesson(self.root, "counting", "counting-add", "script")

    def test_no_fake_runtime_approval(self):
        path = self.folder / "review.json"
        review = read_json(path)
        review["sourceHash"] = source_hash(self.folder)
        review["checks"]["runtime"] = {"status": "passed", "reviewer": "x", "evidence": "x"}
        write_json(path, review)
        with self.assertRaisesRegex(ValueError, "before the preview"):
            validate_lesson(self.root, "counting", "counting-add", "script")

    def test_export_preserves_course_and_custom_assets_and_is_idempotent(self):
        (self.folder / "diagram.svg").write_text("<svg/>\n")
        output = export_course(self.root, "counting", "script")
        manifest = read_json(output / "handoff.json")
        self.assertFalse(manifest["publicationApproved"])
        self.assertEqual(manifest["preview"], "pending-sdk")
        self.assertEqual((output / "source/lessons/counting-add/diagram.svg").read_text(), "<svg/>\n")
        self.assertEqual(export_course(self.root, "counting", "script"), output)
        (output / "source/lessons/counting-add/diagram.svg").write_text("changed")
        with self.assertRaisesRegex(ValueError, "modified"):
            export_course(self.root, "counting", "script")

    def test_other_curriculum_work_does_not_block_export(self):
        new_course(self.root, "unfinished", "Unfinished")
        new_lesson(self.root, "unfinished", "unfinished-first", 1, "Draft")
        self.assertTrue(export_course(self.root, "counting", "script").is_dir())

    def test_different_export_stages_have_distinct_identity(self):
        draft = export_course(self.root, "counting", "draft")
        script = export_course(self.root, "counting", "script")
        self.assertNotEqual(draft, script)
