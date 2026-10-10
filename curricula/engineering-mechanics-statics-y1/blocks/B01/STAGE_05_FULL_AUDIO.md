# B01 Stage 05 — full 69-clip audio production (external, unapproved)

Date: 2026-10-10. **Owner expressly authorized all remaining B01 clips** after the five-clip pilot; this turn remained within B01 Stage 05. It did not authorize B02/B03+ audio, Stage 06 or student publication.

- **Source-of-truth pin:** `addvaluewithai-hub/learn-curriculums@0b135274fd9918c10bff83fd4affc82d1d35554c`, canonical 3 B01 `lesson.json` files and `scenes/*.json` (56 scene narration clips + 13 separate post-question feedback clips).
- Original five Gacrux pilot clips are preserved with their original Cloudinary IDs; factory's new `tts.issue.scene-range` handler automatically excluded these five.
- **64 new clips** synthesized in 12 small owner-created Issue requests **#11 through #22**. Every Issue permits 1–5 scenes and at most eight narration/feedback outputs, with unique job IDs derived from pinned script SHA-256 and Issue identity. Issue runs all recorded dispatch acceptance; no manually pressed Actions buttons.
- **Factory GitHub Actions:** 64 new `repository_dispatch` workflow runs returned `conclusion: success`. Prior pilot five runs also succeeded.
- **Delivery independently cross-checked in Cloudinary:** 69/69 distinct WAV assets (22 Foundations, 25 Newton/Gravity, 22 Units); 69 matching transcription JSON raw assets + 69 VTT raw assets. All URLs recorded verbatim from provider metadata in `AUDIO_ASSETS.json`. No inferred or fabricated links.
- Audio profile: **Gacrux**, mature warm calm Egyptian private-teacher style, `quality` routing, WAV `24000 Hz`, bilingual automatic transcription. `quality` may choose model fallbacks, so actual model must be read per job result before stating a single fixed model for all.
- Full student-audio playback has **not been listened to**; previously flagged pilot N13's automated transcription uncertainty remains unresolved until a reviewer checks the *audio*, not just ASR.
- Lesson-local `media/receipt.json` take selection, imported `result.json`/WAV/transcripts, source-aware `timing.json` cue alignment, real portrait/landscape SDK preview, spoken science/terminology sign-off and student release are **NOT** completed. All six independent `review.json` categories remain `untested`.

**Links:** [69-clip listening catalog](AUDIO_LISTENING_INDEX.md); [machine-readable exact assets](AUDIO_ASSETS.json); [factory automation PR #9](https://github.com/addvaluewithai-hub/gemini-tts/pull/9); [original five-clip evidence](STAGE_05_PILOT_DELIVERY.md).

**Next human gate:** Listen/review accents, bilingual numbers and equations; log targeted retake requests if audio is actually wrong. Separately authorize Stage 06 audio collection/alignment/SDK preview when ready. Do not mislabel generation as final educational approval, no automatic further TTS batch.
