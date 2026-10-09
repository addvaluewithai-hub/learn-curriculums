"""Prepare an immutable request and dispatch only on an explicit --send."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import urllib.request
from uuid import uuid4
from common import clips_for, identity, load_lesson, read_json, require, safe_path, sha256, write_json
from validate import validate_lesson
from verify_delivery import verify


def prepare(root, course, lesson, clip_id, take):
    validate_lesson(root, course, lesson, "script")
    folder, _, scenes = load_lesson(root, course, lesson)
    clips = {c["id"]: c for c in clips_for(scenes)}
    require(clip_id in clips, "Unknown clip")
    clip = clips[clip_id]
    config = read_json(root / "production.json")["audio"]
    teacher = read_json(folder.parents[1] / "course.json").get("teacher", {})
    script_hash = sha256(clip["script"])
    job_id = f"{lesson[:40]}-{identity(clip_id)[:20]}-{identity(take)[:16]}-{uuid4().hex}"
    payload = {"event_type": "tts.generate", "client_payload": {
        "job_id": job_id, "request": {
            "text": clip["script"], "voice": teacher.get("voice", config["voice"]),
            "style": teacher.get("style", config["style"]), "routing": config["routing"],
            "format": "wav", "sample_rate": config["sampleRate"],
            "transcript": {"language_codes": teacher.get("languageCodes", config["languageCodes"]), "write_vtt": True},
            "metadata": {"curriculumId": course, "lessonId": lesson, "clipId": clip_id,
                         "role": clip["role"], "scriptHash": script_hash},
        }}}
    path = safe_path(folder, f"jobs/{job_id}.json")
    write_json(path, payload, exclusive=True)
    return path


def job_for(root, job_path):
    path = safe_path(root, job_path)
    job = read_json(path)
    require(job.get("event_type") == "tts.generate", "Unsupported dispatch event")
    payload = job["client_payload"]
    meta = payload["request"]["metadata"]
    folder, _, scenes = load_lesson(root, meta["curriculumId"], meta["lessonId"])
    require(path.is_relative_to(folder / "jobs"), "Job must belong to the target lesson")
    clip = next((c for c in clips_for(scenes) if c["id"] == meta["clipId"]), None)
    require(clip is not None and meta.get("scriptHash") == sha256(clip["script"]), "Stale audio request")
    require(payload["request"]["text"] == clip["script"], "Request/script mismatch")
    require(payload["request"].get("format") == "wav", "Production delivery requires WAV")
    return path, job, folder, clip


def dispatch(root, job_path, send=False):
    path, job, _, _ = job_for(root, job_path)
    repository = read_json(root / "production.json")["audio"]["repository"]
    if not send:
        return {"status": "dry-run", "jobId": job["client_payload"]["job_id"], "repository": repository,
                "paidCall": False, "payload": str(path.relative_to(root))}
    require(shutil.which("gh"), "Install and authenticate GitHub CLI, or dispatch the saved payload with your authorized GitHub connector")
    receipt = path.with_suffix(".dispatch.json")
    require(not receipt.exists(), "Already dispatched; inspect the existing job before retrying")
    write_json(receipt, {"status": "dispatch-started-outcome-unknown", "jobId": job["client_payload"]["job_id"]}, exclusive=True)
    subprocess.run(["gh", "api", "--method", "POST", f"repos/{repository}/dispatches", "--input", str(path)], check=True)
    report = {"status": "accepted-not-delivered", "jobId": job["client_payload"]["job_id"],
              "repository": repository, "at": datetime.now(timezone.utc).isoformat()}
    write_json(receipt, report)
    return report


def download(url, path, maximum):
    require(isinstance(url, str) and url.startswith("https://"), "Expected HTTPS delivery URL")
    with urllib.request.urlopen(url, timeout=60) as response:
        require(response.url.startswith("https://"), "Insecure delivery redirect rejected")
        data = response.read(maximum + 1)
    require(len(data) <= maximum, "Delivery exceeds supported size")
    path.write_bytes(data)


def collect(root, job_path, result_path, audio_path=None, transcript_path=None, select_new=False):
    _, job, folder, clip = job_for(root, job_path)
    result = read_json(result_path)
    job_id = job["client_payload"]["job_id"]
    require(result.get("id") == job_id and result.get("status") == "completed", "Wrong/incomplete job result")
    script_hash = sha256(clip["script"])
    require(result.get("metadata", {}).get("scriptHash") == script_hash, "Result script provenance mismatch")
    base = safe_path(folder, f"media/{clip['id']}")
    base.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".delivery-", dir=base) as temporary:
        incoming = Path(temporary)
        for source, key, name, maximum in ((audio_path, "audio_url", "audio.wav", 200_000_000),
                                           (transcript_path, "transcript_url", "transcript.json", 20_000_000)):
            if source:
                shutil.copyfile(source, incoming / name)
            else:
                download(result[key], incoming / name, maximum)
        write_json(incoming / "result.json", result)
        transcript = read_json(incoming / "transcript.json")
        report = verify(result, transcript, incoming / "audio.wav", expected_job=job_id)
        require(report["valid"], "Delivery invalid: " + "; ".join(report["errors"]))
        require(transcript["source_text"].strip() == clip["script"].strip(),
                "Delivered source_text differs; inspect normalization or the actual requested script")
        write_json(incoming / "verification.json", report)
        receipt = {"schemaVersion": 1, "clipId": clip["id"], "jobId": job_id,
                   "scriptHash": script_hash, "audioHash": report["audio_sha256"],
                   "transcriptHash": sha256((incoming / "transcript.json").read_bytes()),
                   "durationMs": report["measured_duration_ms"],
                   "files": {key: f"takes/{job_id}/{name}" for key, name in
                             (("audio", "audio.wav"), ("transcript", "transcript.json"), ("result", "result.json"))}}
        selected = base / "receipt.json"
        if selected.exists():
            previous = read_json(selected)
            require(previous == receipt or select_new, "Different take already selected; use --select-new-take deliberately")
        target = safe_path(base, f"takes/{job_id}")
        if target.exists():
            for file in incoming.iterdir():
                require((target / file.name).read_bytes() == file.read_bytes(), "Same job ID has different bytes; immutable take collision")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            os.rename(incoming, target)
        write_json(selected, receipt)
    return {"status": "delivered-structure-verified", "publicationApproved": False, "receipt": str(selected.relative_to(root)),
            "warnings": report["warnings"], "audioHash": receipt["audioHash"], "durationMs": receipt["durationMs"]}
