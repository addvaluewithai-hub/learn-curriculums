#!/usr/bin/env python3
"""Validate completed Gemini TTS artifacts; do not certify speech content."""
import argparse
import hashlib
import json
import math
import re
from pathlib import Path
import sys
import wave


def verify(result, transcript, audio, expected_hash=None, expected_job=None):
    errors = []
    warnings = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    def finite(value):
        return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    require(isinstance(result, dict), "result must be an object")
    require(isinstance(transcript, dict), "transcript must be an object")
    if errors:
        return {"valid": False, "structural_valid": False, "publication_approved": False, "errors": errors, "warnings": warnings}
    require(result.get("status") == "completed", "job is not completed")
    require(bool(result.get("id")), "missing job ID")
    if expected_job is not None:
        require(result.get("id") == expected_job, "job ID mismatch")
    for key in ("audio_url", "transcript_url"):
        require(isinstance(result.get(key), str) and result[key].startswith("https://"), f"missing HTTPS {key}")
    summary = result.get("transcript")
    require(isinstance(summary, dict) and summary.get("status") == "completed", "transcript job is not completed")
    summary = summary if isinstance(summary, dict) else {}
    require(transcript.get("schema_version") == 1 and transcript.get("type") == "word_timestamps", "unsupported transcript schema")
    require(bool(transcript.get("alignment_mode")), "missing alignment provenance")
    for key in ("source_text", "recognized_text"):
        require(isinstance(transcript.get(key), str) and bool(transcript[key].strip()), f"missing {key}")
    duration = transcript.get("duration_ms")
    require(finite(duration) and duration > 0, "invalid transcript duration")
    words = transcript.get("words")
    require(isinstance(words, list) and len(words) > 0, "missing timed words")
    words = words if isinstance(words, list) else []
    require(transcript.get("word_count") == len(words), "transcript word count mismatch")
    require(summary.get("word_count") == len(words), "result word count mismatch")
    timed_ends = []
    previous_start = -1
    for index, word in enumerate(words):
        if not isinstance(word, dict):
            errors.append(f"word {index}: not an object")
            continue
        start, end = word.get("start_ms"), word.get("end_ms")
        valid = finite(start) and finite(end) and finite(duration) and 0 <= start < end <= duration
        require(valid, f"word {index}: invalid time bounds")
        if valid:
            require(start >= previous_start, f"word {index}: starts out of order")
            previous_start = start
            timed_ends.append(end)
        require(isinstance(word.get("text"), str) and bool(word["text"].strip()), f"word {index}: missing text")
    sha = hashlib.sha256(Path(audio).read_bytes()).hexdigest()
    if expected_hash is not None:
        require(sha == expected_hash, "audio SHA-256 mismatch; discard stale cues")
    measured = None
    try:
        with wave.open(str(audio), "rb") as wav:
            measured = wav.getnframes() * 1000 / wav.getframerate()
        require(measured > 0, "empty WAV")
        if finite(duration):
            require(duration <= measured + 1, "transcript duration exceeds WAV duration")
            if duration < measured - 250:
                warnings.append("WAV extends beyond transcript duration; use WAV duration for playback, review trailing interval separately")
        for index, word in enumerate(words):
            if isinstance(word, dict) and finite(word.get("end_ms")):
                require(word["end_ms"] <= measured + 1, f"word {index}: exceeds WAV duration")
        reported = summary.get("duration_ms")
        require(finite(reported) and finite(duration) and abs(duration - reported) <= 1, "result/transcript duration mismatch")
    except (wave.Error, EOFError) as exc:
        errors.append(f"invalid WAV: {exc}")
    # A missing recognized term is a coverage warning, never an assertion about speech.
    latin = lambda value: set(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", value.lower())) if isinstance(value, str) else set()
    timed_text = " ".join(w.get("text", "") for w in words if isinstance(w, dict) and isinstance(w.get("text"), str))
    missing = sorted(latin(transcript.get("source_text", "")) - latin(timed_text))
    if missing:
        warnings.append("English source tokens lack timed recognition: " + ", ".join(missing))
    if words and isinstance(words[0], dict) and finite(words[0].get("start_ms")) and words[0]["start_ms"] > 3000:
        warnings.append("No timed words in the opening interval; inspect actual audio, do not assume silence")
    return {"valid": not errors, "structural_valid": not errors, "publication_approved": False,
            "warnings": warnings, "recognized_speech_end_ms": max(timed_ends) if timed_ends else None, "audio_sha256": sha, "measured_duration_ms": measured,
            "word_count": len(words), "alignment_mode": transcript.get("alignment_mode"),
            "semantic_audit": "required separately", "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path)
    parser.add_argument("transcript", type=Path)
    parser.add_argument("audio", type=Path)
    parser.add_argument("--job-id", help="Expected completed job ID")
    parser.add_argument("--sha256", help="Expected exact accepted recording SHA-256")
    args = parser.parse_args()
    try:
        report = verify(json.loads(args.result.read_text()), json.loads(args.transcript.read_text()), args.audio, args.sha256, args.job_id)
    except (OSError, ValueError, TypeError, ZeroDivisionError) as exc:
        report = {"valid": False, "structural_valid": False, "publication_approved": False, "errors": [str(exc)]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
