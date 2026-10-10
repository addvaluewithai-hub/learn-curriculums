# Block B02 STATUS — Functions, Graphs, Limits and Continuity

**Updated:** 2026-10-10  
**Active Block:** **B02 ACTIVE — Stage 04 script/scene/visual authoring completed**, now **STOP for human inspection**.  
**Book/source:** `abd-el-salam-math-i-scan`, printed **pp. 21–53**, photographed PDF **14–30 left**. Original scanned source was checked during prior B02 editorial work; temporary chat-only access, **not proven durably available** to future agents. User explicitly deferred private PDF storage; no public upload. Source rights unknown.  
**Draft PR:** [#8](https://github.com/addvaluewithai-hub/learn-curriculums/pull/8) on `curriculum/engineering-math-1/stage-01-functions`, **open/draft/unmerged**.

## Last authorized human gate and canonical source

- User sent fresh **`Next`** when B02 **Stage 03** had been completed. Stage 04 **ONLY** now builds canonical lesson packages for the eight previously issued stable IDs. **No Stage 05 audio, B03 authoring, professor approval or student publication**.
- **Stage 04 authoring result:** **8** complete `lessons/<stable-id>/lesson.json`, **106 ordered scene JSONs** including **80 teaching + 26 independent written exam attempts**, plus **26 separately withheld post-attempt feedback clips = 132 distinct speech clips**. B02 Stage 03 historical editorial manuscripts `final-scripts/*.md` preserved unchanged and are **not independently editable canonical spoken text now**.
- **Actual canonical speech:** `../../lessons/<id>/scenes/Sxx.json` teaching/question narration and `question.feedback`. **Do not maintain a second separately edited final manuscript.** The Stage 03 texts are historical source comparison for regression testing.
- **8 subject-specific lesson React/Remotion `scenes/ConceptBoard.tsx` components**, and distinct 16:9 vs 9:16 instructions in each `STORYBOARDS.md` and scene `visual`; disclosure via full spoken-phrase text anchors, no fabricated timestamps or audio. **Rendered real lessons, narrow screens and actual player behavior UNTESTED**.
- **`review.json`:** six checks **sources/teaching/audio/timing/visual/runtime all `untested`**, sourceHash null. No dummy pass/reviewer.

## Eight issued B02 IDs — local orders 1–8 vs global runtime 6–13

| B02 local order | Stable ID; canonical folder under `../../lessons/` | Curriculum global `lesson.json.order` | Teaching scenes | Questions / separate feedback |
|---:|---|---:|---:|---|
| 1 | `em1-functions-domain-range` | 6 | 11 | 4 / 4 |
| 2 | `em1-functions-algebraic-graphs` | 7 | 10 | 3 / 3 |
| 3 | `em1-functions-trig-exp-log` | 8 | 9 | 3 / 3 |
| 4 | `em1-functions-monotonicity` | 9 | 9 | 3 / 3 |
| 5 | `em1-limits-concept-one-sided` | 10 | 9 | 3 / 3 |
| 6 | `em1-limits-algebraic-methods` | 11 | 10 | 3 / 3 |
| 7 | `em1-limits-trigonometric` | 12 | 10 | 3 / 3 |
| 8 | `em1-functions-continuity` | 13 | 12 | 4 / 4 |

**Global runtime orders 6–13** are deliberate because B01's five previously issued student lessons already have `lesson.json.order` 1–5. B02's within-block issued order remains 1–8 and no B01 lesson/ID was renumbered. The repo's `validate_curriculum` rejects duplicate runtime orders.

## Evidence and outstanding blockers

- **Detailed Stage 04 authoring/readback evidence:** `reviews/STAGE_04_SCENES.md`; confirmed lesson source/topic boundaries `reviews/STAGE_03_BOUNDARY_DECISION.md`, Stage 02 critique `reviews/STAGE_02_CRITIQUE.md`.
- **Technical checks:** persistent `tests/test_b02_stage04_scene_fidelity.py` compares every spoken word with the issued Stage 03 manuscripts, question/feedback separation, objective maps and global orders; generic `tests/test_script_stage_ready.py` validates authored lesson packages at the actual `script` contract stage. Record exact GitHub Actions success/failure from the final commit — no local GitHub checkout or visual playback is claimed.
- **Original/source caveats:** printed **p.34** appears to reverse exponential domain/range; authored lesson 3 uses standard independently checked mathematics and explicitly flags the probable book misprint. Printed **p.42** quotient-zero shorthand needs sign/context rather than real zero division. **Academic source/solution sign-off NOT DONE**.
- **UNTESTED:** independent math lecturer review, novice student pilot, Arabic/English voice pronunciation and number/formula rendering, original media duration/timed anchors, actual React component compilation for these real B02 lessons, 320px portrait, reduced motion, seek/replay/submit→feedback, human acceptance. Technical CI / fixture SDK build never means student content approved.
- **B01 unchanged and inactive:** five stable student IDs, 72 earlier canonical scenes and 15 question/feedback pairs, audio and academic review deferred. **B03 has not started.**

## HUMAN STOP — two exclusive future authorizations

**STOP now at the B02 Stage 04 authoring checkpoint.** A **future bare `next`** advances **B02 Stage 05 optional representative audio-pilot preparation/dry-run ONLY**; any paid TTS dispatch requires separately explicit user permission. A distinct **`next block`** may begin **B03 Stage 01** only after human inspection of B02 Stage 04 artifacts and verification that actual B03 source body is accessible. B02 voice, true playback and specialist approvals may remain deferred/unapproved. A correction today revises B02 Stage 04 without advancing.
