# Human-gated curriculum production: one stage per human turn

**This document controls execution scope, not scientific sign-off or the JSON authoring contract.**
Read with [curriculum planning](curriculum-planning.md), [teaching](teaching.md), [handoff](handoff.md), and the existing [audio](audio.md)/[preview](../preview-sdk/README.md) instructions.
`next` authorizes **only the next editorial/production stage**, never paid synthesis, an academic `passed` review, a merge to `main`, or student publication.

## Default invocation and stop rule

- A new user request like **"عايزين نبدأ إنتاج منهج" + source PDF + repository** means **Stage 01 only**, not the entire production pipeline. Choose a manageable source-grounded chapter/neighboring block; do not ask for an arbitrary lesson count when the source permits a useful start.
- **At the end of every stage** save deliverables to the scoped curriculum branch/draft PR when GitHub write access is authorized, update curriculum or lesson STATUS, report exactly what was completed and what remains unreviewed, and **STOP**. Do not begin the next stage in the same assistant execution, even if time, tools or budget remain.
- On the next human turn, **"next" / "كمل" / "التالي"** with no other instruction means execute **exactly one next numbered stage** for the currently active curriculum/block, then stop again. Re-read current STATUS and files/PR head; don't depend on old chat context.
- A human correction/comment means **revise the current or explicitly named stage**, report changes and stop; it is **not** permission to advance. A request for a particular artifact/stage can narrow scope, but must not silently mark skipped dependencies complete.
- A user may **explicitly** authorize multiple stages in one message; otherwise never infer blanket end-to-end authorization from "ابدأ" or a link. Higher-priority or explicit user scope wins, subject to real prerequisites, review integrity, paid action permission and non-publication boundaries.
- Stop early if the PDF is inaccessible, identity/scope is genuinely unresolved, an owner decision is necessary, or a required artifact is missing. Record the blocker and ask one focused question; do not fill missing source pages with general knowledge.
- Multiple active curricula require identifying the current course/branch from the user turn and STATUS. Never advance a different PR because it looks newer. Treat legacy work as-is; do not retroactively claim earlier gates were approved.

## Numbered gates and deliverables

### 01 — Source, provisional boundaries, **complete continuous drafts**
- Inspect available source pages/coverage; record unavailable parts honestly, audience assumptions, concept/prerequisite map, learner objectives and a **provisional** lesson split.
- Write the **full teachable spoken working draft for every proposed lesson in the selected chapter/neighboring block**: explanations, natural bilingual terminology, examples, independent questions, and **separate post-attempt feedback**, meaningful opening and recap. Do not deliver only outlines, skeletons or scene snippets.
- Keep prose coherent without production scene cuts; natural paragraphs/editorial headings and non-spoken attempt markers are allowed. Do a minimal factual/format sanity check, but **reserve systematic scientific/teaching/cognitive-load critique and rewrite for Stage 02**.
- Save draft text, source review, provisional OUTLINE and STATUS. **Do not** issue new stable lesson IDs, create `lesson.json`/scene JSON/visual modules, run TTS, or decide final lesson boundaries.
- **Stop:** tell the human the drafts/PR are ready to read and ask for comments or `next`.

### 02 — Evidence-led **critique and rewrite** of the complete drafts
- Review the *entire* Stage 01 drafts for novice concept gaps, source/scientific fidelity, bilingual clarity, math/narration, misconceptions, actual question independence, repetition and cognitive load.
- Record specific findings tied to passage/source, fix the text, and check each fix. Recommend possible **keep / internal chunks / split / merge / rescope** decisions, **but do not finalize boundaries or create scenes**.
- Save revised drafts and documented critique as editorial evidence, not false human/academic approval. **Stop** for feedback or `next`.

### 03 — **Boundary decision, rewrite and final scripts**
- Based on Stage 02 evidence, explicitly decide how proposed lessons should be kept, internally chunked, split, merged or rescoped. Never cut one narration mechanically; each resulting lesson needs its own coherent opening, explanation, independent assessment/feedback and recap.
- Map source coverage/prerequisites/objectives without gaps or accidental overlap. Coordinate changes to **already issued** stable IDs or shared OUTLINE with the owner; preserve existing IDs and reviewed work unless the human authorized a controlled change.
- Finalize the source-grounded teaching scripts and OUTLINE/order/IDs **only within authorized scope**, then re-review the resulting lessons. Document decisions, any outstanding owner/teacher review, and what is ready for scene production.
- **Stop** before creating scene JSON. `next` from the user moves to Stage 04, not back through stages already completed.

### 04 — **Scene, question/feedback and visual authoring**
- Convert the finalized lessons to canonical `lesson.json` and `scenes/*.json` according to [contract](contract.md); keep questions, attempts and feedback separate. Preserve spoken wording and traceable source locators; derive a continuous reading copy from scenes if needed.
- Create semantic units, **independent 16:9 and 9:16 storyboards**, and permitted lesson-local bespoke components. Run relevant tests, quality and `validate --stage script` where possible; report actual checks, not fabricated certification.
- No paid audio or timed cue guesses. **Stop** after scene/script handoff.

### 05 — **Audio pilot preparation and separately authorized synthesis**
- Review [audio](audio.md). Prepare a representative bilingual/equation/number pilot and its exact request, initially dry-run. `next` alone **does not authorize a paid send**.
- If the user has explicitly authorized the cost/scope, dispatch the pilot using unique jobs, reconcile delivery, review actual speech and source wording. Otherwise present the pending authorization/blocker and **stop without sending**.
- Never expand a batch solely because pilot preparation succeeded. **Stop** and report audio/listening evidence and remaining blockers.

### 06 — **Timed alignment, visuals, preview and handoff**
- Proceed only with actually delivered, reviewed audio and the relevant authorization for any further paid batch. Follow the timed-media and visual/replay checks; render using the **pinned shared preview SDK** when the dependencies exist.
- Keep runtime, human source/teaching/listening review and publication independently evidenced. Prepare the handoff package only at its validated stage. No automatic merge or student publication.
- **Stop** with actual results, limits and next requested human decision. If Stage 06 is too large for a safe turn, finish a clearly named bounded subtask and **stop** rather than silently skipping a verification gate.

## Durable STATUS checkpoint (Markdown, no schema change)

For every active curriculum/block, place a concise, findable checkpoint in curriculum `STATUS.md` (or lesson `STATUS.md` and linked course STATUS). Suggested fields:

```md
- Scope: <course / chapter or neighboring block / working lesson labels>
- Current branch/PR: <branch, PR number, optional head SHA>
- Last completed human gate: 01 — drafts (or 02/03/04/05/06)
- Next authorized gate: NONE — awaiting human "next" or comments
- Stage outputs: <exact links/paths to sources, full drafts, critique, scenes as applicable>
- Open decisions/blockers: <genuine unknowns, review and cost permissions>
- Checks actually run: <commands/results; leave academic reviews untested without evidence>
```

On a subsequent `next`, first verify the files and the last completed gate in STATUS. Update the checkpoint **only after** successfully completing the requested stage; on interruption record the partial work and remain at that gate. Do not mark a next gate authorized in GitHub simply because the previous gate finished: authorization comes from the next human message.

## Review and acceptance examples

- **New PDF + "ابدأ":** create outline and **full** connected draft(s) for a manageable source block; report and stop at 01. No self-critique gate, no scenes.
- **"جميل، next":** critique/rewrite those drafts, show documented corrections, stop at 02.
- **"عدّل الشرح عن القوة":** revise the relevant current drafts, update STATUS and stop; do **not** treat this as `next`.
- **"next" again:** decide/rewrite boundaries and finalize those lesson scripts; stop at 03.
- **"next" again:** only now author scene JSON/storyboards; stop at 04.
- **"next" at audio pilot:** dry-run preparation is permitted; **paid dispatch requires explicit authorization**.
- **Existing scenes in a legacy PR:** don't erase them or pretend Stage 01 happened with a human gate; assess current artifacts, flag missing steps, and ask for the next intended review action.
