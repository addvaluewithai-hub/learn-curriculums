# B01 Stage 05 — actual pilot delivery (not listening acceptance)

**Human authorization:** Owner explicitly requested automatic production and confirmed unrestricted pilot cost; scope remained the **five** frozen pilot jobs. **Date:** 2026-10-09.

- Factory gateway PR https://github.com/addvaluewithai-hub/gemini-tts/pull/6 merged safely into `main` after passing unit CI.
- Owner-created smoke Issue #7 (mode `dry-run`) triggered gateway workflow run `37955305553`, `success`, no synthesis or dispatch.
- Actual production Issue **https://github.com/addvaluewithai-hub/gemini-tts/issues/8** triggered Issue Gateway run **`37955372144`**, completed `success`, with claim/comment records for five accepted `repository_dispatch` jobs. No manual Actions button or secret exposure.
- All five TTS factory runs returned `success`, and each output was **downloaded from its matching GitHub Actions artifact**, including `result.json`, WAV, transcript JSON and VTT. The WAV files were opened with a WAV parser and checked as 24 kHz, 16-bit audio; duration values measured from the actual WAV frames.
- **Model reported:** Gemini 3.8 Flash TTS (Gacrux voice); word-level transcript produced via Gemini transcription. Technical delivery is NOT listening-quality approval.

| Clip | Lesson | Factory run | WAV / audio | Actual duration | Recognized words |
|---|---|---|---|---:|---:|
| `N02` | `ems-y1-foundations-models` | [37955404099](https://github.com/addvaluewithai-hub/gemini-tts/actions/runs/37955404099) | [WAV](https://res.cloudinary.com/as9o12al/video/upload/v1791561404/gemini-tts/ems-y1-foundations-models-N02-pilot-t01-0a3e351a0fd049c18efaaec0adb1b3ca.wav) | 24.20s | 48 |
| `N13` | `ems-y1-newton-gravity` | [37955404707](https://github.com/addvaluewithai-hub/gemini-tts/actions/runs/37955404707) | [WAV](https://res.cloudinary.com/as9o12al/video/upload/v1791561412/gemini-tts/ems-y1-newton-gravity-N13-pilot-t01-d6626610f6224727895cb2a766056a30.wav) | 41.00s | 67 |
| `N09` | `ems-y1-newton-gravity` | [37955406507](https://github.com/addvaluewithai-hub/gemini-tts/actions/runs/37955406507) | [WAV](https://res.cloudinary.com/as9o12al/video/upload/v1791561402/gemini-tts/ems-y1-newton-gravity-N09-pilot-t01-a61efc0ff62c4b5baf03f353e1bddd83.wav) | 21.52s | 38 |
| `F02` | `ems-y1-newton-gravity` | [37955407674](https://github.com/addvaluewithai-hub/gemini-tts/actions/runs/37955407674) | [WAV](https://res.cloudinary.com/as9o12al/video/upload/v1791561405/gemini-tts/ems-y1-newton-gravity-F02-pilot-t01-559a668db17f4b8b9396da78ad63de2e.wav) | 30.32s | 57 |
| `N12` | `ems-y1-units-conversions` | [37955409962](https://github.com/addvaluewithai-hub/gemini-tts/actions/runs/37955409962) | [WAV](https://res.cloudinary.com/as9o12al/video/upload/v1791561411/gemini-tts/ems-y1-units-conversions-N12-pilot-t01-7c817d1fb0624c809d0c964972b0a45c.wav) | 32.92s | 59 |

## Quality review note (important)
- The word-level transcript for **N13 / Newton's Law of Gravitation** omits or compresses parts of the English law name and spoken `F = G m₁ m₂/r²` formula. This is **ASR evidence only**, not proof speech was actually omitted: missing transcription does not mean silence. A human must **listen to this clip first**, check actual pronunciation of subscripts, r squared and the English term, and retake only if the original audio is genuinely wrong.
- N09 question transcript retains the English question and Arabic explanation. F02 transcript contains net force, `4 m/s²`, and Arabic reasoning. N12 transcript records `0.3048` and `1.524`. Still require actual listening and educational review, not automatic acceptance.
- The five factory artifacts also provide transcript and VTT URLs. Exact URL suffix convention: source job name plus `.transcript.json` and `.transcript.vtt`; corresponding individual Cloudinary links are preserved in the recorded factory result.json artifacts. Do not infer timing correction or editorial approval from them.

## What Stage 05 does NOT certify
- No human listening sign-off, scientific/bilingual QA, audio quality certification, selected `media/<clip>/receipt.json` or word-reviewed `timing.json`. The five media jobs are **delivered externally** but have **not yet been imported/selected with `tools/cli.py audio-collect`** into the curriculum directory. Keep all `review.json` checks at `untested`.
- No Stage 06 timed preview/SDK playback, no bulk audio for the rest of 56 scenes, no PDF durable/private storage, no merge of Draft curriculum PR #7, no student publication.
- Distinguish immutable prep index `PILOT_REQUESTS.json` (its `prepared-dry-run-not-sent` statuses are a historic snapshot) from this **post-send** report and linked factory Issue #8. Avoid replaying same job IDs; factory storage IDs are deterministic and re-dispatch may overwrite outputs.

**Next human step:** Listen to the samples, especially N13, and give review/retake instructions. Only after source-media receipts and actual audio review may a separately authorized Stage 06 timing/preview process start. A broader paid batch requires separate explicit approval.
