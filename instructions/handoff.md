# Review, collaboration and handoff

Separate source/scientific, teaching, listening, timing, visual and runtime review.
Defaults are untested. Passed means real reviewer/evidence tied to current sourceHash from validate.
Hash binds course policy/source files and lesson inputs; input edits invalidate review conservatively.
Never fill faithful/approved/passed to satisfy a checker. Runtime stays untested until SDK exists.

Use lesson branches/PRs, stable IDs/order from the outline and existing channels for coordination.
No shared hardcoded registry edits per lesson. STATUS records date/editor/scope/files/checks/limits/next action.
GitHub PR review holds comments; no new admin app/database.

```bash
python3 tools/cli.py export --course COURSE --stage script
```

Export copies the entire course/assets/media with hashed manifest under dist/handoff.
Use actual passed stage; draft/script exports are useful early handoffs.
Keep generated output out of Git; version sources and evidence in Git.
Platform must validate, build via compatible SDK, review playback, retain files, import a draft, then explicitly release.
That importer is not implemented here; do not copy source into platform src and create another player.
With SDK check both ratios, question onset/no leaked answer, submit/feedback/next, pause/replay/seek and errors.
Student ownership/persistence belong to platform acceptance, not ordinary preview.
Published corrections create immutable new editions; no changing existing release files.
Report actual stage and unresolved checks; script, audio, preview and release are different milestones.
