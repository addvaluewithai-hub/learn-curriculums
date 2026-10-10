# Course STATUS — First-Year Engineering Chemistry

- **Date:** 2026-10-10; ID `chemistry-preparatory-engineering`. Audience: **طلبة سنة أولى هندسة**. Original book bibliographic title unchanged.
- **Active Block:** B01; **last completed human authoring stage: Stage 04** (canonical scene decomposition and independent responsive storyboard/React sketches); awaiting next human decision. B02–B09 are provisional.
- **Stable lessons and order:** `chem1-states-phase-changes` (1), `chem1-boyle-law` (2), `chem1-charles-law` (3). See OUTLINE.
- **Actual artifacts:** 3 `lessons/<id>/lesson.json`, 18 `scenes/Snn.json`, 3 local React boards, 3 `review.json` statuses all untested, 3 lesson STATUS; 7 question scenes + 7 isolated feedback clips = 25 speech clips. Source-to-script parity recorded in `blocks/B01/STAGE04_SCRIPT_INTEGRITY.md`.
- **Canonical text:** `lessons/<id>/scenes/*.json` narration & feedback. Stage 03 `blocks/B01/final-scripts/*.md` are archival snapshots and MUST NOT be independently edited.
- **Validation:** repo CI contains a scoped test that runs actual `validate_lesson(...,"script")` on all three lessons plus repository quality/tests. Intermediate workflow SHA `a026040c06ae01ee97cb578e8afdce568b522db2` reported success; *latest revision workflow result is tracked separately, do not misstate it*. Real audio, timed and browser runtime reviews **not performed**.
- **Source:** user-provided scanned PDF 20 pages, hash `c16cf18739edc03529c002bd921e9772917c42049932fa34cb6501fd10b9367c`. Visible body ends printed p36; B01 printed pp6–17 used. Rights/private durable source access and Drive sharing controls unresolved. No scanned original in public repo.
- **Known scientific/worksheet caveats:** Condensation book p9 arrow direction wrong; Boyle book p12 numerical result wrong; conditions explicitly added to adapted Sheet 1 p17 questions #5/#7/#8. Human scientific and teaching sign-off still needed.
- **Blocked until later stages:** paid TTS, actual audio, timestamps, preview playback, student release, database writes and GitHub merge. Script structure does not imply content approved.
- **Draft review:** `curriculum/chemistry-prep-stage00`, Draft PR #11, main untouched.
- **Next choices after Stage 04:** `next` = B01 Stage 05 **audio pilot dry-run only** (paid dispatch needs separate explicit approval); `next block` = B02 Stage 01 authoring (audio B01 deferred). Both require a new human message. **STOP**.
