"""Small, dependency-free file and identity helpers."""
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def identity(value):
    require(isinstance(value, str) and bool(re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9._-]{0,95}", value)),
            f"Invalid stable ID: {value!r}")
    require(value not in {".", ".."}, "Invalid ID")
    return value


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value, exclusive=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if exclusive:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(serialized)
        return
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(serialized)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def sha256(value):
    if isinstance(value, str):
        value = value.encode("utf-8")
    return hashlib.sha256(value).hexdigest()


def safe_path(base, name):
    base = Path(base).resolve()
    require(isinstance(name, str) and name and not Path(name).is_absolute(), "Expected relative path")
    require(".." not in Path(name).parts, "Parent path rejected")
    path = base / name
    for parent in [path, *path.parents]:
        if parent == base:
            break
        require(not parent.is_symlink(), f"Symlink rejected: {parent}")
    require(path.resolve().is_relative_to(base), "Path escapes its owner folder")
    return path


def lesson_folder(root, course, lesson):
    return safe_path(root, f"curricula/{identity(course)}/lessons/{identity(lesson)}")


def walk_files(folder):
    folder = Path(folder)
    require(not folder.is_symlink(), f"Symlink rejected: {folder}")
    for base, directories, files in os.walk(folder):
        for name in directories + files:
            require(not (Path(base) / name).is_symlink(), f"Symlink rejected: {name}")
        for name in sorted(files):
            if name.endswith(".pyc") or "__pycache__" in Path(base).parts:
                continue
            yield Path(base) / name


def source_hash(folder):
    """Bind editorial review to all lesson inputs, excluding review and status."""
    rows = []
    course_folder = Path(folder).parents[1]
    course = read_json(course_folder / "course.json")
    course_files = [course_folder / "course.json", course_folder / "OUTLINE.md"]
    course_files.extend(safe_path(course_folder, s["file"]) for s in course["sources"] if s.get("file"))
    for path in sorted(set(course_files)):
        require(path.is_file(), f"Missing course input: {path}")
        rows.append(["course/" + path.relative_to(course_folder).as_posix(), sha256(path.read_bytes())])
    for path in sorted(walk_files(folder)):
        relative = path.relative_to(folder).as_posix()
        if relative in {"review.json", "STATUS.md"}:
            continue
        rows.append([relative, sha256(path.read_bytes())])
    return sha256(json.dumps(rows, ensure_ascii=False, separators=(",", ":")))


def clips_for(scenes):
    clips = []
    for scene in scenes:
        clips.append(scene["narration"])
        if scene.get("question"):
            clips.append(scene["question"]["feedback"])
    return clips


def load_lesson(root, course, lesson):
    folder = lesson_folder(root, course, lesson)
    data = read_json(folder / "lesson.json")
    require(isinstance(data, dict) and isinstance(data.get("scenes"), list), "Lesson/scenes shape invalid")
    scenes = [read_json(safe_path(folder, f"scenes/{identity(s)}.json")) for s in data["scenes"]]
    require(all(isinstance(scene, dict) for scene in scenes), "Scene must be an object")
    return folder, data, scenes
