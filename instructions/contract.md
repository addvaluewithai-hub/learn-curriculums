# Authoring data contract v1

Production source format, not the platform's native LessonPackage.
Later the shared SDK adapts sources to approved playback; no adapter is implemented yet.
Preserve source content and stable IDs; make contract revisions explicit.

## Curriculum and lesson

course.json: schemaVersion=1, id, title, revision, description, language, sources, teacher.
OUTLINE.md: audience, prerequisites, ordered stable lesson IDs, objectives and source coverage.
Source: id, title, access=available|reviewed-notes|unavailable, plus file/URL and limitations.
Local notes/files go under curriculum references/; label original examples as original sources.

lessons/<id>/lesson.json: schemaVersion=1, kind=learn-authoring, id, curriculumId, order,
title, englishTitle, scriptRevision, prerequisites, objectives, scenes, glossary.
Objective: id, description, taughtIn=[scene IDs], assessedIn=[question IDs].
Scenes is an ordered list; each ID resolves to scenes/<id>.json.
Discovery uses folders, not tools with hardcoded lesson names.

## Scene

- id, title, objectiveIds, sources=[{sourceId, locator}].
- narration={id, role: teaching|question, script, units}.
- Unit={id, text, occurrence: 1, visualIntent}; text is a verbatim occurrence-qualified spoken phrase.
- visual={renderer, module, params, landscape, portrait}; both storyboard ratios required at script stage.
- module is lesson-relative, e.g. scenes/ParticleComparison.tsx; may be null during drafting.
- Question scene: question={id, english, arabic, attempt, answer, feedback}.
- answer={english, arabic, reasoning}; feedback={id, role: feedback, script, units} is a separate clip.
- attempt=written|choice|choice-and-written; choice needs options and zero-based correctIndex.
- Teaching and question scenes are separate; feedback is not a normal learning-path scene.
- Model answers never belong in pre-attempt audio/visuals.

Example question object:

```json
{
  "id": "Q1",
  "english": "What changed?",
  "arabic": "إيه اللي اتغير؟",
  "attempt": "written",
  "answer": {"english": "The volume changed.", "arabic": "الحجم اتغير.", "reasoning": "Explain the observation."},
  "feedback": {
    "id": "F01",
    "role": "feedback",
    "script": "The volume changed. الحجم اتغير. ونشرح السبب هنا.",
    "units": [{"id": "F1", "text": "The volume changed", "visualIntent": "Reveal the answer after submission."}]
  }
}
```

## Media and timing

jobs/: prepared requests and explicit dispatch outcomes.
media/<clip-id>/takes/<unique-job-id>/: result.json, transcript.json, audio.wav, verification.json.
media/<clip-id>/receipt.json: selected job, script/audio/transcript hashes, measured duration and relative files.
--select-new-take deliberately changes selection; previous takes remain intact.
Do not edit delivered words/bytes to manufacture coverage.
timing.json: audioHash, scriptHash, transcriptHash, method, reviewer, evidence, cues.
method=word-anchors-reviewed|multi-pass-reviewed. Cue={unitId, wordStart, wordEnd, atMs}.
Indices are zero-based inclusive; atMs is first anchor word start. Phrase and occurrence must match evidence.
Missing English anchors require real audio/alignment review, never guessed timings.
alignment.json optionally selects a separately reviewed corrected transcript under alignments/<hash>.json.
It binds the original transcript hash, selected audio/script hashes, method, reviewer and evidence.
timing.json uses that selected transcript hash; the factory original remains unchanged.

## Checks

draft checks shapes/identity/references; script adds source locators, teaching/assessment mappings, scripts and storyboards.
media adds verified delivered recordings; timed adds semantic anchor bindings.
None automatically proves scientific, listening, visual or playback quality.
review.json: sourceHash + checks sources/teaching/audio/timing/visual/runtime, each passed|failed|untested with reviewer/evidence.
Use current sourceHash from validate only after actual review. Source policy/input changes invalidate it.
Runtime stays untested while SDK is absent.
