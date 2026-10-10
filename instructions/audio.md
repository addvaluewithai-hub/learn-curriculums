# Audio production and recovery

## Factory

Read current [API](https://github.com/addvaluewithai-hub/gemini-tts/blob/main/docs/API.md)
and [agent guide](https://github.com/addvaluewithai-hub/gemini-tts/blob/main/docs/AGENT.md) before dispatch.
Factory uses asynchronous repository_dispatch; never invent a synchronous completion endpoint.
Defaults live in production.json; course.teacher overrides voice/style/languageCodes.
Gacrux is this project's accepted mature, calm Egyptian default; factory-wide Kore does not override it.
Acting direction in style, speech in script; WAV 24kHz, actual waveform duration for playback.
Auto language detection is default here; audit a representative bilingual/number pilot before batch synthesis.

## Prepare and send

```bash
python3 tools/cli.py audio-prepare --course COURSE --lesson LESSON --clip N01 --take t01
python3 tools/cli.py audio-dispatch --job curricula/COURSE/lessons/LESSON/jobs/JOB_ID.json
```

Both are safe without secrets; dispatch defaults to dry-run. --send needs authenticated gh and authorized synthesis scope.
An authorized GitHub connector may dispatch the exact saved payload instead, preserving unique job_id/request metadata.
No credentials in browser/source/payload. One request per clip and unique job IDs; reuse overwrites factory outputs.
CLI records intent first. On timeout/error inspect factory before retrying: outcome may be unknown, not failed.
Do not delete dispatch history and blindly resend. Reconcile outcome or create a new take only when actually needed.
No paid call in CI/setup; script-only/dry-run requests remain so.

## Collect

Find the matching factory Actions job and download its result.json artifact; not simply the newest run.

```bash
python3 tools/cli.py audio-collect --job curricula/COURSE/lessons/LESSON/jobs/JOB_ID.json --result /path/result.json
```

Downloads completed audio/transcript HTTPS URLs; checks identities, scriptHash, waveform duration, structure and hashes.
--audio /path/audio.wav --transcript /path/transcript.json uses downloaded files instead.
--select-new-take explicitly changes selection while preserving old takes.
Delivery remains publicationApproved=false; speech/English/values/negation need actual listening review.
If factory normalization changes source_text, inspect the exact request/delivery; do not certify a mismatch.

## Recovery

Missing ASR does not prove missing speech/silence. Review audio first.
Correct speech: retranscribe same audio using supported auto-language/multiple passes or alignment, not a retake by default.
Preserve original evidence, served hash, full-audio origin and slice offsets; no guessed English timestamps.
Corrected alignment is a separate evidence-bound revision; original result/transcript stay intact.
Import reviewed corrections with evidence:

```bash
python3 tools/cli.py audio-align --course COURSE --lesson LESSON --clip Q01 --transcript /path/corrected.json --method multi-pass-reviewed --reviewer REVIEWER --evidence "Actual recording reviewed; full-audio offsets verified"
```

The corrected file keeps the word_timestamps schema and original source_text. Times refer to full served audio, not a sliced origin.
This command verifies bounds/hash/provenance; it does not listen or create corrected words for you.
timed checking uses the selected corrected transcript hash when available; stale corrections fail after a new take.
Build adapters must follow alignment.json when present; never falsify the original factory result.
Wrong speech: retake only affected clips. New selected audio invalidates old cues/review.
Follow [AI-authored timing](timing.md): choose observed word ranges by meaning and context,
write timing.json directly, and do not require exact ASR wording or per-cue human approval.
validate --stage timed checks technical bindings/ranges/coverage, not semantic quality.
Trailing silence is valid; use waveform duration. Structural success never grants listening approval.
