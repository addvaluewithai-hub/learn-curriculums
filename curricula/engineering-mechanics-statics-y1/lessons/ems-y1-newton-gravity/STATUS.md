# ems-y1-newton-gravity — Stage 04 authoring status

- Ordered lesson: 2; B01; issued ID is unchanged.
- Scene JSON is now the **canonical spoken text**. Original `drafts/02-newton-and-weight.md` remains a **read-only Stage 03 reference snapshot**, NOT a second editable script.
- Teaching scene paragraphs: 15; question scenes: 5; feedback clips: 5 (separate from ordinary scene path).
- Both landscape and portrait storyboards embedded in each scene visual; shared lesson-local bespoke React concept board scaffold at `scenes/ConceptBoard.tsx`.
- Script text copied exactly from Stage 03 spoken teaching paragraphs, question clauses, English answers and Arabic feedback. No artificial duration/timing/audio created.
- Current review statuses in review.json: all **untested** until genuine human and later media/runtime evidence; original source storage remains temporary.
- Authored question examples are not printed textbook exercises. Academic and learner-level verification pending.
- Next human action: inspect Stage 04 content; `next` for B01 Stage 05 dry-run pilot, or `next block` for B02 Stage 01; no paid calls authorized.

## B01 Stage 05 — pilot dry-run (2026-10-09)
- Prepared clips: `N13` (teaching), `N09` (question), `F02` (feedback); each job in `jobs/<jobId>.json`, indexed by `../../blocks/B01/PILOT_REQUESTS.json`.
- **Not sent / paidCall=false**, no WAV/transcript/media receipt, no human listening pass, no timings. Gacrux WAV 24 kHz quality request saved with scriptHash.
- Actual no-send code test passed on GitHub Actions `37951705099`; all six review checks remain `untested`. Future paid dispatch requires separate explicit scope/cost authorization, not just `next`.

## B01 Stage 05 — real pilot audio delivered after dry-run (2026-10-09)
- Real paid pilot dispatch authorized by owner and executed via factory Issue https://github.com/addvaluewithai-hub/gemini-tts/issues/8.
- Produced clips: `N13` — 41.00s, factory run 37955404707; `N09` — 21.52s, factory run 37955406507; `F02` — 30.32s, factory run 37955407674. WAV, word-level transcript and VTT delivered; **none** imported as selected lesson media receipts yet.
- Listening, pronunciation, educational accuracy, word-timing acceptance and SDK visual preview remain `untested`. N13 gravitation ASR omits/compresses key English/formula wording: inspect real audio before approving.
- Do not send other jobs or start Stage 06 without a separate human instruction. See `../../blocks/B01/STAGE_05_PILOT_DELIVERY.md`.

## B01 Stage 05 — full audio catalog (2026-10-10)
- **All 25/25 canonical clips generated** (narration + separate feedback), with real WAV, transcript JSON and VTT externally verified. Voice Gacrux, routing quality. Each actual job and provider URL is indexed at `../../blocks/B01/AUDIO_ASSETS.json`; human listening catalog `../../blocks/B01/AUDIO_LISTENING_INDEX.md`.
- Previous pilot section above is historical; **no other clips are pending synthesis** for this lesson at this source version. `review.json` categories remain `untested`; local media receipts/timed anchors/visual playback not yet completed. Do not treat production as approval or authorized Stage 06.

## B01 Stage 06 — evidence-only technical preflight (partial, 2026-10-10)
- **25/25 real WAVs plus factory transcript and VTT** checked against current canonical scene clip scripts in GitHub Actions run `38038542682`; no structural violations. The original audio clip identity and text are preserved (factory only flattened bilingual paragraph breaks).
- **Actual B01 preview still blocked:** `media/N01/receipt.json` not present. Lesson files have NOT been selected via `audio-collect` or imported as reviewed local immutable takes; cue `timing.json` and real mobile/landscape playback were not invented.
- Human listening, science, audio, timing, visual and runtime checks remain `untested`. See `../../blocks/B01/STAGE_06_TECHNICAL_PREFLIGHT.md` for audit/artifact and decisions needed.

## B01 Stage 06 — selected original-factory takes linked (2026-10-10)
- **25/25 source-bound `media/<clipId>/receipt.json` selections persisted**, plus matching original factory `takes/<jobId>/result.json` metadata. No WAV/ASR binaries are committed; [full hydrated media CI](https://github.com/addvaluewithai-hub/learn-curriculums/actions/runs/38040173233) verified the real sound and passed this lesson's `validate --stage media` check.
- ASR-anchored timing proposals are **draft only**; full human-reviewed `timing.json`, SDK preview and publication are NOT passed. User gave general listening approval; formal scientific/timed/runtime `review.json` checks remain untested. See `../../blocks/B01/STAGE_06_MEDIA_LINKING.md`.
