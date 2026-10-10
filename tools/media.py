"""Verify accepted WAV receipts and evidence-bound visual cue anchors."""
import math
import re
from common import read_json, require, safe_path, sha256
from verify_delivery import verify


def check_receipt(folder, clip):
    base = safe_path(folder, "media/" + clip["id"])
    receipt = read_json(base / "receipt.json")
    require(receipt.get("schemaVersion") == 1 and receipt.get("clipId") == clip["id"], "Receipt identity mismatch")
    require(receipt.get("scriptHash") == sha256(clip["script"]), "Stale audio: script changed")
    files = receipt["files"]
    result = read_json(safe_path(base, files["result"]))
    transcript = read_json(safe_path(base, files["transcript"]))
    audio = safe_path(base, files["audio"])
    report = verify(result, transcript, audio, receipt["audioHash"], receipt["jobId"])
    require(report["valid"], "Invalid delivered recording: " + "; ".join(report["errors"]))
    require(receipt.get("transcriptHash") == sha256(safe_path(base, files["transcript"]).read_bytes()),
            "Transcript changed since delivery verification")
    require(abs(receipt["durationMs"] - report["measured_duration_ms"]) < .01, "Wrong waveform duration")
    require(result.get("metadata", {}).get("scriptHash") == receipt["scriptHash"], "Result/script provenance mismatch")
    return receipt, transcript


def tokens(value):
    return re.findall(r"[^\W_]+", value.casefold(), flags=re.UNICODE)


def check_timing(folder, clip):
    receipt, transcript = check_receipt(folder, clip)
    from alignment import selected_words
    transcript, transcript_hash = selected_words(folder, clip, receipt, transcript)
    timing = read_json(safe_path(folder, f"media/{clip['id']}/timing.json"))
    require(timing.get("audioHash") == receipt["audioHash"] and timing.get("scriptHash") == receipt["scriptHash"],
            "Stale cue bindings")
    require(timing.get("transcriptHash") == transcript_hash, "Cues reference a different transcript")
    semantic = timing.get("method") == "semantic-word-anchors"
    require(semantic or timing.get("method") in {"word-anchors-reviewed", "multi-pass-reviewed"},
            "Unsupported cue method")
    if semantic:
        require(isinstance(timing.get("author"), str) and timing["author"].strip(), "Cue author missing")
    else:
        require(timing.get("reviewer") and timing.get("evidence"), "Cue review evidence missing")
    cues = timing.get("cues")
    require(isinstance(cues, list) and all(isinstance(c, dict) and isinstance(c.get("unitId"), str)
                                         for c in cues), "Cue list missing or malformed")
    require(len(cues) == len({c["unitId"] for c in cues}), "Duplicate cue unit")
    require({c["unitId"] for c in cues} == {u["id"] for u in clip["units"]}, "Cue coverage incomplete")
    words = transcript["words"]
    for unit in clip["units"]:
        cue = next(c for c in cues if c["unitId"] == unit["id"])
        first, last = cue.get("wordStart"), cue.get("wordEnd")
        require(type(first) is int and type(last) is int and 0 <= first <= last < len(words), "Cue word range invalid")
        at = cue.get("atMs")
        require(type(at) in {int, float} and math.isfinite(at) and 0 <= at < receipt["durationMs"],
                "Cue time outside recording")
        require(cue.get("atMs") == words[first]["start_ms"], "Cue time is not its first spoken word")
        if semantic:
            require(isinstance(cue.get("reason"), str) and cue["reason"].strip(), "Semantic cue reason missing")
        # The author selects meaning/occurrence using context. ASR spelling equality
        # is neither a timing decision nor a proof of visual/educational quality.
    return timing
