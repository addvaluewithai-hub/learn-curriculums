# Block B01 STATUS — Preliminaries, Engineering Mathematics I

**Date:** 2026-10-09  
**Block/source:** B01 (ACTIVE), `abd-el-salam-math-i-scan`, printed pp. **1–20**, PDF image pp. **4–13**; printed pp. 19–20 are the source exercise bank, not copied problems.  
**Branch and draft review:** `curriculum/engineering-math-1/stage-01-functions`, [PR #8](https://github.com/addvaluewithai-hub/learn-curriculums/pull/8), **open, draft, not merged**. B02 is inactive.

## Human stage and real current checkpoint

- **Last completed authorized gate: Stage 04 — five lessons decomposed into 72 canonical scene JSON files, with 15 written-question scenes and 15 separate feedback clips (87 clips total).** No progression to any next gate.
- **Issued B01 student lesson IDs and orders 1–5** were finalized in Stage 03 and retained unchanged:
  1. `em1-prelim-real-sets` — number system, line and sets; printed pp. 1–5; **14 scenes**.
  2. `em1-prelim-intervals-linear` — intervals and linear/compound inequalities; pp. 5–8; **15 scenes**.
  3. `em1-prelim-absolute-value` — distance, equations, inequalities, triangle inequality; pp. 9–12; **14 scenes**.
  4. `em1-prelim-polynomial-sign` — polynomial sign charts and repeated roots; pp. 13–18; **14 scenes**.
  5. `em1-prelim-rational-sign` — rational sign charts, forbidden denominator and combined constraints; pp. 13–18, exercise-bank coverage 19–20; **15 scenes**.
- **Canonical spoken/script source NOW:** `../../lessons/<stable-id>/lesson.json`, plus `scenes/Sxx.json` narration and question feedback in each of the five lesson folders. `blocks/B01/final-scripts/*.md` from Stage 03 are retained **for historical comparison only**, not as a separately editable final runtime script. Original Stage 02 working-drafts and joint critique also retained unmodified.
- **Stage 04 evidence and human review checkpoint:** `reviews/STAGE_04_SCENES.md`; Stage 03 rationale `reviews/STAGE_03_BOUNDARY_DECISION.md`; global `../../OUTLINE.md` shows fixed B01 identities/coverage. Each lesson owns a responsive `scenes/ConceptBoard.tsx`, independent `STORYBOARDS.md` directions for **16:9 and 9:16**, `review.json` with all six checks **untested**, and a separate lesson STATUS. No invented sourceHash or reviewer.
- **Source access and rights:** `../../references/SOURCE_MANIFEST.md`, `SOURCE_COVERAGE.md`; original PDF is **not publicly uploaded or proven retrievable by future agents**, rights unknown. The user expressly deferred durable PDF storage; no action requested here.

## Checks ACTUALLY done — evidence limited to what happened

- **GitHub readback:** all 72 scene texts and 15 post-attempt feedbacks mapped to the five Stage 03 manuscripts; **5/5 exact source-spoken-words parity**, removing Markdown emphasis formatting only. Three independent written questions per lesson, kept completely separate from feedback; 87 distinct clip IDs within their lessons.
- **Actual `--stage script` repository validation in GitHub CI:** new general `tests/test_script_stage_ready.py` invokes `validate_lesson(..., "script")` for each non-scaffold lesson (all five B01 lessons). [Production contracts workflow run 37952958546](https://github.com/addvaluewithai-hub/learn-curriculums/actions/runs/37952958546) completed **successfully**, including Python unit tests, authoring quality limits, default validation and existing fixture preview checks. **No local checkout**; this success is from GitHub Actions, not container commands.
- **Storyboards, component source and answer gates checked structurally**, but real lesson components have **not been built/played with their own recorded word timings**. The passing SDK/preview CI fixture is **not** a student lesson visual/runtime approval.
- **Untested independent reviews:** source/math professor sign-off; novice teaching trial; English/Arabic listening and formula pronunciation; delivered audio, measured word timestamps, 320px overflow/reduced motion, pause/replay/seek and actual SDK runtime playback. No paid TTS, accepted takes, platform DB or publication.

## STOP — two separately authorized next choices

- **`next`** (bare) = **B01 Stage 05 representative bilingual/formula audio pilot preparation (dry-run only)**, following audio guidance. **Paid TTS requires separate explicit approval**. Stop again after this gate.
- **`next block`** = **start/resume B02 Stage 01** following human inspection of B01 Stage 04 files, source re-access check and reconciliation of B02's preexisting historical Stage 01/02 scripts/critique; **do not invent B02 stable IDs or skip its newly required gates**. Deferred B01 audio/scientific approvals do not become `passed` by proceeding.
- Until the user chooses, **no future gate is authorized**. Corrections only revise Stage 04 and stop.
