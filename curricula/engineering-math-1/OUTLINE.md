# Mathematics I — Engineering Year One | خريطة المنهج

**Editorial checkpoint:** 2026-10-10. **Active Block B02 — Stage 02 completed.** Last completed human-authorized gate: **B02 critique and connected full-draft rewrite**, with **21 independent attempts and 21 feedback explanations**, no B02 final lesson IDs/scenes. B01 remains Stage 04 authored with audio and all human academic/student approval deferred. **STOP; new human `next` → B02 Stage 03 only.**

## Audience, source and limits

Egyptian Arabic spoken explanations introduce and reuse English engineering mathematics terms; exam questions/model answers in English, with Arabic comprehension support and explanation. First-year engineering students, institutional syllabus not independently verified. Basic arithmetic, real intervals, polynomial factoring, Cartesian coordinates and some trig familiarity are assumed or bridged.

Original `abd-el-salam-math-i-scan`: *Mathematics I (Calculus-Differentiation) For Engineering*, Associate Professor Dr. Mohamed A. Abd El Salam. **43 scanned PDF pages**: cover/contents on PDF pp. 1–3; printed book pp. **1–80** on PDF pp. 4–43. Only table of contents is visible for later chapters. Exact SHA-256 is stored in `references/SOURCE_MANIFEST.md`, confirmed again 2026-10-10. User deferred durable private storage; book scans are **not** public GitHub assets and future-agent retrieval unverified. Index-only topics are plans, not teaching evidence. `references/SOURCE_COVERAGE.md` gives actual inspected/available details.

## Whole-course provisional production-Block roadmap

A Block is a bounded workflow unit, **not** a student lesson or stable lesson ID.

| Block | Printed book pages | Body availability and learning dependency | Production checkpoint |
|---|---|---|---|
| **B01 — Preliminaries** | **1–20** | Actual source body; real numbers, sets, intervals, inequalities, absolute value, polynomial/rational sign analysis; source **Exercises (1)** on pp. 19–20 | **INACTIVE; Stage 04 canonical authoring**: 5 issued stable student lesson IDs, 72 scenes, 15 assessment/feedback pairs, prior script validation. Audio/academic release **not approved** |
| **B02 — Functions, limits, continuity** | **21–53** | Actual source body; functions/graphs, families, increasing/decreasing, approaching a limit, limit evaluation and continuity; **Exercises (2)** on pp. 51–53 | **ACTIVE; Stage 02 critique/rewrite COMPLETE**, five provisional working scripts, **21 Q/21 separate feedback**; boundaries/IDs/scenes not issued |
| **B03 — Differentiation** | **54–80** | Actual body supplied; introductory derivatives/rules, chain rule, trig/implicit/parametric differentiation and exercises; requires B02 concepts | Not drafted in active Block workflow |
| **B04 — Inverse, exp/log related topics** | **81–143** (inferred) | **Contents headings only; actual body missing** | Blocked on source |
| **B05 — Hyperbolic functions** | **144–150** (inferred) | **Contents headings only** | Blocked |
| **B06 — Maclaurin and applications** | **151–174** (inferred) | **Contents headings only** | Blocked |
| **B07 — Partial derivatives** | **175–181** (inferred) | **Contents headings only** | Blocked |
| Closing matter | Summary from **182**, references from **186** | Contents only, no inspectable body | Not a teaching Block yet |

## B01 — fixed student lesson boundaries and Stage 04 spoken canon

These five IDs/orders are **issued** and must not be silently changed. Canonical B01 speech and assessment feedback now live in `lessons/<id>/scenes/Sxx.json`, with ordered identity/objective maps in `lessons/<id>/lesson.json`. The Stage 03 connected manuscripts in `blocks/B01/final-scripts/` are historical comparison, not independently edited running scripts.

| B01 order | Stable student lesson ID | Book printed locators | Core learning |
|---|---|---|---|
| 1 | `em1-prelim-real-sets` | **1–5** | Real-number classifications, order and set operations |
| 2 | `em1-prelim-intervals-linear` | **5–8** | Intervals, endpoint/union notation, linear inequalities |
| 3 | `em1-prelim-absolute-value` | **9–12** | Distance interpretation, absolute-value equations and inequalities |
| 4 | `em1-prelim-polynomial-sign` | **13–18** | Quadratic/polynomial sign chart, repeated roots |
| 5 | `em1-prelim-rational-sign` | **13–18**, practice bank **19–20** | Rational denominator exclusion, cancellation and intersections |

Why the last two overlap printed pp. 13–18: the photographic source interweaves polynomial and rational reasoning. **The B01 4→5 split is a teaching decision, not a fabricated exact textbook page break.** Decisions and objective assessment maps: `blocks/B01/reviews/STAGE_03_BOUNDARY_DECISION.md`; scene evidence: `blocks/B01/reviews/STAGE_04_SCENES.md`; state: `blocks/B01/STATUS.md`. B01 visual source supports draft 16:9 and 9:16 layouts but no real timed lesson or human acceptance has occurred.

## B02 — revised Stage 02 working drafts, PROVISIONAL A–E only

**Active editorial masters** live in `blocks/B02/working-drafts/`; they are still **complete continuous teaching texts**, not runtime scenes. Prior joint-curriculum five `working-drafts/*.md` and `reviews/STAGE_02_CRITIQUE.md` remain **historical and unmodified**. The current independent B02 Stage 02 critique, true passage-level fixes and new assessment map are in **`blocks/B02/reviews/STAGE_02_CRITIQUE.md`**.

| Editorial cluster, NOT a stable ID | Source printed pp. | Teaching objective and independent checks (21 total) | Stage 03 boundary *candidate only* |
|---|---|---|---|
| **A: Functions/domain/range** (`01-functions.md`) | **21–25** | Function uniqueness, domain/range/co-domain, graph vertical-line test, finite domain → achieved range; **A1–A4 (4)** | **Keep**, short connected internal parts |
| **B: Function families** (`02-function-families.md`) | **25–35** | Algebraic/trig/exp/log family graphs, exclusions, transformations, exponential range and tangent input domain; **B1–B5 (5)** | **Consider split** algebraic vs trig/exp/log; no final decision |
| **C: Monotonicity and meaning of limits** (`03-monotonicity-limits.md`) | **35–40** | Increasing/decreasing over intervals, one-/two-sided nearby limits vs assigned value; **C1–C4 (4)** | **Consider split** graph monotonicity vs limit concept |
| **D: Calculating limits** (`04-calculating-limits.md`) | **39–46** | Conditional limit laws, factoring, conjugates, directional divergence, radian-based sine/tangent limits; **D1–D4 (4)** | **Consider split** algebraic and trigonometric methods |
| **E: Continuity** (`05-continuity.md`) | **47–50**, exercise bank **51–53** | Three pointwise conditions, holes vs jumps, piecewise matching, endpoint/corner continuity; **E1–E4 (4)** | **Keep**, connected parts |

These are **suggestions**, not stable student lessons. In Stage 03, any split must produce independently coherent **new full scripts** (opening, source/prereq bridge, new worked examples, independent questions, feedback and recap). Splitting the original Markdown at headings is not enough. Boundaries should follow novice comprehension and workload rather than printed section labels.

**Source discrepancy:** book printed **p. 34 / PDF p. 20 right** visibly prints exponential domain/range opposite the accompanying graph and independently checked real exponential facts. The B02 B manuscript documents and corrects the mathematics *as independently authored reasoning*, not as a silent verbatim transcription of the book. Faculty review remains required. PDF p. 24 (printed p. 42) quotient-limit shorthand also needs careful one-sided/domain interpretation; infinity is not a real value assigned to a zero denominator. B02 `reviews/STAGE_01_SOURCE_REOPEN.md` maps photographed evidence.

## Cross-Block prerequisites, evidence and human stop

**Dependency flow:** B01 number/set/interval/denominator fluency → B02 A function mapping/domain/range → B family graphs → C monotonicity/limits → D limit methods → E continuity → future B03 derivative notion. Brief bridges required for Cartesian graphs, trigonometry and radians; do not assume novice mastery. Formal epsilon–delta proofs, L'Hôpital and advanced differentiation remain later topics.

**Actual B02 Stage 02 checks:** **5/5** complete revised scripts structurally reviewed; **21/21** question/feedback pairs and English/Arabic support checked; **30/30** selected algebraic, limit and boundary numerical checks passed. These checks **are not** lecturer approval or a learner trial. No B02 stable IDs, lesson JSON, scene JSON, word timing, TTS or runtime approval. B01 audio remains deferred; nothing merged to `main`.

**STOP — human gate:** later **`next` authorizes B02 Stage 03 ONLY**, to decide and fully rewrite final standalone lessons and issue IDs/orders. No B03 move, scenes, paid audio or publication without separate instruction. Per-Block authoritative state: `blocks/B02/STATUS.md`; whole-course active gate: `STATUS.md`.
