#!/usr/bin/env python3
"""Production commands; no SDK, login, database or paid call by default."""
import argparse
import json
import subprocess
import sys
from common import ROOT
from scaffold import new_course, new_lesson
from validate import STAGES, validate_all, validate_lesson
from audio import collect, dispatch, prepare
from handoff import export_course
from alignment import import_alignment


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    course = commands.add_parser("course-new")
    course.add_argument("--id", required=True)
    course.add_argument("--title", required=True)
    lesson = commands.add_parser("lesson-new")
    lesson.add_argument("--course", required=True)
    lesson.add_argument("--id", required=True)
    lesson.add_argument("--order", required=True, type=int)
    lesson.add_argument("--title", required=True)
    validate = commands.add_parser("validate")
    validate.add_argument("--course")
    validate.add_argument("--lesson")
    validate.add_argument("--stage", choices=STAGES, default="draft")
    audio = commands.add_parser("audio-prepare")
    for key in ("course", "lesson", "clip", "take"):
        audio.add_argument("--" + key, required=True)
    send = commands.add_parser("audio-dispatch")
    send.add_argument("--job", required=True)
    send.add_argument("--send", action="store_true")
    delivered = commands.add_parser("audio-collect")
    for key in ("job", "result"):
        delivered.add_argument("--" + key, required=True)
    delivered.add_argument("--audio")
    delivered.add_argument("--transcript")
    delivered.add_argument("--select-new-take", action="store_true")
    aligned = commands.add_parser("audio-align")
    for key in ("course", "lesson", "clip", "transcript", "reviewer", "evidence"):
        aligned.add_argument("--" + key, required=True)
    aligned.add_argument("--method", choices=("manual-measured-reviewed", "multi-pass-reviewed"), required=True)
    export = commands.add_parser("export")
    export.add_argument("--course", required=True)
    export.add_argument("--stage", choices=STAGES, default="draft")
    args = parser.parse_args()
    try:
        if args.command == "course-new":
            result = str(new_course(ROOT, args.id, args.title).relative_to(ROOT))
        elif args.command == "lesson-new":
            result = str(new_lesson(ROOT, args.course, args.id, args.order, args.title).relative_to(ROOT))
        elif args.command == "validate":
            if bool(args.course) != bool(args.lesson):
                raise ValueError("Pass both --course and --lesson, or neither")
            result = (validate_lesson(ROOT, args.course, args.lesson, args.stage)
                      if args.lesson else validate_all(ROOT, args.stage))
        elif args.command == "audio-prepare":
            result = str(prepare(ROOT, args.course, args.lesson, args.clip, args.take).relative_to(ROOT))
        elif args.command == "audio-dispatch":
            result = dispatch(ROOT, args.job, args.send)
        elif args.command == "audio-collect":
            result = collect(ROOT, args.job, args.result, args.audio, args.transcript, args.select_new_take)
        elif args.command == "audio-align":
            result = import_alignment(ROOT, args.course, args.lesson, args.clip, args.transcript,
                                      args.method, args.reviewer, args.evidence)
        else:
            result = str(export_course(ROOT, args.course, args.stage).relative_to(ROOT))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError, StopIteration) as error:
        print(json.dumps({"valid": False, "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
