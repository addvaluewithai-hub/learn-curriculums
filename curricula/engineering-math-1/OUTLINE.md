# Mathematics I — أولى هندسة
**Editorial status:** new Stage 00 / Blocks governance **retrospectively documented** around legacy Stage 02 editorial work. Active B01; no Stage 03 permission. **Lesson boundaries remain provisional**. Labels P-A–P-D and A–E are **working labels, not issued stable lesson IDs**. No scenes, TTS or student publication.

## Intended audience and bilingual approach
First-year engineering students learning calculus. Egyptian Arabic natural spoken instruction introduces concepts alongside familiar standard English mathematical terms; exam-style questions/model answers in English with Arabic support. We assume basic arithmetic, factorization and Cartesian coordinates; actual placement/syllabus is **awaiting human input**, not verified.

## Course map from what is actually visible
1. **Preliminaries — printed pp. 1–20 (PDF images 4–13):** real number system, real line, order properties, sets, intervals, linear inequalities, absolute value and multi-factor/rational inequalities. Printed pp. **19–20 are Exercises (1)**, treated as practice coverage rather than an invented fifth lecture. **Stage 02 revised draft block; placed BEFORE Chapter 1 provisionally.**
2. **Chapter 1 — printed pp. 21–53:** *Functions and Their Graphs*, including families, increasing/decreasing, limits and continuity. Stage 02 rewritten; structural lesson boundaries still await the next human gate.
3. **Chapter 2 — printed pp. 54–80:** visible start of differentiation and exercises; not scripted in this PR.
4. **Chapters 3–6 — table-of-contents only:** inverse functions and related differentiation, hyperbolic functions, Maclaurin and related topics, partial differentiation. Detailed pages are not provided, so no lesson drafting based on their unseen text.

## Master roadmap — provisional production Blocks (whole available book)

A **Block** is a bounded source/workflow unit, not a student lesson, ID, or guarantee that all pages are available. **B01 is currently active.** The suggested ranges beyond printed p. 80 are inferred from the table of contents and must not be taught as inspected content.

| Block | Proposed printed pages | Source availability | Prerequisite purpose / status |
|---|---|---|---|
| **B01 — Preliminaries** | **1–20** | Body supplied, editorially reviewed; exercises pp. 19–20 | Real-number and inequality foundations; **active; legacy Stage 02 drafts/critique retained** |
| **B02 — Functions, limits, continuity** | **21–53** | Body supplied, editorially reviewed | Depends on B01; five prior Stage 02 drafts retained, **inactive until authorized Block activation** |
| **B03 — Differentiation** | **54–80** | Body supplied but not scripted; coverage skimmed | Depends on B02 limits/function fluency; **future Stage 01** |
| **B04 — Inverse-related and exp/log functions** | **81–143 (inferred)** | **Contents only; pages not supplied** | Chapter 3 headings in contents; **blocked on actual body source** |
| **B05 — Hyperbolic functions** | **144–150 (inferred)** | **Contents only; pages not supplied** | Chapter 4 headings; **blocked** |
| **B06 — Maclaurin and applications** | **151–174 (inferred)** | **Contents only; pages not supplied** | Chapter 5 headings; **blocked** |
| **B07 — Partial derivatives** | **175–181 (inferred)** | **Contents only; pages not supplied** | Chapter 6 heading; **blocked** |
| Closing matter | Summary 182; references 186 (TOC) | Contents only | Not yet an instructional Block |

**Source-of-truth docs:** `references/SOURCE_MANIFEST.md` (exact file hash, provisional storage and rights), `references/SOURCE_COVERAGE.md` (PDF/printed-page map), and earlier `references/SOURCE_REVIEW.md` (historical page-level observations). B01 and B02 own separate durable `blocks/B01/STATUS.md` and `blocks/B02/STATUS.md`; root `STATUS.md` is the active-Block control plane.

**Legacy transition rule:** the full B01/B02 scripts and shared Stage 02 critique predate the new Blocks policy. Keep them untouched; acknowledge their real historical authorship, but neither invent a Stage 00 human approval nor advance B02 by default. `next` currently concerns B01 only, after an explicit future human authorization. After B01 Stage 04 human inspection, `next block` may activate B02 and reconcile its already-written draft/review evidence with available source; audio is a separate path.

## Module 0: Preliminaries — provisional lessons BEFORE Functions
| Working label (not stable ID) | Printed source pages | Connected learner goal and independent check | Working-draft path |
|---|---|---|---|
| **P-A. Real numbers and sets** | 1–5 | Recognize rational/irrational/real numbers and number-line order; interpret set notation, membership, union and intersection; two independent number/set questions. | `working-drafts/prelim-01-real-numbers-sets.md` |
| **P-B. Intervals and linear inequalities** | 5–8 (order rules also pp. 1–2) | Express open/closed/half-open/unbounded intervals; solve single and compound linear inequalities with correct negative sign reversal; two independent questions. | `working-drafts/prelim-02-intervals-linear-inequalities.md` |
| **P-C. Absolute value** | 9–12 | Interpret distance, use properties, solve absolute-value equations and inequalities; two independent questions. | `working-drafts/prelim-03-absolute-value.md` |
| **P-D. Polynomial/rational inequalities** | 13–18, and exercises 19–20 for practice coverage | Make a sign chart, handle zeros and excluded denominators, combine conditions; two independent questions. | `working-drafts/prelim-04-polynomial-rational-inequalities.md` |

**Coverage:** the source's numbered preliminary pages 1–18 contain the instructional narrative and solved examples; pages 19–20 are the exercise bank. The independent questions are **authored instructional material**, not copies of those exercise pages. Stage 02 critique identified possible high cognitive load in P-D, B, C, and D; **no split has been approved**.

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

## Preliminary visual ideas (nonproduction)
A real-line zoom; set union/intersection overlap; bracket/circle endpoint examples; flipping order under negative scaling; distance arrows for absolute value; alternating signs on intervals and hollow excluded denominator point. These are **rough teaching ideas only**; formal storyboards and scene JSON must wait for Stage 04.

## Evidence and workflow
- Original scanned source and exact page map: `references/SOURCE_REVIEW.md`.
- Four **complete critically revised** Preliminaries continuous spoken drafts and five likewise revised Chapter 1 drafts are in `working-drafts/`. Together they contain **29** independent attempts with **29** separate explanatory feedback sections. Detailed review: `reviews/STAGE_02_CRITIQUE.md`.
- Stage 02 AI editorial critique and full-draft rewrites historically cover B01 + B02, but **this is not academic sign-off or learner testing**. A subsequent explicit human `next` **for active B01** authorizes **Stage 03 only**: decide keep/internal parts/split/merge using the critique and rewrite each final resulting script; STOP before scenes.
- **No stable lesson IDs/order have been issued.**

## Stage 02 boundary options for human consideration — NOT final decisions
- P-A: possibly internal sections on numbers/order vs set notation.
- P-B: likely keep as one connected inequality/interval unit with small checks.
- P-C: internal sections on distance, equations, inequalities and properties.
- P-D: potential split between polynomial signs and rational/compound conditions.
- A: input/output/domain-range and vertical-line sections may remain connected.
- B: high-priority candidate for algebraic vs trig/exponential/log families; graph shifts are authored pedagogical extension.
- C: high-priority candidate to separate monotonicity from the first limit concept.
- D: high-priority candidate to separate algebraic and trigonometric limits.
- E: likely connected internal parts on the continuity test, hole, jump and piecewise repair.
These are recommendations only. Source/assessment mapping, stable IDs and coherent rewritten openings/closings require the separately authorized Stage 03 decision.
