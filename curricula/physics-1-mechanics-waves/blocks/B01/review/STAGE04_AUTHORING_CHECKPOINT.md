# B01 Stage 04 — authoring and validation record

**Date:** 2026-10-10 | **Goal:** convert four Stage 03 connected manuscripts into canonical scene data, question/feedback units, semantic cues, two responsive storyboard descriptions, and local visual components.
**Audience:** first-year engineering students. **Source:** S01 scanned pp.5–11 (printed 121–133), S02 printed pp.124–125 duplicate; no new source. Workbook values are authored and **not** claimed as copied exercises.
**Status at this git commit:** authoring done, actual GitHub Actions script-contract test pending; update check results only after inspecting a real CI run.

## Production files and counts

| Order/ID | Scenes | Teaching scenes | Question scenes | Feedback clips | Layouts |
|---|---:|---:|---:|---:|---:|
| 801 phys1-solid-structure-stress-strain | 9 | 7 | 2 | 2 | 18 |
| 802 phys1-young-axial-stiffness | 9 | 7 | 2 | 2 | 18 |
| 803 phys1-shear-deformation | 8 | 6 | 2 | 2 | 16 |
| 804 phys1-bulk-compression | 9 | 7 | 2 | 2 | 18 |
| **Total** | **35** | **27** | **8** | **8** | **70** |

- Per lesson: `lesson.json` stable issued ID/order/objectives/prerequisites, `scenes/Sxx.json` with narrator, `review.json` all untested, `STATUS.md`, and a custom React `scenes/ConceptBoard.tsx`.
- Question scene `narration.role=question` speaks English and Arabic support as separate full-clause semantic units. Feedback is separate `question.feedback.role=feedback` with English model answer and explanatory Arabic speech. Solutions aren't included in reading prompts or question-phase visual properties.
- Teaching paragraphs from the Stage 03 final manuscript are assembled in contiguous scene groups without rephrasing. Questions and answers copied to dedicated source clips from their Stage 03 sections. Closure follows both attempts/feedback.
- Each Scene has source ID and printed-PDF locator, original-practice label when applicable, storyboard ideas in independent landscape/portrait fields, and occurrence-qualified text anchors. No invented times or source page media included.
- Local TypeScript visual modules support responsive single-focus diagrams/captions, independent question/feedback phases and `cueIsVisible`/ `visibleQuestionParts` timing interfaces. The code has **not** been visually reviewed in runtime; this stage does not authorize that claim.

## Real checks and expected gates

1. GitHub Actions `Production contracts` default checks: unit tests, `tools/quality.py`, draft authoring validation, preview build checks and browser fixtures. Read actual status before marking passed.
2. GitHub Actions now adds **four exact `tools/cli.py validate --course ... --lesson ... --stage script` commands**. This is the **real existing repository validator**, not an invented JSON check.
3. After CI finishes: record run ID/result, rerun failed check if needed; don't advance stage if script validation fails. `review.json` stays `untested` independently of CI.
4. Media/timed and actual playback require real accepted recordings and measured alignments, outside Stage 04. No paid TTS and no student publication.

## Next human choice after verified Stage 04
- **next:** B01 Stage 05 audio pilot preparation/dry-run, separately obtain explicit consent before any paid TTS call.
- **next block:** start B02 Stage 01 Sound Waves authoring based only on printed pp.134–149; no Stage 00 repeat. Existing B01 audio may be deferred.
- Do not merge PR or mark qualified science/teaching approval without human evidence.
