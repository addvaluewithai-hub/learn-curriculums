# B01 Stage 04 authoring and structural verification

**Human authorization:** `next` after workflow reconciliation on 2026-10-09, for B01 Stage 04 **only**. No paid synthesis, source public upload, audio or student publication.

## New canonical source inventory
| Stable lesson ID | Teaching scenes | Question scenes | Separate feedback clips | Total ordered scenes |
|---|---:|---:|---:|---:|
| `ems-y1-foundations-models` | 14 | 4 | 4 | 18 |
| `ems-y1-newton-gravity` | 15 | 5 | 5 | 20 |
| `ems-y1-units-conversions` | 14 | 4 | 4 | 18 |
| **Total** | **43** | **13** | **13** | **56** |

- Each lesson has `lesson.json` with issued stable ID, order, prerequisites and objective `taughtIn`/`assessedIn`; 56 ordered scene JSONs include source locators, `narration.script`, semantic units, and **independent landscape/portrait storyboard specifications**. Each of the 13 written question scenes has English wording, spoken Arabic support, a required attempt and a **separate** feedback clip with English model answer plus Arabic reasoning.
- Stage 03 text-preservation comparison during generation: **every teaching paragraph copied verbatim and in order**; question/feedback wording preserved. Old `drafts/*.md` files are archived comparison snapshots, *not independently editable master scripts*; any future reading copy must be generated from canonical scenes.
- Total **114 semantic units** across teaching, questions and separate feedback, including whole-English and whole-Arabic question/answer anchors. They have IDs and visual intentions, **not fabricated word timestamps**.
- Bespoke `scenes/ConceptBoard.tsx` module in each lesson with original SVG diagrams for force arrows, gravity, models and unit conversion; uses SDK `frame` and `cueIsVisible` and `visibleQuestionParts`; no extra player or textbook scan assets. These modules are **not yet compiled/rendered against recordings**, so precise motion/onset, typography, question interactions, seek/replay and actual 320px layout remain *untested*.
- Each scene's `visual.landscape` and `visual.portrait` specify distinct 16:9 versus 9:16 compositions. Pre-submit question visuals are neutral; model answers reside only in answer/feedback objects and are intended for post-attempt display.
- Full original scanned PDF source remains `chat-only-temporary` with unverified permanent retrieval and rights, per owner's decision to handle it later. Only previously inspected B01 source content is decomposed here; **no newly invented chapters**.
- `review.json` sources/teaching/audio/timing/visual/runtime checks **all remain `untested`**. No false teacher, student or playback approval.

## Actual structural evidence
- Authoring preflight: teaching paragraph exact-equality check to reviewed Stage 03 scripts, independent question/feedback inventory (4/5/4), correct issued IDs and objective mapping, nonempty source locators and per-scene landscape/portrait fields, authored file line limits.
- GitHub Actions `Production contracts` on SHA `c6857f8e739ef9277a43d784bfdec141f196f869`, run **`37948932838`**, returned **success**. It runs Python unittest discovery, `tools/quality.py`, default `tools/cli.py validate`, preview checks; the newly authored `tests/test_statics_b01_script.py` also invokes **real** `tools/cli.py validate --course engineering-mechanics-statics-y1 --lesson <ID> --stage script` for all three lessons and tests pre-attempt answer absence.
- These are **structural** checks, not math/science reviewer sign-off, TTS listening review, responsive-rendered screenshot approval or actual runtime playback. Subsequent STATUS/OUTLINE metadata commit requires latest-head CI check.

## Human stop / options
- **`next`** after inspection → B01 Stage 05 **dry-run** bilingual/equation audio pilot preparation only; paid dispatch requires separate explicit approval.
- **`next block`** after inspection → B02 Stage 01 source-reopened drafts; B01 audio may remain deferred.
- Comments → revise Stage 04 only and stop.
