# B01 Stage 03 — confirmed teaching boundaries and re-review (AI editorial, not science sign-off)

**Date:** 2026-10-09  
**Scope:** B01 Preliminaries only, printed pp. **1–20** (43-page scanned-PDF original; B01 PDF image pages **4–13**, pp. 19–20 exercise bank).  
**Source ID:** `abd-el-salam-math-i-scan`; source/version access and preservation: `../../references/SOURCE_MANIFEST.md`, `../../references/SOURCE_COVERAGE.md`. **No new scan storage or publication; user elected to defer permanent PDF retention.**  
**Input:** original four B01 Stage 02 full drafts `../../working-drafts/prelim-01-*.md` to `prelim-04-*.md` and joint critique `../../reviews/STAGE_02_CRITIQUE.md` (rows P-A–P-D). Links are relative to `blocks/B01/`; actual legacy draft paths are listed explicitly in block STATUS.  
**Decision authority:** user said `next` for the currently active B01; Stage 03 editorial work only. Human mathematics/educational approval has **not** occurred.

## Boundary decision — from four candidate drafts to FIVE issued lesson identities

| Historical cluster | Stage 02 concern | Stage 03 decision and reason | Resulting stable identity / B01 order |
|---|---|---|---|
| **P-A** real numbers / sets, printed **1–5** | Distinct terminology for rationality/order versus sets; multiple small objectives but close foundation role. | **KEEP ONE lesson, two connected learning parts.** Number-line/classification first, sets/union/intersection second; use distinct delayed-feedback attempts after their teaching and a final transfer. Splitting would add a context switch before interval notation despite a shared real-number/selection goal. | `em1-prelim-real-sets` / **1** |
| **P-B** intervals / linear inequalities, printed **5–8**, order rules earlier | Risk of conflating OR/AND and negative division, plus endpoint notation. | **KEEP ONE lesson with short checkpoints.** Visual number-line language directly supports solving inequalities; distinct tests assess intervals, negative division and compound bounds. Conditional sign-of-unknown expression is explicitly deferred to sign charts. | `em1-prelim-intervals-linear` / **2** |
| **P-C** absolute value, printed **9–12** | Distance, two-branch equations, inequalities and triangle inequality create sequential conceptual demand. | **KEEP ONE lesson with connected internal parts**, distance → equation → inequality → properties. The distance model provides one causal spine; pauses/three independent checks reduce load without fragmenting that connection. | `em1-prelim-absolute-value` / **3** |
| **P-D**, polynomial half, printed **13–18** (overlapping spread) | Several independent sign rules; repeated root vs ordinary roots. | **SPLIT**: write a full autonomous polynomial sign-chart lesson with worked quadratic, repeated-root misconception, fresh exam problems and a recap that prepares denominator exclusions. Not a mechanical transcript cut. | `em1-prelim-polynomial-sign` / **4** |
| **P-D**, rational/compound half, printed **13–18**, practice **19–20** | Denominator domain restriction adds a new rule; simultaneous conditions add another objective. | **SPLIT**: new full rational and compound lesson with original opening recalling the polynomial sign chart, numerator-vs-denominator zeros, factor cancellation and intersection of conditions; independent questions on each. Full separate recap closes B01 before B02. | `em1-prelim-rational-sign` / **5** |

**Source split caveat:** printed pp. 13–18 were originally treated as one interwoven inequality source cluster; both new lesson scripts cite the entire range. We do **not** claim a precise book page on which polynomial instruction ends and rational instruction begins. Printed pp. 19–20 are the existing exercise bank, not authored source narration or an invented lecture.

## Issued lesson order, source locators, learner outcome and assessment evidence

| Order | Stable ID and canonical Stage 03 continuous script | PDF pages / printed pages | Independent learner outcome | Non-leaking question→feedback pairings |
|---|---|---|---|---|
| 1 | `final-scripts/em1-prelim-real-sets.md` | **4–6 / 1–5** | Classify rational vs irrational; use ordered real line; represent sets, union, intersection, empty set. | RS-Q1 classification; RS-Q2 set operations; RS-Q3 signed order + empty intersection (each its own separate post-attempt feedback) |
| 2 | `final-scripts/em1-prelim-intervals-linear.md` | **6–7 / 5–8** | Read/write bounded/unbounded intervals; use union/intersection for OR/AND; solve and check single/compound linear inequalities, including sign reversal. | IL-Q1 OR→union/endpoints; IL-Q2 negative division; IL-Q3 compound bounds |
| 3 | `final-scripts/em1-prelim-absolute-value.md` | **8–9 / 9–12** | Interpret $\lvert x-a\rvert$ as distance; solve two-branch equation, interval inequality; check the triangle inequality. | AV-Q1 two roots; AV-Q2 bounded inequality; AV-Q3 independent triangle property |
| 4 | `final-scripts/em1-prelim-polynomial-sign.md` | **10–12 / 13–18** | Factored polynomial sign analysis, endpoint inclusion, repeated-root interpretation. | PS-Q1 quadratic ≤ 0; PS-Q2 squared factor and strict >0; PS-Q3 inclusive product sign |
| 5 | `final-scripts/em1-prelim-rational-sign.md` | **10–12, 13 for exercises / 13–20** | Rational sign chart with forbidden denominator; cancellation with persistent exclusion; combine rational and linear restrictions. | RA-Q1 strict rational sign; RA-Q2 cancellation with hole; RA-Q3 rational+linear intersection that genuinely trims the solution |

**Total authored final B01 assessment evidence:** **15** independent English exam questions, **15** separate feedback explanations with Arabic reasoned walkthrough; no assessment depends on the same worked numerical example. Historical Stage 02 working drafts remain **unchanged** in `working-drafts/` for editorial provenance. The five `final-scripts/` files are the **authoritative Stage 03 editorial manuscripts** for B01; Stage 04 will convert them into canonical scene narration/feedback, after which the scene files (not these drafts) become the runtime source of spoken truth.

## Prerequisite/coverage integrity re-review

- **Foundation order:** real number/order/set operations (1) → interval/negative sign reasoning (2) → absolute-value distance and linear bounds (3) → sign of factored products (4) → denominator exclusion and combined conditions (5). Each resulting script states assumed vs taught vs deferred terms at first use and independently assesses its key target.
- **Cross-boundary transitions:** lesson 1 closes by introducing intervals; lesson 2 ends at distance; lesson 3 moves from distance to sign charts; lesson 4 explicitly previews denominator zero restrictions; lesson 5 closes by connecting exclusions to B02 domain of a function.
- **No loss of prior B01 targets:** rationality and sets (P-A); interval endpoints/compound linear inequalities (P-B); distance, equations/inequalities and properties (P-C); polynomial/rational sign, repeated roots, forbidden denominators, cancellation and conjunction (P-D) retained. Source pp. 19–20 remain practice-bank coverage, **not copied**.
- **Distinct scripts rather than chopped narration:** both children of P-D now have complete introductions, explanatory bridges, separate fresh worked examples, independent attempts/post-attempt feedback and recaps.
- **No B02 editorial change:** the five B02 Stage 02 scripts remain preserved and un-issued; no IDs/orders for B02 assigned or conflicts silently created.
- **Answer leakage:** questions and Arabic meaning appear in pre-attempt prompt sections; English model answers and Egyptian-Arabic reasoning occur only in `Post-attempt explanatory feedback` sections. Any eventual visual storyboard must preserve that separation.
- **Math checks to inspect:** negative inequality flip; closure at numerator zero but not denominator; `(x-2)^2` unchanged signs; `(x+1)^2(x-4)>0` only after 4; cancelled factor `x=2` still excluded; RA-Q3 intersection gives `[-2,0)` rather than a redundant constraint. Numerical spot checks and file-shape checks are additional, not proof.

## Unresolved before production
- **Academic review untested:** mathematical lecturer should verify every spoken claim, formal notation and independently authored answer against first-year engineering expectations; scan page formulas remain historically inspected but not certified line by line.
- **Source access future:** original scanned attachment not made permanently retrievable; user postponed storing the PDF; do not claim it is in GitHub or let future block authoring invent unsupplied pages.
- **Human instructional trial untested:** the keep-vs-split decisions are source-informed editorial judgments, not classroom cognitive-load outcomes.
- **Build/quality tooling:** draft scripts are not `lesson.json` scene assets. Stage `script` validator, voice and SDK preview belong to the later authorized Stage 04 or beyond; never claim they ran now.
- **No full student-ready approval, audio paid dispatch, stable B02 IDs, scenes or publication.**

**Human stop:** Stage 03 B01 editorial decision and five complete resulting manuscripts produced. **Await a new explicit `next` for B01 Stage 04 only**, which will create scene/storyboard artifacts and perform script-stage checks; `next block` is available only after Stage 04/human inspection.
