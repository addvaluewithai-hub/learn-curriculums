# Mathematics I — أولى هندسة
**Editorial status:** **B01 Stage 04 canonical scene authoring and actual script-stage CI checks complete**. Five previously issued B01 IDs/orders remain stable; independent academic/human reviews, audio, real lesson SDK playback and release are **not complete**. **B02–B07 remain provisional**: B02 preserves historical Stage 02 drafts without issued IDs. No B02 gate advanced or source storage action performed.

## Intended audience and bilingual approach
First-year engineering students learning calculus. Egyptian Arabic natural spoken instruction introduces concepts alongside familiar standard English mathematical terms; exam-style questions/model answers in English with Arabic support. We assume basic arithmetic, factorization and Cartesian coordinates; actual placement/syllabus is **awaiting human input**, not verified.

## Course map from what is actually visible
1. **Preliminaries — printed pp. 1–20 (PDF images 4–13):** real number system, real line, order properties, sets, intervals, linear inequalities, absolute value and multi-factor/rational inequalities. Printed pp. **19–20 are Exercises (1)**, treated as practice coverage rather than an invented fifth lecture. **Stage 04 canonical lesson scene files (B01), before Chapter 1; publication still blocked.**
2. **Chapter 1 — printed pp. 21–53:** *Functions and Their Graphs*, including families, increasing/decreasing, limits and continuity. Stage 02 rewritten; structural lesson boundaries still await the next human gate.
3. **Chapter 2 — printed pp. 54–80:** visible start of differentiation and exercises; not scripted in this PR.
4. **Chapters 3–6 — table-of-contents only:** inverse functions and related differentiation, hyperbolic functions, Maclaurin and related topics, partial differentiation. Detailed pages are not provided, so no lesson drafting based on their unseen text.

## Master roadmap — provisional production Blocks (whole available book)

A **Block** is a bounded source/workflow unit, not a student lesson, ID, or guarantee that all pages are available. **B01 is currently active.** The suggested ranges beyond printed p. 80 are inferred from the table of contents and must not be taught as inspected content.

| Block | Proposed printed pages | Source availability | Prerequisite purpose / status |
|---|---|---|---|
| **B01 — Preliminaries** | **1–20** | Body supplied, editorially reviewed; exercises pp. 19–20 | Real-number and inequality foundations; **ACTIVE, Stage 03 five final editorial scripts/issued IDs** |
| **B02 — Functions, limits, continuity** | **21–53** | Body supplied, editorially reviewed | Depends on B01; five prior Stage 02 drafts retained, **inactive until authorized Block activation** |
| **B03 — Differentiation** | **54–80** | Body supplied but not scripted; coverage skimmed | Depends on B02 limits/function fluency; **future Stage 01** |
| **B04 — Inverse-related and exp/log functions** | **81–143 (inferred)** | **Contents only; pages not supplied** | Chapter 3 headings in contents; **blocked on actual body source** |
| **B05 — Hyperbolic functions** | **144–150 (inferred)** | **Contents only; pages not supplied** | Chapter 4 headings; **blocked** |
| **B06 — Maclaurin and applications** | **151–174 (inferred)** | **Contents only; pages not supplied** | Chapter 5 headings; **blocked** |
| **B07 — Partial derivatives** | **175–181 (inferred)** | **Contents only; pages not supplied** | Chapter 6 heading; **blocked** |
| Closing matter | Summary 182; references 186 (TOC) | Contents only | Not yet an instructional Block |

**Source-of-truth docs:** `references/SOURCE_MANIFEST.md` (exact file hash, provisional storage and rights), `references/SOURCE_COVERAGE.md` (PDF/printed-page map), and earlier `references/SOURCE_REVIEW.md` (historical page-level observations). B01 and B02 own separate durable `blocks/B01/STATUS.md` and `blocks/B02/STATUS.md`; root `STATUS.md` is the active-Block control plane.

**Legacy transition rule:** the full B01/B02 scripts and shared Stage 02 critique predate the new Blocks policy. Keep them untouched; acknowledge their real historical authorship, but neither invent a Stage 00 human approval nor advance B02 by default. `next` currently concerns B01 only, after an explicit future human authorization. After B01 Stage 04 human inspection, `next block` may activate B02 and reconcile its already-written draft/review evidence with available source; audio is a separate path.

## Block B01 — Preliminaries: Stage 03 issued identities, Stage 04 canonical scenes

**Workflow Block:** B01, printed source pp. **1–20**, PDF image pp. **4–13**. These **five stable lesson IDs and their explicit within-Block order (1–5)** are now **issued in the Stage 03 editorial outline**. Names are stable; a later editorial amendment must use explicit change control. There are **no B02 stable lesson IDs** yet. A Block is a workflow unit, **not** a student lesson.

| B01 order | Issued stable lesson ID / working title | Source (printed; PDF images) | Standalone objectives and independent assessment | Historical Stage 03 connected manuscript (no longer canonical speech) |
|---|---|---|---|---|
| **1** | `em1-prelim-real-sets` — Real Numbers, Order & Sets | **1–5; 4–6** | Rational/irrational classification, number-line order, membership/union/intersection; **RS-Q1–3** | `blocks/B01/final-scripts/em1-prelim-real-sets.md` |
| **2** | `em1-prelim-intervals-linear` — Intervals and Linear Inequalities | **5–8; 6–7** (order rules earlier) | Correct endpoint notation and OR/AND sets, sign flip under known negative division, compound bounds; **IL-Q1–3** | `blocks/B01/final-scripts/em1-prelim-intervals-linear.md` |
| **3** | `em1-prelim-absolute-value` — Absolute Value as Distance | **9–12; 8–9** | Distance, two-branch equation, bounded inequality, triangle inequality; **AV-Q1–3** | `blocks/B01/final-scripts/em1-prelim-absolute-value.md` |
| **4** | `em1-prelim-polynomial-sign` — Polynomial Inequalities and Sign Charts | **13–18; 10–12** | Zero factors, regions, repeated-root signs, strict/inclusive endpoints; **PS-Q1–3** | `blocks/B01/final-scripts/em1-prelim-polynomial-sign.md` |
| **5** | `em1-prelim-rational-sign` — Rational Inequalities and Combined Conditions | **13–18; 10–12**; exercise coverage **19–20; 13** | Numerator zero vs forbidden denominator, cancellation hole, rational+linear condition intersection; **RA-Q1–3** | `blocks/B01/final-scripts/em1-prelim-rational-sign.md` |

**Coverage & boundary decisions:** Stage 02 critique P-A–P-D led to **keep with internal parts** (P-A), **keep** (P-B), **keep with parts** (P-C), and **split** (P-D) into **two complete self-contained scripts**, giving **five B01 lessons**. Source pp. **13–18 overlap across the last two** because the photographed teaching is interwoven; **no unsupported exact split page** is claimed. Printed pp. 19–20 are the book's exercise bank; the authored independent questions are original, not transcriptions. Detailed learner-centered decisions, prerequisite checks and 15 matched question/feedback pairs: `blocks/B01/reviews/STAGE_03_BOUNDARY_DECISION.md`.

**Editorial authority transition completed:** `working-drafts/prelim-*.md` are archival Stage 02 inputs, and `blocks/B01/final-scripts/*.md` are historical Stage 03 manuscripts. **The canonical B01 words now live in `lessons/<id>/scenes/Sxx.json` narration and question feedback**. Lesson identity/objective/ordering lives in `lessons/<id>/lesson.json`. Any joined reading copy must be generated from the scene canon, not independently edited.

## Chapter 1 — existing provisional lessons, after the Preliminaries
| Working label (not stable ID) | Printed source pages | Learner objectives; independent check |
|---|---|---|
| **A. What makes a function?** | 21–25 | Interpret input/output, domain/range, domain restrictions and the vertical-line test. |
| **B. Reading the function family** | 25–35 | Recognize power/polynomial/rational versus trig/exp/log families and related graphs. |
| **C. Increasing/decreasing and the limit idea** | 35–40 | Interpret monotonic intervals and values approached around a point. |
| **D. Computing limits safely** | 40–46 | Apply valid limit laws, factoring/rationalization, one-sided reasoning and radians-based trigonometric limits. |
| **E. Continuity and piecewise functions** | 47–53 | Test the three continuity conditions and solve a parameter matching problem. |

Chapter 1 working drafts: `working-drafts/01-functions.md` to `working-drafts/05-continuity.md`.

## Concept/prerequisite map
- **Assumed/possibly diagnosed:** basic arithmetic with positive/negative values, fraction operations, solving equations, polynomial factorization, plotting axes, introductory trigonometry.
- **Taught in Module 0:** real numbers and sets → line/order and set operations → intervals and inequality solutions → absolute value as distance → factored polynomials, rational sign analysis and boundary exclusion.
- **Taught in Chapter 1 drafts:** domain/range using interval fluency → function families → increasing/decreasing → limits and their laws → continuity.
- **Deferred:** derivatives, formal epsilon–delta rigor, L'Hôpital, derivative rules and later-book chapters.

## B01 Stage 04 visual source (not yet runtime-approved)
Each of the five B01 lesson folders now owns `scenes/ConceptBoard.tsx` with a subject-specific neutral diagram and speech-gated content disclosure, plus `STORYBOARDS.md` and distinct scene-level 16:9/9:16 plans. **Actual recordings, 320px render review, word timings, bilingual listening and student-ready SDK playback remain UNTESTED**; no visual/runtime approval follows from source code alone. B02 illustrations are still only editorial suggestions until its own later stages.

## Evidence, freeze scope and next gate
- Original scanned source and checked access limits: `references/SOURCE_MANIFEST.md`, `references/SOURCE_COVERAGE.md`, `references/SOURCE_REVIEW.md`. The user chose to postpone private long-term PDF retention; no original bytes uploaded.
- **B01 Stage 03 (historic):** five reviewed complete connected manuscripts, IDs, source/objective map, 4→5 split rationale: `blocks/B01/reviews/STAGE_03_BOUNDARY_DECISION.md`.
- **B01 Stage 04 (current canonical):** **72 scene JSON files, 15 independent question scenes, 15 separate feedback clips, 87 clips**, five lesson-owned TSX boards and independent 16:9/9:16 storyboards. `blocks/B01/reviews/STAGE_04_SCENES.md` and `blocks/B01/STATUS.md`. A generic `tests/test_script_stage_ready.py` executes real `validate_lesson(...,"script")` in successful [GitHub Actions](https://github.com/addvaluewithai-hub/learn-curriculums/actions/runs/37952958546).
- **B02 historical Stage 02:** five complete provisional working drafts and the joint critique preserved in `working-drafts/01-functions.md`–`05-continuity.md` and `reviews/STAGE_02_CRITIQUE.md`. They were drafted under the former curriculum-wide workflow; **no new B02 gate, ID or lesson-boundary decision**.
- Academic/scientific, audio/listening, timing, lesson-specific preview/runtime and student publication reviews remain **untested**; `review.json` does not claim any passed reviews. No paid TTS.
- **STOP for B01 Stage 04 human inspection.** A later bare `next` authorizes **B01 Stage 05 audio pilot preparation/dry-run only** (paid dispatch requires separate approval); distinct `next block` may explicitly activate B02 editorial resumption after B01 inspection, reconciling historical B02 scripts/source access. No automatic move into B02.
