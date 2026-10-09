"""Bind declared runtime review to the pinned SDK; not automatic approval."""
import re
from common import read_json, require


def sdk_identity(root):
    path = root / "preview-sdk/sdk-version.json"
    if not path.exists():
        return None
    sdk = read_json(path)
    require(isinstance(sdk.get("version"), str) and re.fullmatch(r"\d+\.\d+\.\d+", sdk["version"]), "Invalid SDK version")
    require(isinstance(sdk.get("sha256"), str) and re.fullmatch(r"[a-f0-9]{64}", sdk["sha256"]), "Invalid SDK artifact hash")
    return sdk


def check_runtime_review(root, check):
    if check["status"] != "passed":
        return False
    sdk = sdk_identity(root)
    require(sdk is not None, "Runtime cannot pass before the preview SDK exists")
    require(check.get("runtimeVersion") == sdk["version"] and check.get("runtimeArtifactHash") == sdk["sha256"],
            "Runtime review references a different SDK edition")
    return True
