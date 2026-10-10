# math1-pf-two-linear — Stage 04 authoring

- **Order:** 3. **Audience:** First-year engineering. **Source locator:** printed pages 3–4; PDF 3–5 within B01.
- **Coverage:** معاملان A وB، وهوية البسط والتحقق والمجال.
- **Canonical sources:** `lesson.json`; ordered `scenes/Sxx.json`; teaching visual `scenes/MathBoard.tsx`.
- **Counts:** 8 scenes, 7 teaching scenes, 1 question scenes, 1 separately narrated feedback clips, 9 audio-clip scripts (not recordings), 18 semantic units.
- **Assessment:** every objective mapped to actual teaching scenes and independent written question IDs in lesson.json. English question and Arabic support in question clip; English model answer plus explanatory Arabic is held until feedback clip.
- **Storyboards:** landscape 16:9 and independently reflowed portrait 9:16 described on each scene; cue-sensitive custom MathBoard contains staged equations. Question scene uses SDK question board; no model answer in its narration or component.
- **Actual script validation:** Python CI `tests/test_stage04_curriculum_authoring.py` invokes `validate_lesson(root, course, lesson, "script")`; regression tests and quality checks passed on earlier Stage04 commit, final CI rerun pending.
- **Non-claim:** no audio WAV, transcript, measured semantic timings, visual playback review, listening review, learner testing, independent academic/teaching approval, or release.
- **Editorial history:** Stage 03 frozen continuous reading copy is under `blocks/B01/final-scripts/math1-pf-two-linear.md`; after Stage04 edit only canonical scene clips.
- **Next action:** human `next` Stage 05 pilot dry-run OR `next block` B02 Stage 01. STOP.
