# B01 Stage 05 — representative TTS pilot, dry-run only

**Authorization:** user's separate `next` after B01 Stage 04. **Date:** 2026-10-09. **Result:** requested **preparation and dry-run only**; no paid factory dispatch, recording, transcription, audio delivery, words/timing or listening evaluation.

## Actual factory configuration used
- Process: `tools/audio.py` request shape and the `tts.generate` asynchronous `repository_dispatch` contract documented in `addvaluewithai-hub/gemini-tts/docs/API.md` and `docs/AGENT.md`.
- Target factory: `addvaluewithai-hub/gemini-tts`. **No dispatch endpoint invoked.**
- Voice: **Gacrux**, as pinned in this curriculum's `production.json` (not the factory-wide Kore default).
- Acting direction: existing **calm, mature, warm Egyptian private teacher** style in request `style`. Exact words are copied verbatim from canonical scene narration/feedback, not editorial instructions.
- Routing: `quality`, `format=wav`, `sample_rate=24000`. Transcript: `language_codes=[]` (auto for Arabic + English), `write_vtt=true`.
- Version binding: `scriptHash=SHA-256` of each canonical clip script, and immutable unique `job_id` for `pilot-t01`; if script changes, the factory request fails `job_for` script-match checks instead of silently speaking stale words.
- Request index: `blocks/B01/PILOT_REQUESTS.json`. Five actual `jobs/<job-id>.json` source payloads are committed in their corresponding lesson directories; no `.dispatch.json` receipt exists, and none should be created without a fresh paid approval.

## Five carefully chosen clips
| Lesson | Scene / clip | Purpose and potential listening issue |
|---|---|---|
| Foundations & Models | S02 / **N02** (teaching) | Egyptian explanation and clear natural code-switching: Mechanics, Statics, Dynamics |
| Newton & Gravity | S13 / **N13** (teaching) | Pronounce Newton's Law of Gravitation, `F = G m₁ m₂ / r²`, subscripts and squared-distance relation correctly |
| Newton & Gravity | S09 / **N09** (question) | Read full English exam question and then natural Egyptian Arabic support; preserve numerical **3 kg** and **12 N**; no answer leakage before attempt |
| Newton & Gravity | S09 / **F02** (feedback) | Separate post-submit clip: English numerical model answer followed by Arabic explanatory feedback; pronounce `m/s²` and “net force” correctly |
| Units & Conversions | S12 / **N12** (teaching) | Decimal/practical unit speech: `0.3048`, `1.524`, foot-to-meter conversion and cancellation without dropping digits |

**Across three lessons:** three teaching clips, one independent bilingual question clip, one independent bilingual feedback clip. This is **a representative pilot**, not a whole-course or 69-clip synthesis batch.

## Safe real-code validation (not audio generation)
- Prepared 5 payloads with the same fields as `audio.prepare` in `tools/audio.py`; payload text, `scriptHash`, roles, metadata, voice and format preserved.
- `tests/test_statics_b01_audio_pilot.py` re-opens **every saved job** with actual `audio.job_for`, verifies SHA-256 and exact current canonical script match, and calls actual `audio.dispatch(send=False)`, expecting `status=dry-run`, `paidCall=False`, and *no* dispatch receipts. The test explicitly mocks `subprocess.run` to throw if sending were attempted.
- It separately calls **real `audio.prepare()`** for a short-lived `ci-probe` bilingual question, compares the generated request with its stored pilot equivalent, invokes the dry-run dispatch code and cleans up the fixture.
- **GitHub Actions success:** `Production contracts`, run `37951705099` on `b420b717aeca71b035dc8a28b40ef2bffaefb729`. Unittest suite, quality, standard validate and preview build checks completed; this includes the new safe audio pilot tests and previously installed script-stage tests. This only proves contract/format consistency, **not voice sound**.

## Listening/academic criteria AFTER separately approved dispatch, not passed today
1. Gacrux genuinely sounds like a natural, calm Egyptian teacher rather than mechanically reading English acronyms or sounding unnatural.
2. Spell and speak `Statics`, `Dynamics`, `Newton's Law of Gravitation` clearly; spoken `m₁`, `m₂`, `r²` have the right index/exponent; do not change the physics in paraphrase.
3. Keep exact values: 3 kg, 12 N, 0.3048 meter/foot, 1.524 meters; readable decimals, signs, units and negation.
4. The full English question is heard before Arabic support, and *answer/feedback* speech does not appear until **after** a valid written attempt/submit.
5. Upon actual delivery, inspect generated audio bytes/actual WAV duration, result+transcript source text, English words, ASR gaps and word-level timestamps. Missing ASR ≠ silence; review listening first, then correct alignment if needed.
6. Observe portrait 9:16 and landscape 16:9 behavior only after actually timed/pinned SDK playback; no runtime result is asserted from these dry-run jobs.
7. Independent science and teaching reviewers must still inspect the original source, content and novice appropriateness; `review.json` remains fully **untested** for all six check categories.

## Exactly where human authorization is needed
- This user message **did not approve paid audio dispatch**. Before sending, obtain separate explicit approval of **the five indexed B01 pilot clips, expected costs/budget and factory access**; use saved exact payloads only. Do not start a batch automatically.
- After actual deliverables are collected, verify and listen to a pilot before asking for separate batch approval. **Stage 06 cannot run on nonexistent audio**.
- Alternatively, human `next block` may choose B02 Stage 01 with B01 paid audio deferred, if **actual** printed Ch.2 PDF source pages are available to reopen then.
- No original PDF was made public or claimed durable. Publishing/merging remains separate and unauthorized.
