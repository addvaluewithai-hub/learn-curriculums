# Curriculum STATUS — Mathematics I, first-year engineering

**Updated:** 2026-10-09  
**Current gate:** **B01 Stage 04 complete — scenes/storyboards and script-stage checks**, **STOP for human inspection**. No paid sound, human academic pass, student publication or automatic B02 activation.

## Whole-course source and roadmap
- Course: `engineering-math-1`, Egyptian Arabic explanation with English math/exam language; source ID `abd-el-salam-math-i-scan`.
- **Global Block plan B01–B07:** `OUTLINE.md`; exact PDF/printed-page and missing-coverage map `references/SOURCE_COVERAGE.md`, manuscript/version/rights `references/SOURCE_MANIFEST.md`.
- **Source:** 43 photographed PDF pages covering printed pp. 1–80; original's SHA-256 is recorded in source manifest. Printed pp. beyond 80 in the table of contents only. **Future retrieval not verified; source storage deferred by the user**. No raw scan uploaded to this public repo.
- **Open, draft, unmerged GitHub PR:** [#8](https://github.com/addvaluewithai-hub/learn-curriculums/pull/8) on `curriculum/engineering-math-1/stage-01-functions`. `main` unchanged by this PR.
- **Legacy governance history:** Earlier Stage 01+02 scripts covered B01+B02 together under the old workflow. The new Stage 00/Blocks governance was backfilled transparently, not claimed as an originally approved Stage 00; `reviews/WORKFLOW_MIGRATION.md`.

## Active Block table

| Block | What is actually done | Gate / next authorization |
|---|---|---|
| **B01 — Preliminaries, printed pp. 1–20, ACTIVE** | Stage 03 five issued lesson IDs, **Stage 04 canonical scenes and boards complete**: **72 scenes**, **15 independent written questions + 15 post-attempt feedback clips**, **87 speech clips**. [B01 STATUS](blocks/B01/STATUS.md), [Stage 04 report](blocks/B01/reviews/STAGE_04_SCENES.md) | **Await B01 human inspection.** `next` → B01 Stage 05 **dry-run audio-pilot prep only**; `next block` → B02 editorial resumption, after checking source/history |
| **B02 — Functions & Limits, pp. 21–53, INACTIVE** | Historical five complete Stage 02 working drafts + shared critique preserved; no issued IDs or scenes | Requires later explicit `next block` and reinspection/source-evidence reconciliation. No automatic Stage 03 |
| **B03 — Differentiation, pp. 54–80** | Source body available/skimmed but no authoring | Planned |
| **B04–B07 — later chapters** | Index/contents-only; body pages missing | Blocked by missing original body |

## B01 canonical and archival artifacts
- **Five unchanged issued IDs, within-Block order 1–5**: `em1-prelim-real-sets`, `em1-prelim-intervals-linear`, `em1-prelim-absolute-value`, `em1-prelim-polynomial-sign`, `em1-prelim-rational-sign`. All now have `lessons/<id>/lesson.json`, ordered `scenes/Sxx.json`, `STORYBOARDS.md`, bespoke `scenes/ConceptBoard.tsx`, review metadata and lesson STATUS.
- **Stage 03 final manuscripts** remain at `blocks/B01/final-scripts/*.md` as source-history only. Spoken canon is now the **scene narration and separate feedback** files, not another editable master draft. Source-manuscript comparison and the Stage 03 keep/split/merge rationale: `blocks/B01/reviews/STAGE_03_BOUNDARY_DECISION.md`; Stage 04 production checks: `blocks/B01/reviews/STAGE_04_SCENES.md`.
- **B02 historical work remains untouched:** `working-drafts/01-functions.md`–`05-continuity.md`, joint Stage 02 `reviews/STAGE_02_CRITIQUE.md` (and original B01 working-drafts).

## Evidence and hard limits
- **Actual script-stage validation:** generic `tests/test_script_stage_ready.py` runs the repo's `validate_lesson(..., "script")` for all five authored Stage 04 lessons. GitHub Actions [run 37952958546](https://github.com/addvaluewithai-hub/learn-curriculums/actions/runs/37952958546) **PASSED**, along with repo Python tests, `tools/quality.py`, default CLI validation and shared-preview **fixture** tests. The container's GitHub DNS remained unavailable; do not claim local execution.
- **Verbatim dialogue parity:** 5/5 manuscript comparisons passed, checking 72 teaching/question scenes and all 15 explanatory feedback clips. Audio timings and scene-component visuals have not been tested through actual lesson playback. `review.json` for each lesson truthfully says source/teaching/audio/timing/visual/runtime **untested**.
- **Prior Stage 03 samples:** 17/17 focused arithmetic/sign checks passed; this doesn't certify expert mathematics or actual teaching effectiveness. First-year learner trial, faculty source fidelity and Arabic-English listening still unreviewed.
- **No** audio jobs, paid TTS, timestamped media, working playable lesson in SDK, import, student publication or `main` merge.

## Human stop
**STOP — no new stage authorized.** A user correction revises B01 Stage 04. A future bare `next` authorizes **B01 Stage 05 representative pilot preparation/dry-run** (never paid dispatch alone). The distinct command **`next block`** explicitly allows starting B02 Stage 01 after inspecting the B01 scene artifacts, while B01 voice/human reviews remain deferred and not approved. The user elected to postpone secure source storage; do not demand it during this checkpoint.
