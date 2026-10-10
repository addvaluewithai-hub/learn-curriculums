# ems-y1-foundations-models — Stage 04 authoring status

- Ordered lesson: 1; B01; issued ID is unchanged.
- Scene JSON is now the **canonical spoken text**. Original `drafts/01-mechanics-and-models.md` remains a **read-only Stage 03 reference snapshot**, NOT a second editable script.
- Teaching scene paragraphs: 14; question scenes: 4; feedback clips: 4 (separate from ordinary scene path).
- Both landscape and portrait storyboards embedded in each scene visual; shared lesson-local bespoke React concept board scaffold at `scenes/ConceptBoard.tsx`.
- Script text copied exactly from Stage 03 spoken teaching paragraphs, question clauses, English answers and Arabic feedback. No artificial duration/timing/audio created.
- Current review statuses in review.json: all **untested** until genuine human and later media/runtime evidence; original source storage remains temporary.
- Authored question examples are not printed textbook exercises. Academic and learner-level verification pending.
- Next human action: inspect Stage 04 content; `next` for B01 Stage 05 dry-run pilot, or `next block` for B02 Stage 01; no paid calls authorized.

## B01 Stage 05 — pilot dry-run (2026-10-09)
- Prepared clips: `N02` (teaching); each job in `jobs/<jobId>.json`, indexed by `../../blocks/B01/PILOT_REQUESTS.json`.
- **Not sent / paidCall=false**, no WAV/transcript/media receipt, no human listening pass, no timings. Gacrux WAV 24 kHz quality request saved with scriptHash.
- Actual no-send code test passed on GitHub Actions `37951705099`; all six review checks remain `untested`. Future paid dispatch requires separate explicit scope/cost authorization, not just `next`.

## B01 Stage 05 — real pilot audio delivered after dry-run (2026-10-09)
- Real paid pilot dispatch authorized by owner and executed via factory Issue https://github.com/addvaluewithai-hub/gemini-tts/issues/8.
- Produced clips: `N02` — 24.20s, factory run 37955404099. WAV, word-level transcript and VTT delivered; **none** imported as selected lesson media receipts yet.
- Listening, pronunciation, educational accuracy, word-timing acceptance and SDK visual preview remain `untested`. 
- Do not send other jobs or start Stage 06 without a separate human instruction. See `../../blocks/B01/STAGE_05_PILOT_DELIVERY.md`.

## B01 Stage 05 — full audio catalog (2026-10-10)
- **All 22/22 canonical clips generated** (narration + separate feedback), with real WAV, transcript JSON and VTT externally verified. Voice Gacrux, routing quality. Each actual job and provider URL is indexed at `../../blocks/B01/AUDIO_ASSETS.json`; human listening catalog `../../blocks/B01/AUDIO_LISTENING_INDEX.md`.
- Previous pilot section above is historical; **no other clips are pending synthesis** for this lesson at this source version. `review.json` categories remain `untested`; local media receipts/timed anchors/visual playback not yet completed. Do not treat production as approval or authorized Stage 06.
