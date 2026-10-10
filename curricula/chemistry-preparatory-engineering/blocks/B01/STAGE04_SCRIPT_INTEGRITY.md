# B01 Stage 04 — conversion audit (editorial, no playback)

- Conversion preserves **all normalized spoken paragraphs** of the Stage 03 scripts, in order, as canonical scene teaching narration / question clips / post-attempt feedback. Non-spoken titles, notes and markdown formatting are intentionally excluded. There is **no separate actively edited master script** after conversion. Stage 03 text snapshots are archived/historical only.
- Conversion tooling within this authoring turn compared the section speech sequence against concatenated canonical outputs: **identical** (after removing nonspoken headings, metadata and Markdown emphasis/backticks).
- Scene totals: **18 scenes**, **7 independent questions**, **25 narration/feedback clips**, no audio/timing assets.
- IDs and order preserved: 1 `chem1-states-phase-changes`; 2 `chem1-boyle-law`; 3 `chem1-charles-law`. Questions/feedback maintain Q01–Q03/F01–F03 per lesson.
- Each scene has one source locator, semantic phrase anchors (no fabricated milliseconds), and independent 16:9/9:16 storyboard descriptions. Every question has separate full English/Arabic phrase units with explicit reading IDs, model-answer units and written learner attempt.
- Each lesson has local draft React board code that uses the pinned SDK component interface; **no claim of mounted playback**. The boards are creative authoring sketches; actual responsive rendering, cue timing, spoken language and submit/feedback/seek behavior require media/timed stage and human review.
- All formal review statuses explicitly `untested` without sourceHash/reviewer/evidence. Original scan is **not** uploaded to this public repo.
- Source discrepancies remain nonspoken editorial records: condensation direction printed p9; Boyle worked answer printed p12; worksheet conditions Q5/7/8 author-adapted; CO₂ sig figures.
- Coverage from user source extends only to printed p36, not later full chapters. Safe future source access and copyright permissions remain blockers.
- Relevant actual GitHub Actions / script validation results must be recorded from real checks; these structural authoring assertions **alone are not** the `python3 tools/cli.py validate ... --stage script` result.

## Per-lesson conversion
- **chem1-states-phase-changes** — 5 scenes (3 teaching, 2 question), 7 clips; parity exact; objectives O1 -> S01 / Q01; O2 -> S03,S05 / Q02.
- **chem1-boyle-law** — 6 scenes (4 teaching, 2 question), 8 clips; parity exact; objectives O1 -> S01,S02,S03,S06 / Q01; O2 -> S01 / Q02.
- **chem1-charles-law** — 7 scenes (4 teaching, 3 question), 10 clips; parity exact; objectives O1 -> S01,S02,S07 / Q01; O2 -> S04,S07 / Q02; O3 -> S01,S04,S07 / Q03.

## Stage 04 scoped QA / pinned SDK scope

- `tests/test_chemistry_b01_script.py` calls **the real** `validate_lesson(ROOT, course, id, "script")` for all three IDs in GitHub Actions, rather than relying on default `draft` validation. Prior targeted test commit `a026040c06ae01ee97cb578e8afdce568b522db2` completed the repository workflow with success; the latest final authoring commit's CI must still be checked before claiming that revision passed.
- All 18 scenes now include explicit `visual.params.anchors` matching the actual narration `units[].id`, with one anchor per spoken paragraph. Question reading uses full `UEN/UAR`; post-attempt feedback uses full `AEN/AAR`, and an explicit **feedback-phase** local renderer. No timestamps were estimated.
- The visual components have scene-specific modes: states versus transitions; Boyle pistons, reciprocal graphs and examples; Charles piston, Kelvin and rearrangement. Per-scene 16:9 and 9:16 storyboards are independently stated. Actual SDK playback, visual clipping, layout correctness on devices, reduced motion, audio and user flow must be reviewed **only after real media**.
- Source preservation: `blocks/B01/final-scripts/*.md` are **historical editorial snapshots only**. `lessons/*/scenes/*.json` teaching/questions/feedback are canonical from this stage forward. Do not hand-edit both.
- Human academic reviews still **untested**; schema/CI validation cannot approve accuracy, copyright permission or student release.
