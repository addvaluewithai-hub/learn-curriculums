# B01 Stage 04 — canonical script/scene authoring and human checkpoint

**Date:** 2026-10-09. **Scope:** active B01 (printed pp. 1–20; photographed PDF pp. 4–13), not B02.  
**Authorization:** new human `next` after the B01 Stage 03 manuscript/IDs gate. No `next block`, audio payment, merge or student publication was requested.  
**Source ID:** `abd-el-salam-math-i-scan`. Original retention remains `chat-only-temporary` and was expressly deferred by the user; see `../../references/SOURCE_MANIFEST.md`. Newly written diagrams, numerical questions and examples are **authored teaching material**, not copied original book exercises.

## Canonical file handoff (5 previously issued IDs/order)

| Lesson ID | B01 order | Teaching scenes | Question/attempt scenes | Separate feedback clips | Total scenes / clips | Visual authoring |
|---|---:|---:|---:|---:|---:|---|
| `em1-prelim-real-sets` | 1 | 11 | 3 | 3 | 14 / 17 | number line and set overlap |
| `em1-prelim-intervals-linear` | 2 | 12 | 3 | 3 | 15 / 18 | interval boundaries and rays |
| `em1-prelim-absolute-value` | 3 | 11 | 3 | 3 | 14 / 17 | point-to-point distance on line |
| `em1-prelim-polynomial-sign` | 4 | 11 | 3 | 3 | 14 / 17 | factored-root regions and unknown signs |
| `em1-prelim-rational-sign` | 5 | 12 | 3 | 3 | 15 / 18 | numerator zeros vs forbidden denominator |

**Totals:** **72 ordered scenes = 57 teaching scenes + 15 written-attempt question scenes**, with **15 separate feedback clips**; **87 speech clips**. The existing **15 independent questions and their English model answers/Egyptian-Arabic explanations** are preserved; no new exam exercises invented during Stage 04.

Each `lessons/<id>/` now has `lesson.json`, all ordered `scenes/Sxx.json`, `scenes/ConceptBoard.tsx`, `STORYBOARDS.md`, `review.json` and `STATUS.md`. No new `lesson.json` identifiers for B02. The Stage 03 manuscript remains an **unchanged historical manuscript for comparison**. From this checkpoint onwards **scene narration and question feedback scripts are the canonical working speech**; any joined reading copy must be **generated**, not independently edited.

## Semantic and assessment integrity

- One meaningful narrated idea per teaching scene (a cohesive original paragraph); writing/diagram cues are **verbatim full spoken clauses**, refined from earlier substring markers. Every `narration.units[].text` exists in its clip and has explicit positive `occurrence` and intended visual reveal.
- The English exam clause and its natural Arabic support are complete `QEN`/`QAR` units within a **question-role narration clip**. `readingUnitIds` are explicitly mapped; the full prompt remains visible for written attempts.
- **No model answer** is inside pre-attempt scene narration or pre-attempt visual params. Each assessment's answer, English model solution and Egyptian-Arabic explanatory feedback occur only in `question.answer` and **separate `question.feedback` clip**. `answerUnitIds` anchor both complete feedback clauses. **Real onset times are not invented.**
- Lesson objectives map to earlier teaching scenes through `taughtIn` and to later independent question IDs through `assessedIn`; no questions precede their first mapped teaching explanation.
- `visual.landscape` and `visual.portrait` contain **independent 16:9 and 9:16** instructions per scene, with extra ordered page-by-page plans in `STORYBOARDS.md`. Each lesson owns a non-identical subject-specific React/Remotion board, with neutral initial diagrams and phase-gated answer disclosure. Portrait explicitly stacks content for small screens instead of scaling down desktop.
- For each of the five manuscripts, an independent connected-text readback compared Stage 03 speech paragraphs to their ordered Stage 04 teaching scenes (**formatting-only bold removal**) and verified question/feedback text **character-for-character**, **5/5 passed**.

## ACTUALLY EXECUTED verification

- **Actual repository Python script-stage validation runs in CI:** added a generic, course/lesson-ID-independent test `tests/test_script_stage_ready.py` that discovers all non-scaffold authored `lesson.json` and calls `validate_lesson(..., "script")` for each one. It **does not** force Stage 00/scaffold-only lessons to be script-complete.
- **GitHub Actions Production contracts**: [run 37952958546](https://github.com/addvaluewithai-hub/learn-curriculums/actions/runs/37952958546), on commit `2759a04c1ab7aea91aeb018a7067cf3aaccb669e`, **conclusion: success**. Workflow executes `python3 -m unittest discover -s tests -v` (including new actual script-stage test), `python3 tools/quality.py`, default draft validation and existing pinned SDK preview fixture tests/build. These checks are **technical/structural**, not independent scientific or student-playback review.
- Separate GitHub readback verified scene/lesson/source paths, **15/15** English+Arabic question/feedback pairings, semantic unit membership, root/lesson objective mappings and no pre-attempt answer in spoken/visual prompt. The prior Stage 03 **17/17** targeted arithmetic checks were performed in the earlier gate; no new independent exhaustive math proof is claimed here.
- **No local checkout**: container DNS cannot resolve `github.com`, so **local commands did not run here**; actual Python checks above are evidenced by **GitHub Actions**, not by this environment.

## Explicit blockers — NOT approved

- **Academic/source and novice teaching review: UNTESTED**. No faculty member certified faint photographed formulas, source fidelity or all independently authored solutions, and no first-year learners trialled this teaching.
- **Audio & listening: UNTESTED.** No WAV, Gemini TTS job, pilot voice value/pronunciation check or paid dispatch.
- **Timing: UNTESTED.** Units carry *textual* occurrence anchors, not real `atMs`, timestamps or word positions. Math formula pronunciation/English clause pacing should be checked in the future representative pilot.
- **Visual/runtime: UNTESTED.** Source-controlled TSX and responsive written storyboards are not proof of actual component compilation/overflow checks for these real lessons in the pinned SDK, correct reduced-motion behavior, 320px screen performance, seek/pause/replay, or learner submit/feedback. Existing CI preview tests use fixtures; these real lessons lack recordings/timings and cannot be served as verified playable lessons yet. Keep `review.json` fields `untested` (no invented reviewer, `passed` or `sourceHash`).
- **Original PDF private persistence: DEFERRED BY USER**, not uploaded to public GitHub. Rights unknown; B02/B03 source inspection later still needs actual access.

## Human stop and two distinct next choices

**B01 Stage 04 source authoring and script checks complete, pending human inspection. STOP.**
- Future **`next`** means **B01 Stage 05 optional audio-pilot *preparation/dry-run only***, with actual paid dispatch requiring separate explicit approval.
- Future **`next block`** means **activate B02 Stage 01/editorial resumption**, reconciling already preserved Stage 01/02 historical drafts and source accessibility first; B01 audio and external academic reviews remain explicitly deferred. No automatic B02 authorization inferred from this Stage 04.
