# Curriculum STATUS — Engineering Mathematics I (أولى هندسة)

**Updated:** 2026-10-10  
**ACTIVE source Block: B02** — Functions, Graphs, Limits and Continuity, printed book pp. **21–53**.  
**Last human-authorized gate completed: B02 Stage 04 — canonical scene/script authoring, source-controlled boards and technical checks. STOP for human inspection.**  
**Draft PR / branch:** [#8](https://github.com/addvaluewithai-hub/learn-curriculums/pull/8) / `curriculum/engineering-math-1/stage-01-functions`, **open/draft and unmerged**.

## Original book, source access and full-course roadmap
- `engineering-math-1`, first-year engineering; Egyptian Arabic narrated teaching, English exam prompts/math terminology and spoken Arabic comprehension; English model answer + Egyptian Arabic explanatory feedback after written attempts.
- Original `abd-el-salam-math-i-scan`, photographed 43-page scanned PDF, printed book **pp. 1–80** only. Source metadata and actual earlier checked SHA-256 `a4d6e631fd887071db151c6e494519424dc46369376c5aeff6a5b58f72c99623`: `references/SOURCE_MANIFEST.md`, `SOURCE_COVERAGE.md`. Original future authorized-agent/private retrieval remains **unverified**; user expressly postponed durable private PDF storage. Copyrighted scan **not uploaded to public GitHub**. Printed beyond p. 80 is contents-only, not actual inspectable teaching.
- Whole-course Blocks B01–B07 and issued student IDs/coverage: `OUTLINE.md`. Do not mistake a production Block for one student lesson.
- Source caveat in B02: printed **p.34** appears to reverse the real exponential domain/range pair, inconsistent with its graph and standard math; B02 teaching uses independently checked correct math and explicitly flags possible printed typo for qualified human review. Printed p.42 quotient-zero shorthand also needs one-sided sign conditions. No source/faculty sign-off.

## Per-Block status — no invented approvals
| Block | Actual authoring and tests | Current state |
|---|---|---|
| **B01 — Preliminaries, printed 1–20** | **5 issued stable student lesson IDs** at global runtime orders **1–5**. Stage 04 **72 scene files, 15 written questions + 15 withheld feedback = 87 speech clips**, prior actual script CI passed. `blocks/B01/STATUS.md`. | **INACTIVE since next block**. Audio, professor/learner sign-off and real preview all **untested/deferred**. |
| **B02 — Functions/Limits/Continuity, printed 21–53** | **8 issued stable student IDs** with local Block order **1–8** and unique global runtime `lesson.json.order` **6–13**. Stage 04 **106 scenes = 80 teaching + 26 independent written questions, with 26 separate post-attempt feedback clips = 132 speech clips**. 8 subject-specific React/Remotion `ConceptBoard.tsx` source files and independent 16:9/9:16 `STORYBOARDS.md`. `blocks/B02/STATUS.md`, `blocks/B02/reviews/STAGE_04_SCENES.md`. | **ACTIVE — Stage 04 authoring complete, awaiting human inspection**. Real source/teaching/audio/timing/visual/runtime approvals **untested**, no real B02 playback. |
| **B03 — Differentiation, printed 54–80** | Original body was available in prior source inspection but no active authoring. | Only starts by explicit future `next block`, re-access actual source first. |
| **B04–B07** | Later book chapters visible only as table-of-contents headings; original body absent. | Blocked until actual pages supplied. |

## What is now canonical for B02 and what remains historical
- **Stable issued B02 IDs/order:** `em1-functions-domain-range` (1), `em1-functions-algebraic-graphs` (2), `em1-functions-trig-exp-log` (3), `em1-functions-monotonicity` (4), `em1-limits-concept-one-sided` (5), `em1-limits-algebraic-methods` (6), `em1-limits-trigonometric` (7), `em1-functions-continuity` (8). No stable IDs/order changed from Stage 03. Source coverage and dependency map in `OUTLINE.md`.
- **Canon AFTER Stage 04:** `lessons/<id>/lesson.json` and all ordered `scenes/Sxx.json`, including separate `question.feedback` clips and full spoken-phrase semantic units. The eight older `blocks/B02/final-scripts/<id>.md` remain **unchanged historical comparison**, not a second editable final master. Historical Stage 02 drafts and earlier joint-course critique also preserved.
- **26/26 independent exam prompt IDs and delayed feedback** remain mapped, preserving **21** older B02 assessment IDs and **five** new Stage 03 transfer questions, plus B01's unchanged 15/15. No audio jobs, clip takes, voice pilot, media receipt, real transcript/timing, player or student publication.

## Evidence, limitations and human STOP
- **GitHub structural readback:** 13 curriculum lessons total, **178 canonical scene files** (B01 72 + B02 106), 13 source-controlled boards/storyboards/review JSON; source-specific **B02 exact word-parity** with Stage 03 scripts enforced by `tests/test_b02_stage04_scene_fidelity.py`; all authored non-scaffold lesson packages checked by real `validate_lesson(...,"script")` in CI via `tests/test_script_stage_ready.py`. Track actual current GitHub Actions conclusion in the Stage 04 report/PR, never claim CI ran locally.
- **No human approvals:** `review.json` sourceHash null and six statuses `untested` for each B02 lesson. Source-controlled visuals/fixture SDK build **are not** real 16:9/9:16 playback certification. Mathematics professor source/faint formulas, first-year learner trial, mathematical pronunciation and timed cue alignment remain outstanding.
- **STOP:** Next new bare **`next` → B02 Stage 05 optional representative TTS pilot *preparation/dry-run only*** (paid dispatch needs separately explicit approval). Distinct **`next block` → B03 Stage 01**, only after user inspects B02 Stage 04 and we re-open genuine B03 body. B02 audio/scientific sign-off may stay deferred and unapproved. No automatic Stage 05, B03, public PDF upload, main merge or student release.
