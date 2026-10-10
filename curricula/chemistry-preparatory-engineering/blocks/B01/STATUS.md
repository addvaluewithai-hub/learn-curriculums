# B01 STATUS — Stage 04 authoring checkpoint

- **Date:** 2026-10-10. **Last completed gate:** B01 Stage 04; no media/timing/scientific approval. **Awaiting human** `next` (Stage 05 pilot dry-run) or `next block` (B02 Stage 01).
- **Student audience:** first-year engineering; explanatory Arabic ar-EG and English exam terminology/questions with Arabic support.
- **IDs/coverage fixed:** 1 `chem1-states-phase-changes` (book p8–9); 2 `chem1-boyle-law` (p10–12, Sheet1 #5 p17); 3 `chem1-charles-law` (p13–15, Sheet1 #7/#8 p17). Original PDF image pages 6–10; B01 objectives PDF5.
- **Canonical production:** `lessons/<id>/lesson.json` and `scenes/Snn.json`, with **18 scenes** (5/6/7 per lesson), **7 independent questions**, **7 separate post-attempt feedback clips**, **25 total text clips**. No duplicate maintained master speech.
- **Visual assets:** custom local `MatterBoard.tsx`, `BoyleBoard.tsx`, `CharlesBoard.tsx` plus a detailed 16:9 and 9:16 storyboard in each scene. Scene words anchored with occurrence-qualified text units only; no fabricated timings.
- **Academic/source notes:** corrected book Condensation (p9) and Boyle (p12) issues remain documented; workbook adaptations explicitly add missing constant T/P and sample conditions. Additional explanatory physical assumptions require an independent chemistry instructor review.
- **Tests:** real `script` validation added to CI via `tests/test_chemistry_b01_script.py`. Earlier run at SHA `a026040c06ae01ee97cb578e8afdce568b522db2` succeeded; final commit run to be verified. Full scene/speech mapping documented in `STAGE04_SCRIPT_INTEGRITY.md`.
- **Reviews:** all `review.json` checks sources, teaching, audio, timing, visual, runtime are `untested` with no fabricated `sourceHash` approvals; SDK preview (requires WAV and word timing) has not played.
- **Source storage:** original 20-page PDF retained outside public GitHub; p37 onward missing, private storage/rights unresolved.
- **Not authorized:** paid TTS send, accepted audio, timed animation QA, merge, DB writes or student publication. B01 audio can remain deferred while B02 proceeds on a future `next block`.
- **Decision:** this Stage is complete *as authoring*, not as accepted lesson; human next action required before any further stage. **STOP**.
