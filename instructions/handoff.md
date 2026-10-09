# Review, collaboration and handoff

Read [human stage gates](stage-gates.md); separate source/scientific, teaching, listening, timing, visual and runtime review.
At **every** stage completion, commit the work on the current scoped branch/PR, update durable curriculum/lesson STATUS with last completed gate, exact artifacts and pending human `next`/comments, then stop. A PR update or CI success does **not** grant permission for the next stage.
Use the [teaching quality gate](teaching.md) before batch audio: document essential concept bridges, bilingual clarity, source limits, independent assessments and unresolved issues.
Use the [lesson-boundary decision workflow](curriculum-planning.md) **before** scene/audio production; record whether the provisional lesson was kept, internally chunked, split, merged or rescoped and why.
Record material self-critique findings and dispositions in STATUS or PR comments. AI self-review and structural validation are not human academic sign-off.
After scene decomposition the spoken source of truth is scene narration/question feedback, not an independently edited master draft.
Defaults are untested. Passed means real reviewer/evidence tied to current sourceHash from validate.
Hash binds course policy/source files and lesson inputs; input edits invalidate review conservatively.
Changes to existing scripts after accepted audio require an explicit rework plan: preserve previous takes/IDs and revalidate affected reviews, clip hashes, timing and export; don't silently move recorded speech between lessons.
Never fill faithful/approved/passed to satisfy a checker. Runtime stays untested until actual playback review.
Bind runtime evidence to the exact SDK version/artifact hash as described in preview-sdk/README.md.
Reconsider the relevant reviews after source, language-policy or script edits; audio changes also invalidate bound timing/listening evidence.

Use curriculum-level branches for initial multi-lesson draft blocks, then lesson-scoped branches/PRs when stabilizing individual lessons; use stable IDs/order from the outline and existing channels for coordination.
If boundaries change, coordinate with the curriculum/outline owner and update OUTLINE objectives, coverage, prerequisites, orders and ID mappings before changing lesson files. Never silently renumber, reuse an issued ID or overwrite another editor's reviewed lesson.
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
