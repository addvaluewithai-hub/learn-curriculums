# Engineering Mechanics – Statics | Curriculum master roadmap

**Whole-course scope:** First-year engineering mechanics — Statics. Egyptian Arabic teaching, English engineering/exam terms and bilingual question/feedback support. This roadmap is **provisional outside B01** and must not be mistaken for finished teaching or access to an entire printed book.
**Revision note:** 2026-10-09 adaptation of the existing Stage 01–03 work to the newer curriculum → Block workflow. We **did not run Stage 00 as a separate historical gate**; this is a retrospective structure/source inventory created with explicit human permission. The three stable B01 lesson IDs and script content are preserved.
**Source:** `statics-scan-2026-10-08` (36-page scanned PDF). Manifest `references/SOURCE_MANIFEST.md` stores the **measured** file hash, current temporary access and unresolved private archival blocker; `references/SOURCE_COVERAGE.md` distinguishes body-inspected/available from contents-only.

## Whole-course Block plan — deliberately conditional

| Block | Working scope, not a lesson | Source status | Prerequisite/dependency | Gate / next step |
|---|---|---|---|---|
| **B01** | Intro: mechanics, quantity/models, Newton laws, gravitation/weight, units | **Body inspected:** Ch.1 printed pp.1–6, scan pp.7–12 | school algebra, units, basic motion | **Active: Stage 03 complete**; three stable lesson IDs listed below; Stage 04 awaits new human `next` |
| **B02** | Vector foundations and planar force resolution — Ch.2 sections 2.1–2.5 | **Body supplied, partial skim only:** printed pp.9–18, scan pp.14–23 | B01: Force as vector, units | Candidate after B01 Stage 04 and human `next block`; must re-open actual pages at Stage 01 |
| **B03** | Unit vectors, coplanar resultants and position vectors — Ch.2 2.6–2.8 plus available exercises | **Body supplied, partial skim only:** printed pp.19–30, scan pp.24–36 | B02: planar vectors/components | Candidate future source Block; review boundary against actual material before authoring |
| **B04** | Three-dimensional forces and later Ch.2 topics (e.g., dot product) | **INDEX ONLY / BODY MISSING:** begins printed p.32 | B02/B03 planar & vector basics | **Blocked** until original chapter pages supplied and inspected |
| **B05** | Equilibrium of Particles (Ch.3) | **INDEX ONLY / BODY MISSING** | vector/resultant reasoning | **Blocked** — title-level plan only |
| **B06** | Moment of a Force and Equivalent Force Systems (Ch.4) | **INDEX ONLY / BODY MISSING** | forces/vector reasoning | **Blocked** — title-level plan only |
| **B07** | Equilibrium of Rigid Body (Ch.5) | **INDEX ONLY / BODY MISSING** | rigid-body idealization, forces and moments | **Blocked** — title-level plan only |
| **B08** | Structure Analysis (Ch.6) | **INDEX ONLY / BODY MISSING** | rigid-body equilibrium and structural models | **Blocked** — title-level plan only |
| **B09** | Friction (Ch.7) | **INDEX ONLY / BODY MISSING** | equilibrium and contact forces | **Blocked** — title-level plan only |

A Block is an **editorial production unit**, not automatically one textbook chapter or student lesson. B02/B03 boundaries reflect available section clusters and are hypotheses until their own Stage 01 source review and subsequent critique. B04–B09 topics come **only from the index**, so no numbered lessons, scripts, questions or source claims were created for them.

## Curriculum-wide dependency and operational rules
- Core trajectory: recognize bodies and forces → understand laws/units → resolve force vectors → analyze equilibrium/force systems → later statics applications *only after actual material is supplied*.
- One curriculum STATUS tracks source/roadmap and the **active Block**; `blocks/B01/STATUS.md` tracks the active Block's actual human gate and outputs. For B02 onward, create block STATUS only on activation (do not preclaim Stage 01).
- B01 remains the selected bounded block for existing content. Stage 01–03 took place historically under the old rules; their genuine recorded editorial results are carried forward, **not replayed** or marked human-academic approved.
- On the **next separate** `next`, only B01 Stage 04 scenes/storyboards are in scope **if source accessibility/rights blockers and required dependencies are appropriately handled**. After Stage 04, `next block` starts B02 Stage 01 without audio; plain `next` means B01 Stage 05 pilot preparation, not paid dispatch.
- No new original PDF committed to public Git, no guessed edition, no invented future source pages and no automatic merge/teacher sign-off/publication.

---

## B01 — finalized Stage 03 editorial lesson map and coverage

**B01 scope:** Chapter 1 only, original printed pp.1–6 (user-uploaded image-only PDF scan pp.7–12).
**Status:** Stage 03 editorial boundary decision, final spoken scripts and **issued stable lesson IDs**. The human authorized this production stage by sending “next”. This is **not scientific/human publication approval**.
**Language:** Egyptian Arabic explanation; essential English exam terminology, English prompts and model answers, natural Arabic support. Headings/directions not spoken.

## Final ordered lessons (identity is not the order)
| Order | Stable lesson ID | Title / English title | Printed chapter/source locators | Final script (single editable continuous editorial source until Stage 04) |
|---|---|---|---|---|
| 1 | `ems-y1-foundations-models` | مدخل الميكانيكا ونماذج الأجسام / Engineering Mechanics and Idealized Models | Ch.1 pp.1–3; scan pp.7–9 | `drafts/01-mechanics-and-models.md` |
| 2 | `ems-y1-newton-gravity` | قوانين نيوتن والجاذبية والوزن / Newton's Laws, Gravitation and Weight | Ch.1 pp.3–5; scan pp.9–11 | `drafts/02-newton-and-weight.md` |
| 3 | `ems-y1-units-conversions` | الوحدات والتحويلات في الاستاتيكا / Systems of Units and Unit Conversions | Ch.1 pp.5–6; scan pp.11–12 | `drafts/03-units-and-conversions.md` |

**Identity rule:** IDs above are newly issued and stable; never change/recycle them without owner coordination. Shared printed page overlap is deliberate at transitions; identical worked explanations are not copied between lessons. The `drafts/` path is historical; these three in-place files are now **Stage 03 final scripts**, not competing source documents. Stage 04 must replace them as canonical script with scene/feedback narration, deriving any review copy from the scenes. **Do not create lesson.json or scene JSON in Stage 03.**

## Audience and prerequisites
- **Assumed from school:** basic arithmetic, substitution, everyday length/time, notion of motion, basic right/left/up/down spatial orientation.
- **L01 bridging concepts:** body versus model; mass versus force; vector has magnitude and direction; contact force versus gravity. No trig/vector addition required.
- **L02 prerequisites:** L01 Force, Mass and Resultant as total effect; short bridge velocity versus acceleration and directional sign for one-axis calculation.
- **L03 prerequisites:** L01 quantities, L02 ΣF = ma and W = mg; small arithmetic conversion and fraction cancellation bridge.
- **Explicitly deferred:** 2D/3D force vector components and vector algebra (Ch.2), Free-Body Diagrams and particle equilibrium (Ch.3), Moments/Couples (Ch.4), rigid-body equilibrium (Ch.5), structural analysis and friction chapters beyond available body text.
- **Nonformal supporting concepts:** Length and Time descriptions support later calculations, but are not falsely declared independently mastered objectives in this block.

## Objective → actual teaching → independent assessment → source map
Objective IDs are **local to each stable lesson ID** (Stage 04 lesson-level `O1` etc.). Q numbers below are editorial checkpoint ordinals, not issued question JSON IDs.

| Stable ID | Objective | Evidence in current complete spoken script | Independent attempt; separate post-attempt feedback | Actual source |
|---|---|---|---|---|
| foundations-models | O1: distinguish equilibrium-focused Statics from accelerated Dynamics | L01 part 1: bridge/box/elevator question | L01 Q1 accelerating elevator | pp.1–2, scan 7–8; Newton bridge printed p.3 |
| foundations-models | O2: describe force as vector; for extended body name missing force-action data | L01 part 2: length/time/mass/force, door example | L01 Q2 30-N door | p.2, scan 8 |
| foundations-models | O3: select and justify Particle/Rigid Body/Concentrated Force by analysis goal | L01 part 3: conditional model selection | L01 Q3 crane sensor, Q4 bracket/bolt | pp.2–3, scan 8–9 |
| newton-gravity | O1: apply Newton I distinction zero resultant ≠ necessarily rest | L02 part 1: resultant, puck and constant velocity | L02 Q1 puck | p.3, scan 9 |
| newton-gravity | O2: calculate acceleration from **net force** for constant mass | L02 part 2: ΣF = ma and worked 4N/2kg | L02 Q2 cart 12N/3kg | p.3, scan 9 |
| newton-gravity | O3: recognize Newton III pair acting on two different bodies | L02 part 3: hand/wall interaction | L02 Q3 runner/ground | p.4, scan 10 |
| newton-gravity | O4: reason about relative gravitational force when distance changes for particle-model fixed masses | L02 part 4: F = Gm₁m₂/r² | L02 Q4 triple distance, result one ninth | p.4, scan 10 |
| newton-gravity | O5: distinguish mass/weight and compute near-Earth W=mg with N | L02 part 5: 3kg worked weight, conditions on g | L02 Q5 5kg weight | pp.4–5, scan 10–11 |
| units-conversions | O1: classify SI/FPS mass and force units | L03 parts 1–2: SI kg/N, FPS slug/lbf | L03 Q2 mass vs force classification | p.5, scan 11 |
| units-conversions | O2: derive SI force unit and reject inconsistent acceleration dimensions | L03 part 1: kg·m/s² = N; worked 2kg×3m/s² | L03 Q1 4kg, 3m/s², wrong seconds exponent | pp.5–6, scan 11–12 |
| units-conversions | O3: convert length and force across SI/FPS with dimensional cancellation | L03 parts 3–4: 5ft and 10lbf worked | L03 Q3 shelf 2.5ft, Q4 cable 8lbf | pp.5–6, scan 11–12 |

Source locators above refer to **printed** pages first, then 1-based PDF scan pages. Parent/source metadata: `references/SOURCE_REVIEW.md`. Later chapters 3–7 are only headings in this upload. Work examples and all 13 independent questions are **authored teaching material**, not textbook exercises.

## Final Stage 03 decisions with learner-centered reasons
1. **L01 keep one coherent lesson with three internal parts.** Starting from a real object/question, the student learns classification, what information Force needs, then when an idealized body/load is reasonable. Independent Q1/Q2 precede idealization Q3/Q4; making every heading a separate lesson would lose the reason for modeling.
2. **L02 keep one linked lesson with five shorter parts/checkpoints.** Newton I prepares the meaning of resultant; Newton II makes it quantitative; Newton III corrects two-body confusions; gravitation explains the source of weight; near-Earth W=mg applies the concept. Each part has a **different transfer attempt** after its explanation, so the student gets consolidation. This is the highest cognitive-load candidate; a real novice/teacher study may later justify a split, but no speculative duration threshold was applied.
3. **L03 keep one lesson with four internal parts.** Units, derived units, system classification, length conversion and force conversion share one invariant: identify the physical quantity and cancel units. Separate questions ensure the parts are not one undifferentiated block. No need to merge the entire units lesson with Newton II, which is already bridged by a reference to ΣF=ma.
4. **Gravitation is explicitly in-scope, not a hand-wavy bridge.** Stage 02 identified missing independent assessment; L02 Q4 now checks the inverse-square dependence under fixed masses. Weight still gets independent L02 Q5.
5. **No rescope omissions or duplicative explanation:** L01 → L02 → L03 is contiguous. Repeated terms (Force, Mass, Resultant, N) appear as short retrieval bridges, not re-teaching of preceding lessons. The source's running numbered sections govern locators, not inconsistent heading/divider indexing.

## Source and integrity limitations
- The upload is a 36-page scanned partial source; Ch.1 text actually available through printed p.6, Ch.2 printed pp.9–30 later, Ch.3–7 headings only.
- Descriptions about nonaccelerating reference frame, exact foot conversion, using lbf for force, and orbital weightlessness are **contextual author clarifications** for specialist verification; don't pretend they are printed textbook quotations.
- The original PDF is not added to this public GitHub repository. Teacher reviewer should inspect original blurry details/section numbering and source reuse permissions.
- Source/science and teaching still **untested by independent human reviewer**. No student work, durations or production audio assessed. No review.json checks marked passed.

**Next human stage (NOT authorized yet):** Stage 04 — create formal lesson.json/scenes/questions/feedback and independent 16:9/9:16 storyboards with script-level validation, then stop before audio.
