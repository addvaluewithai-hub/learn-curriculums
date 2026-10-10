# B01 — Stage 03 lesson boundary decisions and script freeze (editorial)

**Date:** 2026-10-10 | **Audience:** طلبة سنة أولى هندسة. **Source:** `chemistry-prep-sadik-scan-20261009` (20-page scan, 5,909,225 bytes, SHA-256 `c16cf18739edc03529c002bd921e9772917c42049932fa34cb6501fd10b9367c`). Source PDF pp5–10 opened again; body inspected through printed pp17. Source title stays *Chemistry for Preparatory-Engineering Students* and is not retitled in citations.

> **Scope gate:** This is **Stage 03 only**: resolve the candidate split, issue stable IDs/order, complete fresh coherent *spoken editorial scripts*, audit boundaries. Not Stage 04 scene authoring, audio, sound approval or publishing. Stage 02 draft revisions remain as Git history/editing evidence, while `final-scripts/*.md` become the Stage 03 editorial words. In Stage 04 transform these to canonical `scenes/*.json` and do not keep a second independently edited master script.

## Decision: exactly 3 lessons for B01 (IDs issued)

| Order / stable ID | Stage 02 possibility | Stage 03 decision and reason | Short internal flow | Editor script |
|---|---|---|---|---|
| 1 `chem1-states-phase-changes` | Split states versus six phase changes OR keep with short parts | **Keep with internal parts**. Both follow everyday material properties and prepare the sample/volume concept; independent checkpoint separates shape/volume from direction vocabulary. Splitting would add another opening/recap with little gained dependency separation. | properties → Q01/F01 → direction changes → Q02/F02 | `final-scripts/chem1-states-phase-changes.md` |
| 2 `chem1-boyle-law` | Keep or chunk graph/equation | **Keep one lesson**. A single causal goal links compressible sample→fixed T and n→inverse P,V→piston/graph→worked numbers→check conditions. Q01 numerical and Q02 validity verify two skills without an extra full lesson. | conditions → graph/equation → worked examples → Q01/F01 → Q02/F02 | `final-scripts/chem1-boyle-law.md` |
| 3 `chem1-charles-law` | Split off Kelvin/calc or internal chunks due to novelty | **Keep one lesson with 3 internal parts**, not split into three lessons. Kelvin conversion is an essential prerequisite **within** the same V,T dependency; Q01/F01 consolidate before rearranging to unknown T, Q03/F03 tests law choice. Separating Kelvin from Charles would interrupt the conceptual bridge. | direct V–T → Kelvin/CO₂→ Q01/F01 → solve T → Q02/F02 → Q03/F03 | `final-scripts/chem1-charles-law.md` |

The above are stable IDs, not provisional working labels. Their numbering/order is independent of the source chapter subsection numbering (the source TOC and body disagree). The **entire-course Block roadmap remains provisional** beyond B01; do not infer stable IDs for B02 onward.

## Student prerequisites and dependency handoff

- Everyday water/air/container experience: bridged directly in L01. Formal reading of source table pp8–9 is not assumed.
- Distinguishing shape from volume and gas compressibility are required before the piston model of L02.
- Simple fractions, ratios, inverse versus direct proportionality, and interpreting graph axes: explained before the Boyle/Charles algebra; not assumed mastered.
- Celsius familiarity: bridged to Kelvin (`T(K) = t(°C)+273.15`) before dividing temperatures in L03.
- B02 starts where L03 closes: fixed-volume pressure–temperature Gay-Lussac, then combined gas, Avogadro and Ideal Gas. None taught prematurely within B01.

## Objective-to-teaching-to-assessment to source traceability

| Issued lesson / goal | Taught in Stage 03 script | Independent attempt (after teaching) | Feedback | Source: PDF / printed |
|---|---|---|---|---|
| L01 O1 distinguish properties | Opening: Shape/Volume/Compressibility | Q01 (new beaker) | F01 | PDF6 / p8 |
| L01 O2 classify direct transitions | Continue: six phase directions | Q02 (vapor→frost) | F02 | PDF6 / p9 |
| L02 O1 inverse relation, calculation and units | Concept, both graphs and worked Boyle | Q01 (Sheet1 #5 adapted) | F01 | PDF7–8/pp10–12; PDF10/p17 |
| L02 O2 test law conditions | Opening fixed T,n; closing and law caveat | Q02 (heated compression) | F02 | PDF7/p10 plus **authored** case |
| L03 O1 V–T direct proportionality, Kelvin and find V | Parts 1/2, piston and worked CO₂ | Q01 (Sheet1 #7 adapted) | F01 | PDF8–9/pp13–15; PDF10/p17 |
| L03 O2 rearrange/find Celsius T | Part 3 explicit `T₂=T₁V₂/V₁` | Q02 (Sheet1 #8 adapted) | F02 | PDF10/p17 |
| L03 O3 validity of constant P | Opening/ending conditions; comparison to Boyle | Q03 (rigid container) | F03 | PDF8/p13 plus **authored** case |

**All feedback is explicitly post-attempt and separate from the question script.** Intro/bridges/recaps for each resulting lesson were authored as complete connected speech, not cut mechanically from Stage 02 text. Parenthetical/editorial citations stay outside audio.

## Editorial re-critique of settled boundaries

1. **L01 integrity:** new opening explicitly introduces first-year engineering and connects liquid shape/volume to the need for P,V in gas laws; Q01 tests an unfamiliar wider-beaker situation, Q02 a frost deposition scenario. **Limitation:** one scenario does not prove mastery of all six change labels; a future academic reviewer can request a separate six-arrow diagnostic without treating it as an issued additional lesson.
2. **L02 integrity:** starts from L01 compressibility, bridges the P symbol, demonstrates simple doubling/halving before equation, explains V vs P and V vs 1/P, answers source worked examples, tests numerical unknown pressure and law validity. **Limit:** gas pressure should be treated as absolute when using ratios; full absolute-versus-gauge instruction is beyond the cited page level and requires a separate academic check.
3. **L03 integrity:** B01's most cognitively demanding lesson retained 3 internal parts with two calculation checkpoints and one condition checkpoint, distinct feedback and final B02 bridge. **Limit:** test with a learner and actual read-aloud before deciding whether to visually pause between parts; no fixed runtime minutes or artificial word quota imposed.
4. **Coverage and adjacency:** printed pp8–15 fully represented at high level, and selected Sheet1 p17 problems Q5/7/8 used as **adaptations**, not verbatim quotes; problems from sheet testing P–T deferred to B02. Other unrelated chapter objectives and TOC-only future source pages are not claimed as covered by B01.
5. **No answer leakage:** Q01/Q02/Q03 question segments never contain calculated final answers; independent feedback segments follow the attempt marker. Worked book examples appear **before** independent tests with different numbers or conditions.
6. **Language/speech:** English terms and formulas taught in Egyptian Arabic context; pronounce `P₁,V₂,T₂`, decimals, units and technical terms only after human read-aloud review. Markdown math symbols and stage directions aren't TTS text. No listening approval claimed.
7. **Scientific source mismatches remain flagged:** printed p9 Condensation row `Liquid→Gas` is incorrect; correct Gas→Liquid used in text and preserved as **nonspoken editorial discrepancy**. Printed p12 Boyle 12×1.2/2.4 gives 6 L, not printed 0.6 L; shown correctly, discrepancy documented. Sheet1 p17 Q5/7/8 omit explicit constant-condition statements: teaching versions add them with clear *adapted* provenance.
8. **Significant digits and limitations:** CO₂ printed p15 uses 23.16 mL; L03 says exactly that, additionally distinguishes 23.2 mL at 3 significant figures. Added real-gas/zero-absolute modeling caveat and pressure definition require human scientific verification.
9. **Potential rework:** if independent human review rejects a conceptual claim or decides to split L03, log an explicit before/after ID/order mapping; don't silently recycle the stable lesson ID, create duplicate scripts or invalidate evidence without a new revision.

## Stage 03 freeze / next step

- **Issued:** `chem1-states-phase-changes` order 1; `chem1-boyle-law` order 2; `chem1-charles-law` order 3.
- **No `lesson.json`, `scenes/`, `review.json` or output media created.** Course `OUTLINE.md` is the B01 identity/coverage source of truth; `final-scripts` are editorial wording until Stage 04. Draft history preserved for audit.
- **Human scientific/teaching approval still untested.** No claim of certified accuracy, publication, preview playback, timed assets or rights to redistribute the scan.
- **Next human `next` -> Stage 04 only:** migrate scripts to lesson/scene canonical narration, semantic visual units, independent questions/feedback, separate landscape/portrait storyboards, then run script/quality checks and STOP. No paid audio dispatch.
