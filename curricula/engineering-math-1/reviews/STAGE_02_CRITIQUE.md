# Stage 02 — Evidence-led full-draft teaching critique and rewrite
**Course:** Mathematics I — first-year engineering; draft PR #8
**Editorial iteration:** 2026-10-09, Stage 02 only; **AI-authored critique, not an independent academic or human pass.**
**Source ID:** `abd-el-salam-math-i-scan`. The user-uploaded, image-only scan exposes printed pp. 1–80, preceded by cover/contents (43 PDF pages). Editorial review relates the nine scripts to **printed pp. 1–53** and the PDF-image locators documented in `references/SOURCE_REVIEW.md`. Some equations in the tilted/faint source photos cannot be independently line-by-line transcribed with high confidence. The exercises and worked values in the scripts are **original teaching examples**, not claimed verbatim book questions or answers.

## Method and boundaries
Review each of the **nine complete connected** Stage 01 scripts, separately considering: novice prerequisite gaps; source/condition integrity; conceptual arc; bilingual read-aloud; objective-to-independent-question mapping; answer hiding; misconception handling and likely cognitive load. Apply focused edits to the **entire existing narratives** without making scene cuts. Add truly separate independent prompts and post-attempt feedback where essential objectives lacked evidence. Re-read revised source files and spot-check numerical/sign/limit answers. Do not issue stable lesson IDs or assert acceptance based on these checks.

## Specific findings, source locators, and revisions

| Working label / source pages | Evidence-backed concern in Stage 01 draft | Stage 02 rewrite and rationale | Stage 03 boundary **possibility**, NOT a decision |
|---|---|---|---|
| **P-A: real numbers, sets**; printed **1–5**, PDF **4–6** | Natural-number zero convention was left ambiguous, a novice had no guard for a square root outside the real system, and only two independent checks left ordering/empty intersection untested. | Clarified the intended natural-number convention and contrast between positive nonsquare square roots and `sqrt(-1)` in the real system. Tightened why `sqrt(5)` is irrational; added **Q-P-A3** for order and empty intersection with separate feedback. | Consider short internal sections for numbers/order vs set operations; split only if diagnostics show separate mastery needs. |
| **P-B: intervals and linear inequalities**; **5–8** and earlier order rules, PDF **6–7** | The story taught AND/OR and negative-division flipping but assessed only algebraic inequalities; multiplying by a variable of unknown sign could be misgeneralized. | Added the sign-of-unknown caution, plus **Q-P-B3** requiring translation of an OR condition into a union of open/closed intervals; feedback explicitly contrasts union with impossible intersection. | Likely coherent as one unit with number-line/intersection checkpoints; evaluate under novice testing. |
| **P-C: absolute value**; **9–12**, PDF **8–9** | The positive-distance threshold needed to be stated before generic two-branch rules; triangle inequality was taught but not independently assessed. | Added the nonnegative-value/threshold bridge and equality-vs-inequality explanation; **Q-P-C3** checks `|a+b|` vs `|a|+|b|` with delayed model reasoning. | Internal parts for distance→equations→inequalities/properties may reduce load. |
| **P-D: polynomial/rational inequalities**; **13–18**, exercises **19–20**, PDF **10–13** | A learner might infer that every root flips sign. Also two checks on polynomial and rational signs did not independently assess intersection of conditions. | Explained a squared repeated factor can keep the same sign on both sides; added **Q-P-D3** on simultaneous conditions and intersection, with strict exclusion of a boundary. | Candidate for separate polynomial-sign and rational/compound work, subject to student difficulty. |
| **A: functions, domains and ranges**; **21–25**, PDF **14–16** | Source definition explicitly mentions co-domain as distinct from actual range; novice distinction not taught. Previous point-pair check was not an independent relation-to-vertical-line transfer and had ambiguous point typography. | Explained co-domain vs range without changing objective scope; tightened `f(2)=1` point reasoning; normalized mathematical coordinates; added **Q-A3** on whether a circle relation defines `y` as a function of `x`. | Could stay with short sections for input/output, domain-range and graph validation. |
| **B: function families**; **25–35**, PDF **16–21** | Very wide range of families, with confusing math wrapping and little independent evidence for graph transformation or exponential/trigonometric classification. | Clarified real exponential vs logarithm input/output restrictions; normalized formulas; added **Q-B3** on shifted quadratic vertex and **Q-B4** on sine/exponential family, domain and range. Graph-shift demonstration is independently authored pedagogy, not a claim of a verbatim book exercise. | **High-priority split candidate**: algebraic graphs, then trigonometric/exponential/logarithmic; evaluate whether transformations should be an optional short bridge. |
| **C: monotonicity and limit idea**; **35–40**, PDF **21–23** | Two major conceptual moves share a script, and the initial elementary numerical limit check did not independently test left/right approach or separate point value. | Added a new original open-vs-filled-point narrative bridge; **Q-C3** uses unequal one-sided limits with an arbitrary defined point value. Corrected math prompt/answer notation. | **High-priority split candidate**: increasing/decreasing versus reading limits, but make decision only in Stage 03. |
| **D: evaluating limits**; **39–46**, PDF **23–27** | Factoring, conjugates, unbounded one-sided behavior and radians-based trig rules are distinct skills; previous two independent checks omitted rationalization and directional behavior. Radian precondition needed explicit learner bridge. | Added `pi radians = 180 degrees` reminder; **Q-D3** requires a conjugate with a nontrivial `2x` radicand and **Q-D4** tests opposite unbounded one-sided signs of `1/(x-2)`. All feedback states cancellation is valid **near** an excluded point, not at it. | **High-priority split candidate**: algebraic methods vs trig limits, possibly keep directional limit as a connection to C. |
| **E: continuity**; **47–53**, PDF **28–30 (left side)** | Pen-lifting analogy might appear as a mathematical test; the two-sided three-condition test needed interior-point scope, and assessments lacked a case where no point value could fix the jump. | Clarified interior-point vs endpoint one-sided continuity, stated that the analogy is insufficient without the three conditions, and added **Q-E3** showing no `k` can reconcile unequal side limits. | Likely coherent if organized into tests / hole / jump / piecewise applications; boundary remains provisional. |

## Objective-to-independent-transfer mapping after rewrite
This is a working assessment coverage map, **not** a lesson.json objective/scene binding.

| Draft | Taught targets and distinct independent attempts |
|---|---|
| P-A | rationality Q-P-A1; set membership/union/intersection Q-P-A2; order and empty-set application Q-P-A3 |
| P-B | negative-division inequality Q-P-B1; compound linear bounds Q-P-B2; mixed-endpoint union Q-P-B3 |
| P-C | absolute-value two-branch equation Q-P-C1; enclosed-distance inequality Q-P-C2; triangle inequality Q-P-C3 |
| P-D | polynomial sign regions Q-P-D1; rational denominator exclusion Q-P-D2; compound intersection Q-P-D3 |
| A | radical-denominator domain Q-A1; range + uniqueness Q-A2; independent relation vertical-line test Q-A3 |
| B | polynomial/rational families Q-B1; logarithmic domain Q-B2; graph translation Q-B3; sine/exp family and properties Q-B4 |
| C | increasing/decreasing shift Q-C1; nearby finite limit Q-C2; left/right limits versus point value Q-C3 |
| D | algebraic factoring Q-D1; radians-based trig limit Q-D2; conjugate Q-D3; diverging side limits Q-D4 |
| E | matching piecewise values Q-E1; removable hole with incorrect assigned point Q-E2; irreparable jump Q-E3 |

**Current count:** **29** independent prompts, **29** distinct post-attempt explanatory feedback sections across **9** complete working drafts. No answer is intended in pre-attempt narration or visuals; preliminary visual notes are not final artifacts.

## Answer sanity review — sample concrete checks
- P-A3: `-3 < -sqrt(2) < 0`; disjoint finite sets have empty intersection.
- P-B1: dividing `-3x <= -9` reverses to `x >= 3`; P-B2 yields `[-1,11)`.
- P-C1: `|3x-2| = 7` gives `x = 3` or `-5/3`; P-C3 gives `2 <= 8`.
- P-D1: `(x+4)(x-2) <= 0` gives `[-4,2]`; P-D2 gives `(-infinity,-2) union (3,infinity)`; P-D3 with `x<2` gives `(-infinity,-1] union [1,2)`.
- A1: `1/sqrt(x-3)` needs `x>3`; A3 at `x=0`, the circle has `y=3` and `y=-3`.
- B3 vertex is `(-3,-2)`; B4 positive-base exponential range is `(0,infinity)`.
- C3 one-sided limit values `2` vs `3` mean no two-sided limit, regardless of `p(1)=10`.
- D2 limit `sin(5x)/(2x)` is `5/2` in radians; D3 `(sqrt(2x+9)-3)/x` tends to `1/3`; D4 sides are negative and positive unbounded near `x=2`.
- E1 matching `a=-1`; E2 limit `4` differs from defined value `5`; E3 left/right `2` versus `5` cannot be repaired by `k`.

A separate lightweight JavaScript numerical/boundary spot-check evaluated **21 selected conditions** and passed all 21. Such samples do **not** constitute formal proof of every narrated equation; full manuscript and exercise accuracy still needs the assigned math reviewer.

## Bilingual and narrative pass
- Kept concept-first Egyptian Arabic speech and exam English with Arabic explanation, rather than translating every English phrase mechanically.
- Made English term meanings explicit at first need: Real Number System, Co-domain, Interval, Sign chart, One-sided limit, Radians, Continuity.
- Repaired irregular inline math wrapping in Chapter 1 and English question typography; retained math as written notation and Arabic spoken alternatives in question/support and feedback.
- Added self-contained independent transfer contexts (not repeated with identical coefficients), and separate feedback containing model English answer plus reasons in Egyptian Arabic.
- Kept rough visual suggestions editorial only; no early answer disclosure authorized.

## Unresolved issues and human gates
1. **Academic sign-off: NOT PASSED / untested.** No named mathematics lecturer has reviewed all new examples, spoken phrasing, source interpretation or textbook fidelity. Tilted/faint source formula details should be checked directly in the original PDF by the reviewer.
2. **Teaching and learner trial: untested.** Need first-year student comprehension testing for the dense clusters P-D, B, C and D and more authentic university-style problem sampling.
3. **Source/access and permissions:** the attachment is not redistributed to public GitHub; the complete book is not available beyond printed page 80. The scope here stops at printed page 53.
4. **Stage 03 boundary review: UNDECIDED.** Possible keep/internal-part/split recommendations above are input to Stage 03, **not** an approved restructure. No stable lesson IDs/order, scene/audio/timing assets or publication. The eventual course outline can be revised only after a future explicit user `next`.
5. **No fabricated runtime/voice evidence.** No TTS dispatch, ASR, listen-through, student delivery or preview rendering has occurred at this editorial gate.

**Gate checkpoint:** Stage 02 editorial critique + targeted complete-draft rewrites prepared. **STOP — awaiting human `next` or corrections.** `next` authorizes only Stage 03 lesson-boundary decision and resulting full scripts; no scenes or paid audio.
