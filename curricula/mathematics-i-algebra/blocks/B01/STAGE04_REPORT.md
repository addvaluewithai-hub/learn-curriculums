# B01 — Stage 04 technical authoring report (2026-10-10)

**Scope authorized:** First-year engineering, Mathematics I — Algebra, B01 *Partial Fractions*, scanned printed pp. 1–5 / PDF pages 3–5. **Gate completed in authoring only.** Do not interpret this report as lesson runtime release, audio approval or teacher sign-off.

## Deliverables and canonical paths

| Issued stable Lesson ID | Order | Scenes | Teaching / Question | Feedback clips | Semantic units | Bespoke component |
|---|---:|---:|---:|---:|---:|---|
| \`math1-pf-foundations\` | 1 | 8 | 6 / 2 | 2 | 20 | \`scenes/MathBoard.tsx\` |
| \`math1-pf-forms\` | 2 | 9 | 7 / 2 | 2 | 22 | \`scenes/MathBoard.tsx\` |
| \`math1-pf-two-linear\` | 3 | 8 | 7 / 1 | 1 | 18 | \`scenes/MathBoard.tsx\` |
| \`math1-pf-three-linear\` | 4 | 9 | 7 / 2 | 2 | 22 | \`scenes/MathBoard.tsx\` |
| **Total** | — | **34** | **27 / 7** | **7** | **82** | **4** |

Each lesson lives at \`curricula/mathematics-i-algebra/lessons/<id>/\`, with \`lesson.json\` (immutable issued ID/order; objective, prerequisites, scene IDs, glossary), \`scenes/Sxx.json\`, \`scenes/MathBoard.tsx\`, \`review.json\` and \`STATUS.md\`.

### Authoring contract and teaching fidelity

- Scene teaching and question clips have unique \`Nxx\` IDs; question feedback is a **separate \`Fxx\` clip**. Each question has full English and natural Egyptian-Arabic prompt clauses; feedback has the English model answer and Arabic reasoning after the attempt.
- Objective-to-teaching-scene and objective-to-question-ID mappings appear explicitly in \`lesson.json\`. A novice gap found in final self-check (Proper/Improper F3 mapped only to transition-to-questions scene) was **corrected** to include actual F3 teaching scenes S03 and S04.
- Each script clip has verbatim occurrence-qualified semantic-unit phrases and a visual intent. Question English/Arabic reading units and feedback English/Arabic answer units are separate. **No fabricated atMs, wordStart, wordEnd or fake audio hashes**: real timing only after recorded audio/transcript review.
- Every scene has distinct \`visual.landscape\` (16:9) and \`visual.portrait\` (9:16) planning strings. Four React/Remotion components use real shared preview SDK imports and cue-dependent equation/phase panels. **These are prototypes:** device readability, true safe-area constraints and animation onset have **not been preview-tested**; component presence or CI cannot substitute for playback.
- Student question scenes use \`renderer="sdk-question-board"\`, \`visual.module=null\` and no answer in their **pre-attempt narration**; answer is present only in the separate feedback data/clip as the SDK requires. Pre-attempt visual leakage has **not been checked via real playback**.
- Original \`blocks/B01/final-scripts/*.md\` are now tagged **frozen Stage 03 editorial snapshots**, not a second independently edited canonical script. Going forward, all speech changes must be made in \`scenes/*.json\` and a continuous reading copy should be regenerated from those canonical clips.

## Source fidelity

- Source book: \`math1-algebra-scan-20261009\`; actual image body for B01 was reopened (PDF pp. 3–5) in this stage. Example 1 (printed p.1) appears in L01; rules & Examples 2/3 (pp.2–3) in L02; Example 4 (p.4) in L03; Example 5 (pp.4–5) in L04.
- Authored practice is attributed explicitly to a separate \`course.sources\` entry \`math1-b01-authored-examples\` (original editorial teaching questions; **not** printed textbook exercises). Actual source is scanned out-of-repo; the previous incorrect pseudo-local \`source.file\` text was removed because a \`file\` means a real relative local filesystem path in the validator.
- Differences in scanned Examples 3 and 5 have not been silently erased. Source observations and scientific derivations remain documented in \`blocks/B01/SOURCE_OBSERVATIONS.md\` and Stage02 critique. They still need independent qualified lecturer review.
- Seven algebraic equalities were independently recomputed with SymPy simplification in this session: textbook Examples 1/4/5, independent F-Q1 recombination, authored L03 guided example, T-Q1 and C-Q1. Every lhs−rhs simplifies to **0** at values where each fraction is defined. This is a computational check, not human science sign-off.

## Technical checks actually run

1. **Real repository \`script\` validator:** New non-platform test \`tests/test_stage04_curriculum_authoring.py\` discovers committed Stage 04 lessons by \`scriptRevision\` and invokes \`validate_lesson(ROOT, course, lesson, "script")\` on each one. It verifies valid structure, no publication approval and runtime unverified. This is **not** a mere ad hoc approximation.
2. GitHub Actions workflow \`Production contracts\`, PR run [#38054370082](https://github.com/addvaluewithai-hub/learn-curriculums/actions/runs/38054370082) (Stage04 script + test addition) and run [#38054556311](https://github.com/addvaluewithai-hub/learn-curriculums/actions/runs/38054556311) (responsive math-board upgrade) **completed with success**. Both included Python unittest discovery, repository quality check and \`tools/cli.py validate\` at default draft; only the added unittest explicitly calls **stage="script"**. The run covering latest status updates may have a newer commit SHA; verify that run separately before release decisions.
3. Validator stage is **script**, NOT media or timed. Audio/transcript/timing media validator checks are unrun because no media exists. CI preview build/tests are generic fixture technical checks, not visual acceptance of this lesson.
4. Manual contract audit recorded 4 unique stable IDs, 34 ordered scene paths, 7 standalone feedback clips, 82 semantic anchor strings, 16:9/9:16 authored visual plans, and current review status all untested. Feedback question-before-answer order was additionally checked in source and no model answer string was found in the question narration.

## Open issues, next gate and human choice

- **Human source/scientific/teaching review remains \`untested\`.** AI critique and SymPy do not replace a specialist or classroom trial.
- **Audio, timing, visual device playback and runtime:** all \`untested\`; there is no recording, no word timestamps, no selected take, no real preview acceptance.
- **Math phonetics / wording:** symbolic expressions have not been listened to as Arabic/English TTS; Stage05 pilot preparation should check pronounceable formula narration before dispatch, not invent timestamps. Recorded audio has **not** been requested.
- **Copyright/source location:** scanned original wasn't added to public GitHub. Rights unknown; prior linked Drive copy had anyone-with-link **writer** permission; a safe durable source reference is unresolved.
- **Coverage limit:** supplied scan body ends at printed p.45. B09–B11 are index-only and later source content must not be invented.
- **Next human decision A:** \`next / كمل\` → B01 **Stage 05**, representative bilingual/equation pilot **dry-run preparation only**, without paid TTS; then STOP.
- **Next human decision B:** \`next block / الجزء اللي بعده\` → B02 **Stage 01** from actually available printed pp.5 onward, while deferring B01 audio; then STOP.

**STOP: Stage04 delivered on Draft PR #12, not merged or published.**
