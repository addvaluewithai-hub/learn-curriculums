# Board, storyboard and components

Reflect each meaningful spoken idea using relevant diagram, label, equation, motion or readable text.
One main visual and gradual disclosure; never all conclusions at frame zero or walls of tiny text.
Keep necessary neutral context; do not render filler literally.
Semantic units link a spoken idea and occurrence-qualified phrase to a visible change.
Storyboard 16:9 and 9:16 independently; rearrange portrait rather than shrinking everything.
Account for 320px screens, long English questions, Arabic support and reduced motion.
Font/loading/bounds checks require later actual rendering; a written storyboard is not proof.

Show English question clauses at first spoken word, then later clauses/Arabic at their onsets.
Remove answer-revealing conclusions; preserve neutral context where useful.
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
