# Curriculum STATUS — Engineering Mechanics (Statics), Year 1

## Course control plane — migration to Block workflow
- Workflow alignment date: **2026-10-09**, against `main` revision `ba4706956c2c8ee3bf4103c08124b28b74c3390e`.
- This is a **structural reconciliation of existing Stage 01–03 work**, not a retroactively executed or human-approved separate Stage 00. Original human decisions and the source/editorial history stay intact.
- Course ID: `engineering-mechanics-statics-y1`.
- Active Block: **B01 — Introduction / printed Chapter 1 pp.1–6**.
- Course branch/PR: `curriculum/engineering-statics-y1-stage01` / Draft PR #7 — https://github.com/addvaluewithai-hub/learn-curriculums/pull/7.
- Last executed B01 gate: **Stage 05 — five-clip real paid TTS pilot delivered structurally** (Gacrux, 5 WAV files and transcripts/VTT). Audio listening/academic review **not approved**; Stage 06 NOT started. Production evidence: `blocks/B01/STAGE_05_PILOT_DELIVERY.md`.
- **Next authorized gate: NONE — awaiting human listening feedback or a new instruction.** User explicitly approved the five paid pilot clips and production completed. No full-course audio batch or Stage 06 authorized; `next block` still depends on actual Chapter 2 source access.

## Global source and roadmap
- Master plan: `OUTLINE.md` — provisional whole-course B01–B09, including unavailable source blocks. The **B01 subsection only** contains finalized Stage 03 lesson mapping.
- Source version ID: `statics-scan-2026-10-08`; 36-page original, actual 7,938,527 bytes and SHA-256 `d05d173a02514f6093662c072fa0d8d08deba18d5e552b9586ecdcee1d6591d9`, measured from accessible original on 2026-10-09.
- Source manifest and access/rights: `references/SOURCE_MANIFEST.md`; coverage by actual scan/printed page: `references/SOURCE_COVERAGE.md`; prior inspect notes: `references/SOURCE_REVIEW.md`.
- **Storage = chat-only-temporary, no verified private durable retrieval; redistribution rights unknown.** Original scanned book never committed to public repo. Future agent must retrieve and verify this exact SHA from authorized private storage before authoring another source-grounded Block.
- B01 actual inspected source body: Ch.1 printed pp.1–6; PDF scan pp.7–12. B02/B03 Ch.2 body is supplied but needs full new source review; B04 onward unavailable/contents-only.

## Blocks overview (not lesson IDs)
| Block | Roadmap coverage | Current editorial gate/status |
|---|---|---|
| **B01 (active)** | Ch.1 printed pp.1–6 | **Stage 05 real pilot: 5/5 factory jobs successful; 5 WAV+transcript+VTT delivered**. Human listening, playback/timing acceptance and science checks untested; see `blocks/B01/STATUS.md` |
| B02 | Ch.2 printed pp.9–18; scalar/vector and planar force foundations | Planned only; no active Block STATUS or lesson IDs |
| B03 | Ch.2 printed pp.19–30; unit vectors/resultants/position vectors | Planned only; no active Block STATUS or lesson IDs |
| B04 | Ch.2 printed pp.32 onward, missing body | Blocked: index only |
| B05 | Ch.3 Equilibrium of Particles, missing body | Blocked: index only |
| B06 | Ch.4 Moments/Equivalent Force Systems, missing body | Blocked: index only |
| B07 | Ch.5 Equilibrium of Rigid Body, missing body | Blocked: index only |
| B08 | Ch.6 Structure Analysis, missing body | Blocked: index only |
| B09 | Ch.7 Friction, missing body | Blocked: index only |

## B01 editorial and production status
- Stable issued lesson IDs (unchanged): `ems-y1-foundations-models`, `ems-y1-newton-gravity`, `ems-y1-units-conversions`; order 1/2/3.
- Historical Stage 03 scripts remain untouched as **read-only comparison snapshots** in `drafts/*.md`; the new canonical spoken text lives in `lessons/<stable-id>/scenes/*.json` narration + separate feedback. Total: **43 teaching scenes + 13 question scenes = 56 scenes**; 13 independent written attempts.
- Critique and boundaries: `reviews/STAGE_02_CRITIQUE.md` and `reviews/STAGE_03_BOUNDARIES.md`.
- Previous editorial arithmetic/structure preflight passed as recorded in Git history; **no formal human scientific approval or student test claimed**.
- **2026-10-09 reconciliation verification:** GitHub readback passed for source manifest, coverage, course/Block checkpoints and roadmap; measured SHA/pages/bytes align with source metadata; all three B01 script Git blob SHAs **exactly unchanged** from prior Stage 03 head; authored Markdown/JSON files remain <=300 lines. Local full `tools/quality.py`, `unittest`, and `validate` were **not run**: cloning the repo failed due to DNS resolution of `github.com` (exit 128). No CI, teacher or runtime pass inferred.
- **Authored:** 3 lesson JSONs, 56 canonical scenes, responsive storyboards, 114 anchors and original React boards. **Stage 05:** 5 pilot requests and GitHub Issue #8 triggered 5 real factory dispatches, **all returned WAV + transcript + VTT**. Separate lesson media receipts/selection and reviewed word alignment are **not yet collected**. Human listening, runtime preview, science approval, student release and merge remain pending.

## Handoff and unresolved decisions
- **Pilot dispatch was explicitly authorized and executed** for exactly five clips on 2026-10-09. Next: **listen/review** Arabic and English speech, equation exponents/digits, then use the established `audio-collect` receipt/selection verification before true Stage 06 timing/playback. Full 56-scene batch needs a fresh instruction and review; the five-clip approval is not blanket permission.
- Alternative after inspection: **`next block`** starts B02 Stage 01 without waiting for B01 audio, but actual Ch.2 pages must be available and reopened.
- **Open source decision:** owner must supply/authorize an approved private durable PDF location, with future-agent access and retrieval verification; public upload not authorized.
- Reviewer pending: accurate print/source detail including skewed pages, teacher/learner evaluation (especially B01 L02), scientific and bilingual checks. Source hash is measured, but rights/persistent storage have not been verified.
- Change audit: structural-only alignment to new workflow; no renames or modification to stable lesson IDs, accepted content, audio or published editions. Any script amendment is a separate explicitly reviewed change.

- **Stage 04 actual CI:** `Production contracts` completed **success** on head `c6857f8e739ef9277a43d784bfdec141f196f869` (run `37948932838`), including `tests/test_statics_b01_script.py` which executes the actual `--stage script` validator on each B01 lesson, plus repository unittest/quality/default validation. Final STATUS-only change will trigger a new head run. These are structural checks, not human approvals.

- **Stage 05 actual evidence:** GitHub Actions `Production contracts` run `37951705099` for commit `b420b717aeca71b035dc8a28b40ef2bffaefb729` succeeded. `tests/test_statics_b01_audio_pilot.py` checked all five saved job payloads against current canonical clips and exercised `audio.prepare()` plus `audio.dispatch(send=False)` with sending subprocess blocked. This is **dry-run verification only**, not generated audio. See `blocks/B01/STAGE_05_PILOT_DRY_RUN.md`.

- **Stage 05 delivery evidence:** factory Issue https://github.com/addvaluewithai-hub/gemini-tts/issues/8 ; five `repository_dispatch` runs all `success`, original GitHub artifacts downloaded and inspected: 5 WAVs (24 kHz, 16-bit) and transcripts/VTT. WAV durations 24.20 s / 41.00 s / 21.52 s / 30.32 s / 32.92 s. Recognition of the N13 gravitation law/equation appears incomplete, requiring actual listening. Read `blocks/B01/STAGE_05_PILOT_DELIVERY.md`. Scientific/audio review remains `untested`.

- **2026-10-10 B01 FULL AUDIO (user-approved):** all **69/69 canonical clips** were generated (56 narration + 13 feedback; five previous pilot + 64 new), all **64 new factory Actions succeeded**, and all **69 WAV + 69 transcript JSON + 69 VTT URLs** were verified by listing Cloudinary video/raw assets. Voice Gacrux, quality routing, source commit pinned. Browse `blocks/B01/AUDIO_LISTENING_INDEX.md` and `blocks/B01/AUDIO_ASSETS.json`. No human listening approval, immutable lesson-selected receipts, word cue authoring, Stage 06, full-course B02+ audio, or publication. **Next human step: listening review/retakes or explicit Stage 06 authorization**.
