"""Discover production folders and generate an isolated ephemeral preview."""
import argparse
import json
import os
from pathlib import Path
import shutil
import tempfile
from common import ROOT, read_json, require, safe_path, source_hash, write_json
from preview_package import adapt_lesson


def prepare_preview(root=ROOT, preview=None):
    root = Path(root).resolve()
    preview = Path(preview or ROOT / "preview-sdk").resolve()
    dependency = read_json(preview / "sdk-version.json")
    output = preview / ".generated"
    entries, imports = [], {}
    with tempfile.TemporaryDirectory(prefix=".prepare-", dir=preview) as temporary:
        incoming = Path(temporary)
        public = incoming / "public"
        public.mkdir()
        for course_file in sorted((root / "curricula").glob("*/course.json")):
            for lesson_file in sorted((course_file.parent / "lessons").glob("*/lesson.json")):
                course_id, lesson_id = course_file.parent.name, lesson_file.parent.name
                entry = {"key": f"{course_id}/{lesson_id}", "curriculumId": course_id, "lessonId": lesson_id}
                try:
                    lesson = read_json(lesson_file)
                    entry.update(title=lesson.get("title", lesson_id), order=lesson.get("order", 0))
                    package, modules, provenance = adapt_lesson(root, course_id, lesson_id, public, dependency["version"])
                    provenance["runtimeArtifactHash"] = dependency["sha256"]
                    require(source_hash(lesson_file.parent) == provenance["sourceHash"], "Source changed during preparation; retry")
                    url = f"/packages/{course_id}/{lesson_id}.json"
                    write_json(public / url.lstrip("/"), {"lesson": package, "provenance": provenance})
                    entry.update(ready=True, packageUrl=url, renderers=list(modules))
                    for renderer, module in modules.items():
                        key = entry["key"] + ":" + renderer
                        imports[key] = os.path.relpath(module, output).replace(os.sep, "/")
                except (ValueError, KeyError, TypeError, OSError) as error:
                    entry.update(ready=False, blocker=str(error))
                entries.append(entry)
        write_json(incoming / "catalog.json", {"sdk": dependency, "entries": entries})
        lines = ["// Generated from local reviewed production paths, not remote executable URLs.", "export const moduleLoaders = {"]
        lines.extend(f"  {json.dumps(key)}: () => import({json.dumps(path)})," for key, path in imports.items())
        lines.append("};\n")
        (incoming / "modules.ts").write_text("\n".join(lines))
        # A failed preparation never leaves last run's packages available.
        if output.exists():
            shutil.rmtree(output)
        shutil.copytree(incoming, output)
    return {"lessons": len(entries), "ready": sum(e["ready"] for e in entries), "output": str(output)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(prepare_preview(args.root), ensure_ascii=False))
