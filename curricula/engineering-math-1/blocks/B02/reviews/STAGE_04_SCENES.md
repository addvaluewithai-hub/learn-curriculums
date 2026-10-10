# B02 Stage 04 — canonical scene scripts, responsive authoring and human checkpoint

**Date:** 2026-10-10. **Human authorization:** a new explicit `Next` after B02 Stage 03. **Scope:** B02 Stage 04 only — convert the EIGHT issued stable final editorial manuscripts into complete source-grounded `lesson.json` packages, ordered scene narration, separated written assessments and delayed feedback, semantic text anchors, 16:9 and 9:16 directions and bespoke React/Remotion board source. **Not** TTS, audio pilot, publishing, `main` merge or B03 authoring.

## Stage 03 → Stage 04 canonical speech handoff

| Issued B02 student order | Stable lesson ID | Curriculum runtime order | Teaching scenes | Independent question scenes | Separate feedback clips | Total scenes / speech clips |
|---:|---|---:|---:|---:|---:|---|
| 1 | `em1-functions-domain-range` | **6** | 11 | 4 | 4 | **15 / 19** |
| 2 | `em1-functions-algebraic-graphs` | **7** | 10 | 3 | 3 | **13 / 16** |
| 3 | `em1-functions-trig-exp-log` | **8** | 9 | 3 | 3 | **12 / 15** |
| 4 | `em1-functions-monotonicity` | **9** | 9 | 3 | 3 | **12 / 15** |
| 5 | `em1-limits-concept-one-sided` | **10** | 9 | 3 | 3 | **12 / 15** |
| 6 | `em1-limits-algebraic-methods` | **11** | 10 | 3 | 3 | **13 / 16** |
| 7 | `em1-limits-trigonometric` | **12** | 10 | 3 | 3 | **13 / 16** |
| 8 | `em1-functions-continuity` | **13** | 12 | 4 | 4 | **16 / 20** |
| **TOTAL** | **8 student lessons** | **6–13** | **80** | **26** | **26** | **106 scenes / 132 speech clips** |

**Why global order 6–13:** B01 already issued **five** stable student lessons at global orders **1–5**. The **B02 within-Block issued order 1–8** (which remains unchanged) is not equal to the global runtime `lesson.json.order`. The repository `validate_curriculum` rejects duplicate global lesson orders; the distinction prevents a real collision instead of renumbering B01.

For each B02 student lesson `curricula/engineering-math-1/lessons/<id>/` now holds `lesson.json`, every `scenes/Sxx.json`, `scenes/ConceptBoard.tsx`, `STORYBOARDS.md`, `review.json` and `STATUS.md`. The **canonical speech is now the scene narration and the separate post-attempt question feedback**, NOT the older `blocks/B02/final-scripts/<id>.md` manuscripts, which remain as **unchanged historical comparison**. Regenerate any joined reading copy from scenes instead of creating another independently edited master.

## Teaching and assessment conversion details

- **80 teaching scenes:** a complete authored narrative paragraph/concept per ordered scene, preserving Stage 03 original speech text except removing Markdown `**` emphasis formatting. Each scene carries the real book's **printed/PDF page locators**, original-independent-teaching-example notice, relevant objective IDs, full spoken narration and **occurrence-qualified spoken-phrase semantic units**. Text anchors are selected from whole spoken phrases/clauses, not invented timestamps; physical `atMs` and word indices **do not exist yet**.
- **26 written-attempt question scenes:** each has **complete original English exam wording plus Egyptian Arabic spoken support**, full-clause `QEN`/`QAR` semantic anchors and `readingUnitIds`. The script and the pre-attempt visual metadata **do not contain a model solution**.
- **26 separately stored post-submit `feedback` clips:** the original English model answer plus full Egyptian Arabic explanatory reasoning, full-clause `AEN`/`AAR` units and `answerUnitIds`. They are **not** extra normal teaching scenes, cannot be shown before a valid written attempt, and do not silently leak through question-phase visuals.
- **Stable IDs:** all **21** previously held B02 Stage 02 question IDs **A1–A4, B1–B5, C1–C4, D1–D4, E1–E4** retained together with Stage 03 new **B6, C5, C6, D5, D6**, no invented replacement IDs, and all 8 already issued lesson IDs/orders unchanged.
- **Outcome mapping:** every lesson objective has scene IDs `taughtIn` and later distinct question IDs `assessedIn`. The global runtime order and the local issued order are both documented, and no B01 scene or ID was modified.

## Visual direction (authored code and two layouts, not a render approval)

There are **eight lesson-owned, topic-specific SVG board modules**:
1. Input/output mapping and range/co-domain distinction
2. Coordinate line/parabola and denominator exclusion
3. Trig waves/exponential curve and excluded tangent inputs
4. Monotonic quadratic with distinct decreasing/increasing stretches
5. Two-sided approach and empty vs assigned point
6. Algebraic `0/0` investigation and sided sign restrictions
7. Radian unit-circle and sine/tangent ratio
8. Continuity with open/filled points and one-sided traces

Their `ConceptBoard.tsx` code uses the pinned SDK's `VisualProps`, `cueIsVisible` and `visibleQuestionParts` API; it is **source-controlled authoring code only**. It uses frame-derived speech-cue disclosure, neutral initial context, an independent horizontal left-graph/right-RTL layout and vertically stacked mobile layout. Both `visual.landscape` and `visual.portrait` are filled on EVERY scene; each `STORYBOARDS.md` explicitly includes mobile 320px, reduced-motion, English/Arabic wrap, question onset/attempt/feedback directions. **No verified real audio, word-timed cues, rendered device, mounted lesson component compile, or learner submission UX test** exists; source code/fixture CI can never substitute.

## Original source and scientific review boundaries

- Source ID `abd-el-salam-math-i-scan`: photo PDF scanned book printed **pp. 21–53**, PDF **14–30 LEFT**. Printed pp. **51–53 are Exercise (2)**, *not* new continuity theory. Stage 01/02 of B02 previously re-opened the original, with SHA-256 `a4d6e631fd887071db151c6e494519424dc46369376c5aeff6a5b58f72c99623`; **this Stage 04 used the already source-grounded finalized scripts, not a newly certified fresh complete original-PDF review**. Future authorized-agent retrieval of that source still unverified, and user expressly deferred private retention.
- Printed book **p.34/PDF p.20 right** appears to reverse domain/range for real exponentials. The B02 script teaches an independently reasoned correct pair and identifies the apparent book error. Need specialist source review; do not attribute corrected result to printed prose. Printed p.42 quotient-zero shorthand likewise not adopted as division-by-zero.
- No copyrighted scanned original was committed publicly. The teaching narratives, worked examples and exam items are authored pedagogy, not reproduced textbook exercises.

## Real automated checks and honest limits

- **GitHub tree readback:** found **13** `lesson.json` in this course (5 B01 + 8 B02), **178** `Sxx.json` scenes (72 + **106**), **13** lesson-owned TSX boards, storyboards and `review.json`. New B02 packages contain **146** source files committed in the Stage 04 authoring commit `86cc87c278e2f1734d47bd9652796083a243ccbe`.
- **ACTUAL GITHUB CI PASSED:** [Production contracts run #38045408233](https://github.com/addvaluewithai-hub/learn-curriculums/actions/runs/38045408233) for commit `e9d400606ee1d0246aa07480a3fceaa576c59bd1`, conclusion **success**, which includes persistent `tests/test_b02_stage04_scene_fidelity.py` (exact full speaking and feedback parity across **106** scenes/26 separate feedback, objective ordering, answer concealment/global order) and generic `tests/test_script_stage_ready.py` (actual `validate_lesson(..., "script")` on the 13 authored lessons); repository Python/quality and fixture preview checks also run. **This is technical evidence only**: actual B02 recorded-timed component rendering on a device, faculty review and learner experience remain `untested`. No local GitHub checkout claimed.
- **All six** checks in every B02 `review.json` remain deliberately `untested` with `sourceHash=null`; **no invented reviewer or acceptance**. Only technical structural passes can be asserted from CI. Maths professor source fidelity, student first-year trial, real recorded bilingual values/formula listening, exact cue timing, mobile layout, player SDK seek/pause/replay and human scientific approval are untested.
- No paid TTS jobs, media receipts, timed alignments, student player/persistence/DB import, public PDF, GitHub `main` merge or student publication.

## HUMAN STOP after Stage 04

**Stage 04 script/visual authoring is complete once repository checks pass; human inspection remains pending. STOP.** A future **bare `next`** asks for **B02 Stage 05 optional representative audio pilot preparation/dry-run only** and NEVER authorizes paid dispatch alone. Distinct **`next block`** can begin **B03 Stage 01** *after* the human inspects this Stage 04 scene/source handoff and the original B03 source is accessible; B02 audio and human scientific sign-off may remain expressly deferred/unapproved. No automatic B03 activation follows from this work.
