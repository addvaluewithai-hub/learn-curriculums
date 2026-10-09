"""Enforce size and skill links without requiring a preview build."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SUFFIXES = {".py", ".ts", ".tsx", ".js", ".mjs", ".css", ".md", ".json", ".yaml", ".yml"}
IGNORED = {".git", "dist", "node_modules", "__pycache__", ".venv", "media", "jobs"}


def check():
    errors = []
    for path in ROOT.rglob("*"):
        if any(part in IGNORED for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file() and path.suffix in SUFFIXES:
            if len(path.read_text().splitlines()) > 300:
                errors.append(f"Over 300 lines: {path.relative_to(ROOT)}")
    skill = ROOT / ".agents/skills/produce-learn-lesson/SKILL.md"
    value = skill.read_text()
    if not value.startswith("---\nname: produce-learn-lesson\ndescription:"):
        errors.append("Skill frontmatter invalid")
    for target in re.findall(r"\]\(([^)]+)\)", value):
        if not target.startswith("https://") and not (skill.parent / target).resolve().is_file():
            errors.append(f"Broken skill reference: {target}")
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Quality: {'failed' if errors else 'passed'}")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check())
