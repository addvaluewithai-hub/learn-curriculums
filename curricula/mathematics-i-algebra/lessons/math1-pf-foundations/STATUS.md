# math1-pf-foundations — Stage 04 authoring

- **Order:** 1. **Audience:** First-year engineering. **Source locator:** printed pages 1–2; PDF 3–5 within B01.
- **Coverage:** أساس الكسور الجبرية، درجة كثيرات الحدود وتصنيف Proper/Improper.
- **Canonical sources:** `lesson.json`; ordered `scenes/Sxx.json`; teaching visual `scenes/MathBoard.tsx`.
- **Counts:** 8 scenes, 6 teaching scenes, 2 question scenes, 2 separately narrated feedback clips, 10 audio-clip scripts (not recordings), 20 semantic units.
- **Assessment:** every objective mapped to actual teaching scenes and independent written question IDs in lesson.json. English question and Arabic support in question clip; English model answer plus explanatory Arabic is held until feedback clip.
- **Storyboards:** landscape 16:9 and independently reflowed portrait 9:16 described on each scene; cue-sensitive custom MathBoard contains staged equations. Question scene uses SDK question board; no model answer in its narration or component.
- **Actual script validation:** Python CI `tests/test_stage04_curriculum_authoring.py` invokes `validate_lesson(root, course, lesson, "script")`; regression tests and quality checks passed on earlier Stage04 commit, final CI rerun pending.
- **Non-claim:** no audio WAV, transcript, measured semantic timings, visual playback review, listening review, learner testing, independent academic/teaching approval, or release.
- **Editorial history:** Stage 03 frozen continuous reading copy is under `blocks/B01/final-scripts/math1-pf-foundations.md`; after Stage04 edit only canonical scene clips.
- **Next action:** human `next` Stage 05 pilot dry-run OR `next block` B02 Stage 01. STOP.
