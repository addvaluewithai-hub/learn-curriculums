# Mathematics I — Engineering Year One | خريطة المنهج

**Editorial checkpoint:** 2026-10-10. **Active Block B02 — Stage 04 scene/script authoring COMPLETE.** Eight issued B02 lesson IDs unchanged; **106 canonical scene JSONs** (80 teaching and 26 independent questions), **26 separately gated explanatory feedback** — **132 speech clips**. B01 remains Stage 04 with deferred voice. **No B02 audio/timed media, real playback, professor/student approval, platform publication or merge. STOP; next = B02 Stage 05 pilot PREPARATION ONLY; next block = B03 Stage 01 after source/inspection check.**

## Audience, source and limits

Egyptian Arabic spoken explanations introduce and reuse English engineering mathematics terms; exam questions/model answers in English, with Arabic comprehension support and explanation. First-year engineering students, institutional syllabus not independently verified. Basic arithmetic, real intervals, polynomial factoring, Cartesian coordinates and some trig familiarity are assumed or bridged.

Original `abd-el-salam-math-i-scan`: *Mathematics I (Calculus-Differentiation) For Engineering*, Associate Professor Dr. Mohamed A. Abd El Salam. **43 scanned PDF pages**: cover/contents on PDF pp. 1–3; printed book pp. **1–80** on PDF pp. 4–43. Only table of contents is visible for later chapters. Exact SHA-256 is stored in `references/SOURCE_MANIFEST.md`, confirmed again 2026-10-10. User deferred durable private storage; book scans are **not** public GitHub assets and future-agent retrieval unverified. Index-only topics are plans, not teaching evidence. `references/SOURCE_COVERAGE.md` gives actual inspected/available details.

## Whole-course provisional production-Block roadmap

A Block is a bounded workflow unit, **not** a student lesson or stable lesson ID.

| Block | Printed book pages | Body availability and learning dependency | Production checkpoint |
|---|---|---|---|
| **B01 — Preliminaries** | **1–20** | Actual source body; real numbers, sets, intervals, inequalities, absolute value, polynomial/rational sign analysis; source **Exercises (1)** on pp. 19–20 | **INACTIVE; Stage 04 canonical authoring**: 5 issued stable student lesson IDs, 72 scenes, 15 assessment/feedback pairs, prior script validation. Audio/academic release **not approved** |
| **B02 — Functions, limits, continuity** | **21–53** | Actual source body; functions/graphs, families, increasing/decreasing, approaching a limit, limit evaluation and continuity; **Exercises (2)** on pp. 51–53 | **ACTIVE; Stage 04 COMPLETE**: 8 issued stable IDs, **106 scene JSONs**, 26 written questions + 26 separate feedback (132 clips), lesson-specific two-ratio boards; no audio or real lesson preview |
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

## B02 — issued IDs, Stage 04 canonical scenes (8 student lessons)

**Confirmed editorial decision: five provisional Stage 02 connected drafts A–E became eight coherent student lesson manuscripts**. Kept **A** and **E** (internal learning parts); split **B** into algebraic families vs trig/exp/log, **C** into monotonicity vs nearby/one-sided limit meaning, and **D** into algebraic vs radian trigonometric limit computation. These choices reflect distinct prerequisite concepts and independent practice, not strict textbook headings, transcript cutting or lesson duration quotas.

**All eight student IDs are now issued/stable and ordered 1–8 within B02.** They are different from B01's five earlier issued IDs. **Canonical spoken words NOW live in `lessons/<id>/scenes/Sxx.json` narration and separate question feedback**; each `lessons/<id>/lesson.json` fixes order/objectives. The previous Stage 03 completed manuscripts at `blocks/B02/final-scripts/<id>.md` and prior working drafts remain **archival comparison only**, not a second independently edited final script. Independent 16:9 and 9:16 storyboards and bespoke React modules now live under each issued lesson folder. No audio, word-onset timing or actual lesson SDK/player sign-off yet.

| B02 order | Issued stable lesson ID / source-grounded student topic | Printed book pages; photographed PDF image pages | Independent exam questions (post-attempt English model & Egyptian-Arabic reasoned feedback) |
|---:|---|---|---|
| **1** | `em1-functions-domain-range` — function uniqueness, domain, range, co-domain and vertical-line test | **21–25**; **14–16** | **A1–A4 (4)** |
| **2** | `em1-functions-algebraic-graphs` — linear/power/polynomial/rational forms, denominator restrictions, graph translations/asymptotes | **25–30**; **16–19** | **B1, B3, B6 (3)** |
| **3** | `em1-functions-trig-exp-log` — periodicity, tan-domain exclusions, exponentials and positive-log arguments | **30–35**; **18–21** | **B2, B4, B5 (3)** |
| **4** | `em1-functions-monotonicity` — increasing/decreasing on valid intervals | **35–37**; **21–22** | **C1, C5, C6 (3)** |
| **5** | `em1-limits-concept-one-sided` — neighborhood limits, left/right limits and missing or assigned point values | **37–40**; **22–23** | **C2, C3, C4 (3)** |
| **6** | `em1-limits-algebraic-methods` — conditional laws, factoring, conjugates, one-sided divergent signs | **39–45**; **23–26** | **D1, D3, D4 (3)** |
| **7** | `em1-limits-trigonometric` — radians, basic sine and tangent ratio limits | **44–46**; **25–27** | **D2, D5, D6 (3)** |
| **8** | `em1-functions-continuity` — interior-point/endpoint conditions, removable holes, jumps, piecewise matching, corners | **47–50**; **27–28**; book **Exercise (2) pp. 51–53**, PDF **29–30 left** | **E1–E4 (4)** |

**Assessment ledger:** **26 independent English exam questions with Arabic meaning** and **26 distinct English model answer + Egyptian Arabic explanatory feedback**; 21 existing Stage 02 question IDs remain traceable and five new questions are **B6, C5, C6, D5, D6**. These are original authored examples, **not transcribed book exercises**. Editorial complete scripts have openings, connected prerequisite teaching, independent learner attempts and recaps; the three splits are **full rewritten lessons**, not mechanically excerpted old narration.

**Source overlap is deliberate.** Photographed printed pp. 30, 35–40 and 44–45 contain neighboring ideas; lesson boundaries are pedagogical, and no false exclusive page breaks are claimed. Printed pp. 51–53 belong to Exercise (2), not a new continuity section. **Book printed p. 34** appears to reverse domain/range for real exponentials, inconsistent with its graph; lesson 3 uses independently verified mathematics and records the source disagreement, pending faculty review. Printed p. 42 quotient-zero shorthand likewise does not justify real division by zero or ignoring sided signs.

Detailed **keep/split mapping, 26 assessment-to-source mappings, prerequisite check, AI-only re-review and unresolved humans checks:** `blocks/B02/reviews/STAGE_03_BOUNDARY_DECISION.md`; previous critique: `blocks/B02/reviews/STAGE_02_CRITIQUE.md`; authoritative B02 checkpoint: `blocks/B02/STATUS.md`. No late chapter content beyond printed p. 80 was invented.

## Cross-Block prerequisites, evidence and human stop

**Student dependency order:** B01 real number/interval/rational restriction fluency → B02 lesson 1 mapping and domain/range → lesson 2 algebraic graph families → lesson 3 trig/radian/exp/log families → lesson 4 increasing/decreasing intervals → lesson 5 nearby and sided limits → lesson 6 algebraic methods → lesson 7 radians/trig methods → lesson 8 continuity → later B03 differentiation. Essential brief bridges remain Cartesian axes and radians; avoid assuming novices already know every trig identity.

**Actually authored in Stage 04:** eight finalized B02 lesson packages, **80 teaching scene narrations plus 26 independently attempted English/Arabic question scenes (106 scenes total), with 26 distinct withheld feedback clips (132 speech clips total)**, original 21 question IDs plus five transfers, complete verbal phrase/occurrence anchors, source locators, taughtIn/assessedIn maps and bespoke lesson-owned React/Remotion source. **B02 local order stays 1–8**, while global `lesson.json.order` is **6–13** so it cannot collide with B01's unchanged 1–5. Detailed evidence: `blocks/B02/reviews/STAGE_04_SCENES.md`. Specialist source/scientific review, novice trial, bilingual voice/pronunciation, timed alignment, actually compiled/rendered real lessons and runtime playback remain **untested**. Passing repository script-stage checks do **not** approve publication.

**Human STOP after Stage 04:** A later bare **`next`** authorizes **B02 Stage 05 optional representative bilingual/formula audio-pilot preparation, dry-run only**; paid TTS dispatch separately requires explicit permission. Distinct **`next block`** may activate **B03 Stage 01** after B02 human scene inspection and actual B03 source re-access. B02 voice/human review can remain deferred, not silently approved. No automatic merge/public source upload/student publication. See `STATUS.md` and `blocks/B02/STATUS.md`.
