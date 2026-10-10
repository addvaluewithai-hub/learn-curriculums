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
