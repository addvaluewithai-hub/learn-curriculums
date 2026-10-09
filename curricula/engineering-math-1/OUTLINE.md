# Mathematics I — أولى هندسة
**Editorial status:** Stage 01 / **provisional** module and lesson split. Labels P-A–P-D and A–E are **working labels, not issued stable lesson IDs**. No scenes, TTS or student publication.

## Intended audience and bilingual approach
First-year engineering students learning calculus. Egyptian Arabic natural spoken instruction introduces concepts alongside familiar standard English mathematical terms; exam-style questions/model answers in English with Arabic support. We assume basic arithmetic, factorization and Cartesian coordinates; actual placement/syllabus is **awaiting human input**, not verified.

## Course map from what is actually visible
1. **Preliminaries — printed pp. 1–20 (PDF images 4–13):** real number system, real line, order properties, sets, intervals, linear inequalities, absolute value and multi-factor/rational inequalities. Printed pp. **19–20 are Exercises (1)**, treated as practice coverage rather than an invented fifth lecture. **Stage 01 expanded draft block; placed BEFORE Chapter 1.**
2. **Chapter 1 — printed pp. 21–53:** *Functions and Their Graphs*, including families, increasing/decreasing, limits and continuity. Stage 01 drafted previously; still awaiting Stage 02 critique.
3. **Chapter 2 — printed pp. 54–80:** visible start of differentiation and exercises; not scripted in this PR.
4. **Chapters 3–6 — table-of-contents only:** inverse functions and related differentiation, hyperbolic functions, Maclaurin and related topics, partial differentiation. Detailed pages are not provided, so no lesson drafting based on their unseen text.

## Module 0: Preliminaries — provisional lessons BEFORE Functions
| Working label (not stable ID) | Printed source pages | Connected learner goal and independent check | Working-draft path |
|---|---|---|---|
| **P-A. Real numbers and sets** | 1–5 | Recognize rational/irrational/real numbers and number-line order; interpret set notation, membership, union and intersection; two independent number/set questions. | `working-drafts/prelim-01-real-numbers-sets.md` |
| **P-B. Intervals and linear inequalities** | 5–8 (order rules also pp. 1–2) | Express open/closed/half-open/unbounded intervals; solve single and compound linear inequalities with correct negative sign reversal; two independent questions. | `working-drafts/prelim-02-intervals-linear-inequalities.md` |
| **P-C. Absolute value** | 9–12 | Interpret distance, use properties, solve absolute-value equations and inequalities; two independent questions. | `working-drafts/prelim-03-absolute-value.md` |
| **P-D. Polynomial/rational inequalities** | 13–18, and exercises 19–20 for practice coverage | Make a sign chart, handle zeros and excluded denominators, combine conditions; two independent questions. | `working-drafts/prelim-04-polynomial-rational-inequalities.md` |

**Coverage:** the source's numbered preliminary pages 1–18 contain the instructional narrative and solved examples; pages 19–20 are the exercise bank. The original independent questions in our drafts are **authored instructional material**, not copies of those exercise pages. Proposed lesson split is provisional pending review of learner cognitive load.

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
- Four **complete** Preliminaries continuous spoken drafts and five previously authored Chapter 1 drafts are in `working-drafts/`. Each contains its own independent attempt prompts and post-attempt feedback.
- Stage 01 is **not** a scientific or teaching critique. Stage 02 after a human `next` will critique and rewrite the combined sequence (P-A–P-D, A–E), without prematurely freezing boundaries or creating scenes.
- **No stable lesson IDs/order have been issued.**
