---
name: produce-learn-lesson
description: Author or repair source-grounded Learn curricula and lessons in learn-curriculums. Use for produce lesson 3, curriculum scripts, storyboard, custom React scenes, Gemini TTS, word timestamps, semantic cue alignment and production handoff. This repository currently has no preview SDK or student publication service.
---

# Produce a Learn lesson

Read root AGENTS.md, the selected course.json, OUTLINE.md, sources and lesson STATUS.md.
Resolve the requested ordinal to a stable ID; ask only when the course is genuinely ambiguous.
Use [the data contract](../../../instructions/contract.md) before creating or changing files.
Preserve another editor's work and accepted takes; scope changes to the selected course/lesson.

Read [teaching](../../../instructions/teaching.md) and map audience, source boundaries, objectives and prerequisite concepts.
Classify key terms: already known, needs a brief bridge, taught in this lesson, or deliberately deferred.
Plan the learner journey and rough visual beats; write a coherent continuous spoken *working draft* before formal scenes.
Critique specific novice gaps, scientific/source fidelity, Arabic-English comprehension, independent transfer questions and purposeful length; revise material weaknesses before decomposition.
Map every objective to teaching and independent questions. Use exact source locators; distinguish authored examples from book facts and record missing-source limits.
Decompose the settled draft into scenes, with teaching, question/attempt and explanatory feedback separated; preserve spoken words and conceptual sequence.
Once split, scene narration and feedback are the canonical script; regenerate any continuous review copy instead of maintaining another editable source.
Follow the course language policy; build meaning before or around English technical terms, support exam English naturally in Arabic.
Script-only requests return only the requested script (with non-spoken question/feedback boundaries when useful); do not synthesize or create extra surfaces.

Read [board and scenes](../../../instructions/board.md) for semantic units, both ratios and bespoke components.
Use visual ideas during drafting to improve teaching, but assign formal visual units and word onsets only after the narrative critique.
Keep data and custom React/Remotion code inside the lesson folder.
Do not clone a player, create a temporary platform or install a guessed SDK.
Produce storyboards/component drafts now; report runtime untested until the shared SDK exists.

Read [audio](../../../instructions/audio.md) before calls or delivery imports.
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
Keep runtime untested while SDK is absent. Exports are authoring handoffs, not runtime packages/releases.
Do not access the platform DB or publish students' lessons from this repository.
Finish with files/stage, actual checks, limitations and next executable action.
