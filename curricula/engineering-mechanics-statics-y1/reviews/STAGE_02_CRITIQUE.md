# Stage 02 — Full-draft critique, edits and re-checks

**Scope:** First-year Engineering Mechanics (Statics), Chapter 1 printed pp.1–6, scan pp.7–12. Source is the image-only 36-page PDF supplied in the initiating conversation; binary not stored in this public repository. Stage 01 text remains recoverable from previous Git commits.
**Reviewer status:** AI editorial critique, NOT subject-teacher sign-off, real learner testing or academic/visual/audio approval.

## Passage-by-passage findings and fixes

| ID | Exact Stage 01 issue | Source locator | Stage 02 applied fix | Check |
|---|---|---|---|---|
| A1 | Draft 01 paragraph 2 defined Statics merely as no acceleration and risked confusing rest with absence of forces | Scan p.7, source printed p.1; Newton concepts printed p.3 | Focus on equilibrium and stationary early problems; bridge to constant velocity and Newton 1 | No statement that rest means zero individual forces |
| A2 | Draft 01 box example casually combined support and gravity | Scan pp.8–10, printed pp.2–4 | Differentiate contact support upward and gravitational force downward | Two physical interactions clear; detailed FBD deferred |
| A3 | Draft 01 quantities section described direction without explicitly bridging force as a vector | Scan p.8, printed p.2; Force Vectors chapter listed in scan p.13 | Name magnitude+direction and introduce Vector without doing component calculations | No Chapter 2 algebra taught early |
| A4 | Draft 01 first assessment disclosed dimension-negligibility condition; Rigid Body, Concentrated Force, Statics/Dynamics had no independent checks | Scan pp.7–9, printed pp.1–3 | Replace crane load with sensor/context + condition; add bracket/bolt idealizations and elevator classification | 4 separate English prompts with Arabic support and separated feedback |
| A5 | Draft 01 post-question narration said “ممتاز” without reading student response | Teaching guidance: no false personalized praise | Replace with neutral content-based transition | No assumed correct response |
| B1 | Draft 02 First Law statement was grammatically double-negative (“مفيش عليه محصلة ... غير صفرية”) | Scan p.9, printed p.3 | Say directly that net external force is zero; qualify nonaccelerating reference frame | Zero resultant and zero acceleration differentiated from zero velocity |
| B2 | Draft 02 wrote F=ma with insufficient emphasis on the net force | Scan p.9, printed p.3 | Use ΣF = ma for constant-mass body and explain ΣF with directional sum | Guided 4N/2kg calculation; independent 12N/3kg calculation |
| B3 | Draft 02 jumped from Newton 3 to Weight, omitting book's universal gravitation law | Scan p.10, printed p.4 | Add brief F = Gm1m2/r² meaning and distance dependence, then introduce near-Earth W=mg | Preserves original topic chain without requiring astrophysics calculation |
| B4 | Draft 02 astronaut explanation could imply no gravity in orbit | Scan p.11, printed p.5; contextual science caveat beyond the page | Clarify decrease with distance versus orbital free-fall experience; mark additional explanation as instructor verification item | Does not assert zero gravity in orbit |
| B5 | Draft 02 Q1 and Q2 covered only Newton 1 and weight | Scan pp.9–11, printed pp.3–5 | Add independent second-law cart and third-law runner/ground; retain first-law and weight questions | 4 post-attempt feedback pairs, distinct bodies in Newton 3 |
| C1 | Draft 03 called 1 ft ≈ 0.3048 m rather than an exact definition | Scan pp.11–12, printed pp.5–6 | Treat foot-to-meter as exact and lbf-to-N factor as rounded | Units and conversion arithmetic remain consistent |
| C2 | Draft 03 “lb” might be read as mass or force without context | Scan p.11 FPS force/pound, mass/slug; printed p.5 | Use explicit pound-force (lbf), contrast kilogram mass and slug mass | No kg-to-lbf symbol substitution |
| C3 | Draft 03 unit question copied weight example from previous lesson, creating false sense of transfer | Scan p.12 table, printed p.6 | Replace with trolley force having intentionally wrong time exponent; add cable lbf→N conversion | 3 independent question→attempt→feedback sequences |
| X1 | Some visuals were only named, not motivated by possible novice confusion | Scan pp.7–12 diagrams/tables | Rough beats now point to distinct contact/gravity arrows, force ownership and unit cancellation | No formal scene JSON/visual build at Stage 02 |
| X2 | Risk of giving answers before interaction | Teaching contract | Rechecked English question and Arabic support precede an explicit attempt; model answer kept in separate feedback prose | No early model-answer passage in question block |
| X3 | Novice load: Drafts 01 and 02 teach multiple distinct clusters | Printed Chapter 1 pp.1–5 | Added bridges and assessments without adopting fixed duration or blind split | Boundary alternatives only, NOT finalized |

## Goal to passage to independent checkpoint

| Goal | Taught in | Independent question |
|---|---|---|
| Statics vs Dynamics | Draft 01 introduction | Draft 01 Q3 (accelerating elevator) |
| Describing a force beyond magnitude | Draft 01 quantities and door discussion | Draft 01 Q4 (30 N door force) |
| Particle model choice | Draft 01 idealizations | Draft 01 Q1 (sensor translation) |
| Rigid Body and Concentrated Force conditions | Draft 01 idealizations | Draft 01 Q2 (bracket and bolt) |
| Newton I zero resultant / constant velocity | Draft 02 first law | Draft 02 Q1 (puck) |
| Newton II net force and acceleration | Draft 02 second law | Draft 02 Q2 (cart) |
| Newton III action/reaction on different bodies | Draft 02 third law | Draft 02 Q3 (runner/ground) |
| Weight and mass distinction; W=mg | Draft 02 gravitation and weight | Draft 02 Q4 (5 kg near Earth) |
| SI force dimension | Draft 03 SI derived units | Draft 03 Q2 (trolley's faulty dimension) |
| Foot-to-meter length conversion | Draft 03 worked 5 ft example | Draft 03 Q1 (workshop shelf) |
| lbf-to-N force conversion | Draft 03 worked 10 lbf example | Draft 03 Q3 (cable) |

### Coverage gaps not hidden
- Basic Length and Time are supporting concepts, rather than explicitly assessed objectives. If the final outline promotes them to separate objectives, Stage 03 must provide suitable new independent checks.
- The inverse-square gravitation law is now introduced as a guided conceptual bridge but is NOT tested for independent mastery. Stage 03 must choose whether to treat it as a standalone objective needing assessment or a limited prerequisite bridge.
- A force on a rigid body might also be characterized through its line of action in specific statics formulations; the current introduction intentionally does not prematurely teach moment/equivalent-force theory.

## Review dimensions, teaching burden and author/source distinction
- Prerequisite bridges: added Force as a vector, Resultant and contact interactions before later formulas; kept detailed components, FBDs, moments and equilibrium equations for later chapters.
- English-Arabic integration: familiar observation first, technical English term near meaning, concise English exam wording then Egyptian Arabic comprehension. English model answers plus explanatory Arabic feedback remain separate from question narration.
- Numerical sanity: 4/2=2 m/s²; 12/3=4 m/s²; 5×9.81=49.05 N; 5×0.3048=1.524 m; 2.5×0.3048=0.762 m; 10×4.448=44.48 N; 8×4.448=35.584 N; 4×3=12 N. All newly introduced applied scenarios are authored exercises, NOT original numbered textbook problems.
- Scientific/contextual clarifications beyond literal source prose: qualifier for nonaccelerating frame, SI symbol etymology, exact foot definition, and orbit/free-fall distinction. These should be checked by the teacher; do not misattribute the clarifications as textbook quotations.
- Read-aloud issue: ΣF, superscripts, subscripts, SI and lbf need careful phonetic/English pronunciation review at later audio pilot. Non-spoken headings and Attempt labels must not enter TTS.
- No measured lesson duration and no student evidence. Increased checks may impose fatigue; only Stage 03 may lock learning chunks and rewrite resulting lessons.

## Recommended possible boundaries — deferred to Stage 03
- Working lesson 01: consider **internal parts** (why mechanics matters + core quantities; then idealization choices), or split only if independent assessments show a true prerequisite or conceptual boundary. Do not split by heading/count alone.
- Working lesson 02: consider internal parts for Newton laws and gravitation/weight; possible separate weight lesson if actual novice evaluation shows the concept load is excessive. The source's gravitation formula deserves an explicit coverage/objective decision.
- Working lesson 03: likely keep it one lesson with distinct conversion and unit checks. Could move a tiny SI bridge closer to the second-law example if it helps, without duplicating whole explanations.
- **No actual split/merge/reordering/stable ID decision has been made or approved.** Outline remains a provisional working map.

## Outstanding review/production boundaries
- A qualified engineering-mechanics reviewer and teaching reviewer are still needed; AI editorial self-review is not independent scientific or student validation.
- Original PDF is image-only and partly skewed; very small print in original must be rechecked before an academic pass. Chapters 3–7 are contents entries only.
- No lesson.json, scenes, formal storyboards, media, timing, runtime testing, paid audio, platform integration, main merge or student publication.
- Await the next human **next** or comments before Stage 03.
