# Board, storyboard and components

Reflect each meaningful spoken idea using relevant diagram, label, equation, motion or readable text.
Sketch rough teaching visuals while designing the learner arc; a useful diagram may improve the script before scenes are fixed.
After critiquing the whole narrative **and confirming the lesson boundary map**, split finalized lessons into scene clips and precise semantic anchors; retain all reviewed reasoning and question/feedback boundaries.
Generate any continuous reading copy from canonical scenes rather than editing it as a second script.
One main visual and gradual disclosure; never all conclusions at frame zero or walls of tiny text.
Keep necessary neutral context; do not render filler literally.
Semantic units link a spoken idea and occurrence-qualified phrase to a visible change.
After audio delivery, use [AI-authored timing](timing.md): read actual timestamped words
and write the semantic cue decisions directly. Text matching is only an optional search aid.
Storyboard 16:9 and 9:16 independently; rearrange portrait rather than shrinking everything.
Account for 320px screens, long English questions, Arabic support and reduced motion.
Font/loading/bounds checks require later actual rendering; a written storyboard is not proof.

Show English question clauses at first spoken word, then later clauses/Arabic at their onsets.
Remove answer-revealing conclusions; preserve neutral context where useful.
Check the question speech, option wording, labels and staged reveals together for answer leakage before attempt.
After reading show the full question and enable attempts; feedback reveals only after valid submission.
Flow: teaching → reading → attempt → feedback → next teaching → review.
Submission starts feedback; completion starts next teaching without another Play click.
Defer is not success; self-review is not automatic mastery.

Keep custom React/Remotion component drafts in the lesson scenes folder.
Existing visual responsibilities: spec, recording, frame, layout, reducedMotion, fps.
Reconcile real SDK types/imports when installed; no guessed package names or fake compilation pass.
Until then complete storyboards and provisional components; reuse primitives only where they fit.
Later animate from Remotion current frame, not separate timers or CSS teaching animations.
Pause/buffering/reverse seek/replay preserve or reverse disclosure; one audio source and cancel stale events.
Retry errors rather than skipping audio. Ordinary preview excludes auth and student persistence.
No temporary player/platform/DB to bypass missing SDK.
