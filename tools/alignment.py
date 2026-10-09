"""Preserve reviewed corrected timing without editing factory deliverables."""
import math
from pathlib import Path
from common import load_lesson, clips_for, read_json, require, safe_path, sha256, write_json


def validate_words(data, duration):
    require(data.get("schema_version") == 1 and data.get("type") == "word_timestamps", "Unsupported alignment transcript")
    words = data.get("words")
    require(isinstance(words, list) and words and data.get("word_count") == len(words), "Alignment words/count invalid")
    require(data.get("source_text") and data.get("recognized_text") and data.get("alignment_mode"), "Alignment provenance missing")
    previous = -1
    for word in words:
        start, end = word.get("start_ms"), word.get("end_ms")
        valid = all(type(v) in {int, float} and math.isfinite(v) for v in [start, end])
        require(valid and 0 <= start < end <= duration and start >= previous, "Corrected word bounds/order invalid")
        require(isinstance(word.get("text"), str) and word["text"].strip(), "Corrected word text missing")
        previous = start


def selected_words(folder, clip, receipt, original):
    base = safe_path(folder, f"media/{clip['id']}")
    pointer = base / "alignment.json"
    if not pointer.exists():
        return original, receipt["transcriptHash"]
    alignment = read_json(pointer)
    require(alignment.get("audioHash") == receipt["audioHash"] and alignment.get("scriptHash") == receipt["scriptHash"]
            and alignment.get("sourceTranscriptHash") == receipt["transcriptHash"], "Stale corrected alignment")
    require(alignment.get("reviewer") and alignment.get("evidence"), "Alignment review missing")
    path = safe_path(base, alignment["file"])
    require(sha256(path.read_bytes()) == alignment["transcriptHash"], "Corrected transcript changed")
    transcript = read_json(path)
    validate_words(transcript, receipt["durationMs"])
    return transcript, alignment["transcriptHash"]


def import_alignment(root, course, lesson, clip_id, transcript_path, method, reviewer, evidence):
    from media import check_receipt
    require(method in {"manual-measured-reviewed", "multi-pass-reviewed"}, "Unsupported correction method")
    require(reviewer.strip() and evidence.strip(), "Real listening/alignment review evidence required")
    folder, _, scenes = load_lesson(root, course, lesson)
    clip = next((c for c in clips_for(scenes) if c["id"] == clip_id), None)
    require(clip is not None, "Unknown clip")
    receipt, original = check_receipt(folder, clip)
    transcript = read_json(transcript_path)
    require(transcript.get("source_text") == original["source_text"], "Corrected transcript requested source differs")
    validate_words(transcript, receipt["durationMs"])
    raw = Path(transcript_path).read_bytes()
    digest = sha256(raw)
    base = safe_path(folder, f"media/{clip_id}")
    target = safe_path(base, f"alignments/{digest}.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        require(target.read_bytes() == raw, "Immutable alignment collision")
    else:
        with target.open("xb") as handle:
            handle.write(raw)
    alignment = {"schemaVersion": 1, "audioHash": receipt["audioHash"], "scriptHash": receipt["scriptHash"],
                 "sourceTranscriptHash": receipt["transcriptHash"], "transcriptHash": digest,
                 "method": method, "reviewer": reviewer, "evidence": evidence,
                 "file": target.relative_to(base).as_posix(), "publicationApproved": False}
    write_json(base / "alignment.json", alignment)
    return alignment
