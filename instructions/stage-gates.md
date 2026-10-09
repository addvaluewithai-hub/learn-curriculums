# Human-gated curriculum production: intake once, blocks repeatedly

This is **one authorized stage per human turn**. It does not change runtime JSON schemas or authorize paid TTS, scientific sign-off, GitHub merge or student release. Read [source handling](source-handling.md), [curriculum planning](curriculum-planning.md), [teaching](teaching.md), [handoff](handoff.md), [audio](audio.md) and [shared preview](../preview-sdk/README.md).

## Invocation and scope

- **New curriculum + PDF + "ابدأ" means Stage 00 only**, not a whole-book draft. At completion save planning artifacts in a curriculum-scoped branch/draft PR, update STATUS and **STOP** for a human `next`.
- **Stage 00 runs once for the curriculum**; Stages 01–04 repeat for each selected **Block**. A Block is a bounded source-grounded group of related outcomes, not automatically a textbook chapter, student lesson, or fixed page/word count. One Block may yield several lessons.
- **`next` / `كمل`** executes exactly **one following stage** in the active scope, saves artifacts, reports, **STOP**. A comment/correction revises the current stage, then stops. Explicitly requested multi-stage work may narrow/override the default within real permissions and prerequisites.
- After Stage 00, `next` starts **B01 Stage 01**. Within a block successive `next` commands run 02, 03, 04, then 05 (audio pilot) and 06 (timed preview/handoff) only with prerequisites satisfied.
- **`next block` / `الجزء اللي بعده`** is a distinct human authorization: after Stage 04 has produced scenes, actual script checks are recorded and the human accepts moving on, begin **Stage 01** of the next source-grounded block. Don't redo Stage 00. Prior Block audio may remain deferred; continuing authoring is **not** human scientific approval or release.
- A bare `next` after Stage 04 refers to the **current Block's Stage 05**; `next block` starts the following Block instead. If the active course/Block is genuinely ambiguous, ask one question before modifying another editor's work.
- Never advance on the same turn, even with available time. Incomplete work stays at its current stage; no invented approvals, falsely completed source retention, paid requests, audio/timings or runtime reviews.

## Stage 00 — Curriculum intake and master roadmap (one-time)

1. Identify the source files, title/edition, audience/language assumptions and **exact available coverage**. Inspect cover, contents and accessible body sufficiently to plan; for large scans, index in bounded passes and mark unopened/unreadable or index-only pages honestly.
2. Follow [source handling](source-handling.md). **This repository is public**: do not commit a scanned copyrighted/private original by default. Preserve the original in approved durable/private storage **only if actually possible and authorized**; verify retrieval by a future authorized agent. If not possible, record the blocker and ask for a suitable location/permission rather than pretend a chat attachment is durable.
3. Create `course.json`, curriculum `OUTLINE.md` (provisional **whole-course** topic/dependency/Block roadmap), `references/SOURCE_MANIFEST.md` (version, locator, rights, storage, hash if measured), and `references/SOURCE_COVERAGE.md` (PDF/printed pages and inspected/index-only/missing). No detailed lessons from unseen chapters.
4. Choose **B01**, a manageable connected set of outcomes/pages, and justify why its boundary makes teaching sense; create curriculum `STATUS.md` plus `blocks/B01/STATUS.md`. Do **not** author lesson scripts, issue stable lesson IDs, create scenes or make audio.
5. Commit to a scoped draft PR when authorized, report coverage and storage limitations, master roadmap and B01, **STOP**.

## Stage 01 — Complete continuous scripts for ONE selected Block

- Reopen actual Bxx source pages. Previous-chat summaries/`reviewed-notes` alone do not prove access. If source bytes are unavailable, stop and request them before inventing detail.
- Build a detailed prerequisite/concept map and provisional **within-Block** lesson grouping. Write a **complete speakable master draft** for every proposed lesson in this Block: natural explanations, examples, English terminology with Arabic contextual support, independent learner attempts and **separate post-attempt feedback**, coherent recap. No scenes and no drafts for the whole book.
- Basic source/format sanity check, but defer structured teaching/science/cognitive-load critique to Stage 02. Save drafts and Block STATUS, **STOP**.

## Stage 02 — Critique and rewrite the complete Block drafts

- Review actual novice gaps, accuracy/source boundaries, maths/units, bilingual speech, question independence, misconceptions, length, cognitive load and transfer. Cite problematic passages and make revisions.
- Recommend keep/internal parts/split/merge/defer, **without finalizing lesson boundaries or scenes**. Record findings and fixes; **STOP**.

## Stage 03 — Confirm lesson boundaries and final scripts for this Block

- Based on critique, keep/chunk/split/merge or rescope. Rewrite complete openings, transitions, practice, questions, feedback and recaps for **each resulting lesson**; never mechanically cut a long transcript.
- Reconcile course coverage and prerequisites with adjacent blocks; finalize appropriate lesson IDs/orders/locators in OUTLINE without silently changing issued IDs. Record needed independent human academic review; **STOP**.

## Stage 04 — Scenes, storyboards, and human authoring checkpoint

- Convert the settled scripts into canonical `lesson.json`, `scenes/*.json`, separate questions/feedback, semantic anchors, and independent 16:9/9:16 storyboards and components. Run actual Stage `script` validation and quality checks where available; report exact results.
- Keep source/teaching reviews `untested` unless supported by genuine reviewer/evidence. Save Block + course STATUS. Offer two explicit choices: **`next`** for this Block's Stage 05 pilot preparation; **`next block`** to author the next Block after human inspection, **without requiring audio**. **STOP**.

## Stage 05 — Optional paid-audio pilot gate

- Prepare a representative bilingual/value/equation TTS pilot with the real [audio](audio.md) process, initially dry-run. `next` alone never authorizes paid dispatch; a separately explicit approval is required. Review delivered audio before any separately approved batch; **STOP**.

## Stage 06 — Optional timing, pinned preview and handoff

- Only with real verified recordings and correct prerequisites: align real word timings, build visuals, test both layouts and interaction with the **pinned shared SDK** and bind review evidence to actual hashes. Export at achieved stage, without student publication. **STOP**.

## Durable STATUS state: global control plane and per-Block progress

- `curricula/<course>/STATUS.md` owns **whole-course plan**, source version/access, roadmap of B01/B02/…, **active Block**, completed/deferred stages, branch/PR and next human decision.
- `curricula/<course>/blocks/B01/STATUS.md` (similarly B02…) owns **that Block's** last fully completed Stage 01–06, draft/scene paths, source page locators, provisional vs stable lesson IDs, actual test results, blockers, pending independent reviews and `awaiting human next`. Stage 00 initializes B01 as planned, not as completed Stage 01.
- Stage gate and active Block are independently tracked. On resuming `next`, first verify the actual branch, source accessibility and two STATUS files; advance only **after** the stage really succeeds. If interrupted record partial work without advancing.
- On `next block` after Stage 04, record the previous Block as `editorial scripts/scenes ready; audio and human checks deferred` where applicable — **not fully approved**. Activate the next bounded available-source Block at Stage 01, preserve historical files/takes/IDs and continue revising the course roadmap only with traceable changes.
- If the original edition/hash changes, stop and reassess the manifest, dependent teaching, audio hashes and reviews; preserve immutable published editions. Never treat an AI self-critique or CI pass as a human sign-off.

## Smoke-test sequence

- New PDF + `ابدأ` → **Stage 00 roadmap/source manifest, no script**, STOP.
- `next` → **B01 full spoken drafts only**, STOP.
- `next` → **B01 critique and rewrite**, STOP.
- `next` → **B01 boundary decision and final scripts**, STOP.
- `next` → **B01 scenes and storyboards**, STOP.
- `next block` → **B02 spoken drafts**, even if B01 audio is deferred; alternatively `next` → B01 pilot preparation.
