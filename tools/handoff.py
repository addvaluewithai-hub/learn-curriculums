"""Export complete authoring sources; never pretend this is a runtime release."""
import json
import os
from pathlib import Path
import shutil
import tempfile
from common import identity, read_json, require, safe_path, sha256, walk_files, write_json
from validate import validate_curriculum


def export_course(root, course_id, stage="draft"):
    folder = safe_path(root, "curricula/" + identity(course_id))
    require(folder.is_dir(), "Unknown curriculum")
    reports = validate_curriculum(root, course_id, stage)
    require(reports, "Curriculum has no lessons")
    files = [{"path": p.relative_to(folder).as_posix(), "sha256": sha256(p.read_bytes()), "bytes": p.stat().st_size}
             for p in sorted(walk_files(folder))]
    digest = sha256(json.dumps({"files": files, "stage": stage}, sort_keys=True, separators=(",", ":")))
    output = safe_path(root, f"dist/handoff/{course_id}/{digest}")
    if output.exists():
        manifest = read_json(output / "handoff.json")
        require(manifest["files"] == files, "Handoff identity collision")
        for file in files:
            require(sha256(safe_path(output / "source", file["path"]).read_bytes()) == file["sha256"], "Existing handoff modified")
        return output
    output.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schemaVersion": 1, "kind": "learn-authoring-handoff", "curriculumId": course_id,
        "sourceDigest": digest, "validatedStage": stage, "files": files, "lessons": reports,
        "preview": "pending-sdk", "runtimeVersion": None, "runtimeVerified": False,
        "publicationApproved": False,
        "nextStep": "Review sources/media/cues; build with the shared SDK when available; platform import and publication are separate.",
    }
    with tempfile.TemporaryDirectory(prefix=".export-", dir=output.parent) as temporary:
        incoming = Path(temporary) / "bundle"
        shutil.copytree(folder, incoming / "source")
        for file in files:
            require(sha256(safe_path(incoming / "source", file["path"]).read_bytes()) == file["sha256"],
                    "Source changed during export; retry from a stable checkout")
        write_json(incoming / "handoff.json", manifest)
        os.rename(incoming, output)
    return output
