# Physics I — Mechanics and Waves | Master outline

**Audience:** طلاب سنة أولى هندسة؛ مقرر Physics I. **Language:** شرح مصري، English technical names + English exam questions مع شرح عربي. **Planning date:** 2026-10-10.
**Status:** Stage 03 confirmed **B01 only** (four issued lesson IDs + complete editorial scripts). Other blocks are still provisional. Stage 04 scene production, sound, timings and student publication are **not** complete.

## What is actually in the supplied scanned sources
- **S01 / phys1-main-scan:** PDF 19 pages. Cover pp.1–2; contents pp.3–4; textbook printed pp.121–133 in PDF pp.5–11 (Solid and Elasticity); printed pp.134–149 in PDF pp.12–19 (Sound Waves).
- **S02 / phys1-elasticity-closeup:** PDF p.1 repeats and clarifies textbook printed pp.124–125 only. No new chapter body.
- **Missing body:** chapters 1–7 and Fluid Mechanics/Fluid Dynamics. The table of contents alone cannot ground detailed teaching; some “Error! Bookmark not defined.” entries make its page links unreliable.
- Original scans remain off public GitHub. Sharing rights and Drive security need resolution; do not put the original scans or publicly writable source URLs in this repo.

## Book order versus authoring order — whole-course provisional roadmap

| Source route | Book topic | Coverage | Authoring Block |
|---|---|---|---|
| R01 | Chapter 1: Physics and Measurements | contents-only | B03 deferred |
| R02 | Chapter 2: Vector and Scalar | contents-only | B03 deferred |
| R03 | Chapter 3: Motion in One Dimension | contents-only | B03 deferred |
| R04 | Chapter 4: Motion in Two Dimensions | contents-only | B04 deferred |
| R05 | Chapter 5: The Laws of Motion | contents-only | B04 deferred |
| R06 | Chapter 6: Energy | contents-only | B05 deferred |
| R07 | Chapter 7: Linear Momentum and Collision | contents-only | B05 deferred |
| **R08** | Chapter 8: Solids and Elasticity | **body available: printed pp.121–133** | **B01 Stage 03 complete** |
| R09 | Chapter 9: Sound Waves and Doppler Effect | body available: printed pp.134–149 | B02 planned only |
| R10 | Fluid Mechanics / Fluid Dynamics (manometer, Pascal, Archimedes etc. in contents) | contents-only, unverified book page numbering | B06 deferred |

**Course learner order:** source R01→R10 pending supply/academic review. **Production starts B01** solely because physical content is available. Numeric lesson order **801–804** reserves positions for chapter 8 so chapters 1–7 can later receive lower order values without renumbering these issued IDs. This is an authoring convention, not student release order confirmation.

## B01 — final Stage 03 lesson map: issued stable IDs and order

| Order | Stable lesson ID | Arabic title / English title | Source locators | Preceding learner knowledge |
|---|---|---|---|---|
| **801** | **phys1-solid-structure-stress-strain** | بنية الصلب والتشوه والإجهاد والانفعال / Solids, Deformation, Stress and Strain | S01 PDF pp.5–8; printed **121–126**; S02 PDF p.1 printed **124–125** | ratios, Newton, area, SI conversions (bridged) |
| **802** | **phys1-young-axial-stiffness** | معامل يونج والصلابة المحورية / Young's Modulus and Axial Stiffness | S01 PDF p.8 printed **126–127**; S02 PDF p.1 printed **125** | lesson 801: Stress, Strain and signs |
| **803** | **phys1-shear-deformation** | تشوه القص ومعامل القص / Shear Deformation and Shear Modulus | S01 PDF p.7 printed **125**, p.9 printed **128**; exercises pp.130–133 consulted as types only | lesson 801; geometry and area, optional 802 |
| **804** | **phys1-bulk-compression** | الانضغاط الحجمي ومعامل الحجم / Bulk Modulus and Volumetric Strain | S01 PDF p.7 printed **125**, p.9 printed **129**; exercise types pp.130–133 | lesson 801 + comparison of Shear in 803; scientific notation and volume units |

**Scope note:** source pages may overlap for a definition/reference; not duplicated independently taught lessons. pp.130–133 in the scan provide exercise *types* but **blurred numerical statements are not treated as solved textbook exercises**. Signed Bulk equation and model caveats are labeled **authored explanations** in scripts.

### Objective → teaching → independent assessment coverage

| ID | Objective | Where taught (editorial script) | Independent question before feedback |
|---|---|---|---|
| 801-O1 | Crystalline vs amorphous with correct structural meaning | L801: solids/particles/structures | L801 Attempt 01, particle patterns |
| 801-O2 | Elastic recovery vs permanent plastic change; limits of stress–strain graph and strength claims | L801: deformation and graph | L801 Attempt 01, recovery vs failure evidence |
| 801-O3 | Compute average normal stress and axial engineering strain correctly | L801: SI example and definitions | L801 Attempt 02, new uniform rod |
| 802-O1 | Use Young's modulus and axial extension in small linear strain | L802: axial assumptions, formula and example | L802 Attempt 01, fresh numerical case |
| 802-O2 | Explain Y material property vs k element stiffness | L802: Hooke/axial stiffness | L802 Attempts 01–02 |
| 802-O3 | Interpret geometry and convert mm, mm² using SI | L802: examples and derivation | L802 Attempt 02, two different lengths |
| 803-O1 | Distinguish tangent force/simple shear from axial loading | L803: opening and force direction | L803 Attempt 02, area-effect reasoning |
| 803-O2 | Describe shear τ, γ and simple-shear geometry | L803: h, Δx, small angle | L803 Attempt 01 plus Attempt 02 |
| 803-O3 | Use S (G) with units for simple linear shear | L803: derivation and guide | L803 Attempt 01 |
| 804-O1 | Distinguish uniform pressure/volume change from axial or shear | L804: opening and comparison | L804 Attempt 02, three cases |
| 804-O2 | Explain signed pressure and ΔV/V0 and positive B | L804: sign convention and example | L804 Attempt 01 |
| 804-O3 | Compute signed volume change/magnitude and units | L804: worked example | L804 Attempt 01 |

**Assessment labels are editorial** (Attempt 01/02 within each script), **not JSON scene or question IDs**. Stage 04 issues question IDs and scene IDs while maintaining objectives and teaching boundaries.

## Stage 03 final editorial scripts — single canonical editorial version per lesson
- [L801 — solids, deformation, stress and strain](blocks/B01/final-scripts/01-phys1-solid-structure-stress-strain.md)
- [L802 — Young's modulus and Hooke](blocks/B01/final-scripts/02-phys1-young-axial-stiffness.md)
- [L803 — Shear](blocks/B01/final-scripts/03-phys1-shear-deformation.md)
- [L804 — Bulk](blocks/B01/final-scripts/04-phys1-bulk-compression.md)

Stage 01–02 connected drafts remain under blocks/B01/drafts as **editorial history**, not as competing approved final scripts. When Stage 04 creates scenes, **scene narration and question feedback become the unique operational script**; further continuous copies must be generated from them.

## Confirmed boundary decision and rewrite rationale
- **Prior WORKING-01 → L801, KEEP with internal parts.** A single linked concept journey: particles/structures → recovery/deformation → Stress/Strain; two genuinely distinct independent checks, structure/elastic and numeric axial. The internal boundaries are not separate lessons.
- **Prior WORKING-02 → L802, KEEP.** One causal path from Y to elongation and axial k; new independent area/geometry transfer. Do not cut it just because it has formulas.
- **Prior WORKING-03 → L803 + L804, SPLIT.** Shear load and bulk compression introduce different force directions, distinct strain measures and different independent problem-solving goals. **Both scripts rewritten** with their own engineering question, bridge, guided example, independent attempt(s), feedback and recap; not mechanically cut.
- **Coverage reconciliation:** printed 121–133 covered at topical/exercise-type level; no unseen chapter content invented. Sound Waves is **B02 only**, not pre-taught in this block.
- [Stage 03 decision and re-review evidence](blocks/B01/review/STAGE03_BOUNDARY_DECISION.md). [Stage 02 critique](blocks/B01/review/STAGE02_CRITIQUE.md).

## Authoring gates
**Current:** B01 Stage 03 boundary/editorial scripts complete; academic/learner independent reviews remain pending. **Next on human “كمل/next”:** B01 Stage 04 create lessons/scenes/storyboards and run **actual script validation**, then STOP; **do not synthesize paid TTS** or publish.
