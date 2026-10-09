---
name: produce-learn-lesson
description: Author or repair source-grounded Learn curricula and lessons in learn-curriculums. Use for produce lesson 3, curriculum scripts, storyboard, custom React scenes, Gemini TTS, word timestamps, semantic cue alignment, shared SDK preview and production handoff. Student publication is a separate platform service.
---

# Produce a Learn lesson

Read root AGENTS.md and **[human stage gates](../../../instructions/stage-gates.md) first**; then the selected course.json, OUTLINE.md, sources and STATUS.md when they exist.
Treat a new general production request as **Stage 00 only**, not script writing: verify source/rights/access per [source handling](../../../instructions/source-handling.md), build a high-level whole-course roadmap, choose B01, save and STOP. A bare human `next` advances one gate of the active Block; `next block` begins Stage 01 of the next Block only after Stage 04 inspection. At each handoff save STATUS, report and STOP; comments revise instead of advancing.
Resolve the requested ordinal to a stable ID; ask only when the course is genuinely ambiguous.
Use [the data contract](../../../instructions/contract.md) before creating or changing files.
Read [curriculum planning](../../../instructions/curriculum-planning.md) before setting or revising boundaries; an outline split is provisional until teaching critique.
Preserve another editor's work and accepted takes; scope changes to the selected course/lesson.

Read [teaching](../../../instructions/teaching.md) and map audience, source boundaries, objectives and prerequisite concepts.
Classify key terms: already known, needs a brief bridge, taught in this lesson, or deliberately deferred.
In Stage 00 propose broad provisional **Blocks** for the whole course; do not author lesson scripts or infer content from index-only headings. In Stage 01 propose within-Block lesson boundaries and write coherent full continuous drafts for **that Block only**, without scene cuts.
Plan the learner journey and rough visual beats for each draft; preserve natural paragraphs, question/attempt/feedback boundaries.
**Stage 01 stops after complete connected drafts** for a bounded source block; do not run a full editorial critique, resolve final lesson boundaries or author scenes in that same turn.
**Stage 02 only after human `next`:** critique novice gaps, scientific/source fidelity, Arabic-English comprehension, independent transfer questions, purposeful length and cognitive load; rewrite and stop again.
**Stage 03 only after another human `next`:** decide whether each draft stays one lesson, becomes short internal sections, splits, merges or moves content to a neighboring lesson. Do not split solely by word count or source headings.
Confirm the final lesson map, coverage, prerequisites, assessments and stable IDs/order; rewrite each resulting lesson's opening, transitions, attempts and recap, then critique the revised boundaries before scenes.
Map every objective to teaching and independent questions. Use exact source locators; distinguish authored examples from book facts and record missing-source limits.
**Stage 04 only after the next human `next`:** decompose finalized drafts into scenes, with teaching, question/attempt and explanatory feedback separated; preserve spoken words and conceptual sequence. After this checkpoint, human `next block` may resume authoring the next source Block while current Block audio is deferred.
Once split, scene narration and feedback are the canonical script; regenerate any continuous review copy instead of maintaining another editable source.
Follow the course language policy; build meaning before or around English technical terms, support exam English naturally in Arabic.
Script-only requests return only the requested script (with non-spoken question/feedback boundaries when useful); do not synthesize or create extra surfaces.

Read [board and scenes](../../../instructions/board.md) for semantic units, both ratios and bespoke components.
Use visual ideas during drafting to improve teaching, but assign formal visual units and word onsets only after the narrative critique.
Keep data and custom React/Remotion code inside the lesson folder.
Do not clone a player, create a temporary platform or install a guessed SDK.
Read [shared preview](../../../preview-sdk/README.md) before implementing components or reviewing playback.
Default-export components accepting the public SDK VisualProps; keep them inside the lesson.
Add full English/Arabic question and answer units with reviewed anchors; never estimate missing timings.
At the authorized late-stage gate only, run the shared preview after timed validation and module completion; never skip a human stop gate because the SDK is installed.

Read [audio](../../../instructions/audio.md) before calls or delivery imports. Audio pilot is Stage 05 or later and paid dispatch still requires explicit scope/cost authorization beyond `next`.
Use the existing asynchronous gemini-tts factory; accepted/queued is not completed.
Validate a representative bilingual/value pilot before expanding a batch; use unique job IDs per take.
Reuse correct recordings for visual edits; verify served bytes, actual WAV duration and word timestamps.
Review actual speech/critical English/values separately; missing ASR does not prove silence.
Bind cues to audio/script/transcript hashes and occurrence-qualified timed evidence.
Never estimate timestamps from word counts or spread the script evenly.

Run draft/script/media/timed checks appropriate to the actual stage.
Structural validation and AI self-critique cannot substitute for evidence-backed source/scientific and teaching review.
Read [handoff](../../../instructions/handoff.md), update STATUS and export the selected curriculum.
Passed reviews need real evidence/reviewer and current sourceHash; never fill approval placeholders.
Keep runtime untested until actual playback review in both ratios; bind passed evidence to sourceHash, runtimeVersion and runtimeArtifactHash.
Exports are authoring handoffs, not platform releases. Build/tests never grant publication approval.
Do not access the platform DB or publish students' lessons from this repository.
Finish the **single authorized human gate** with files/stage, actual checks, limits and the next proposed gate. Update STATUS and stop until the user's subsequent `next` or comments.
