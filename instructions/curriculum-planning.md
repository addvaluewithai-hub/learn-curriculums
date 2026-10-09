# Curriculum planning: provisional lesson boundaries

This is an **authoring workflow**, not an amendment to the authoring JSON schema or a new mandatory file format. Follow [human stage gates](stage-gates.md), [teaching](teaching.md), [contract](contract.md), and [handoff](handoff.md) as appropriate.

**Execution boundary:** the steps below describe the end-to-end dependency order, **not permission to complete them all in one run**. Initial request executes steps 1–3 (Stage 01) for a bounded block and stops. The next human turns unlock critique (Stage 02), boundary decision/final writing (Stage 03), then scenes (Stage 04). Do not auto-run step 4 just because draft writing finished.

## Goal

The source's chapter/section structure is not automatically the student's ideal lesson structure. Write enough complete teaching to evaluate how many separate conceptual steps a learner can reasonably absorb, then confirm lesson boundaries **before** committed scene/audio production. Do not optimize to a prescribed word count or minutes-per-lesson target.

## Seven-step workflow

1. **Source and dependency analysis.** Inspect actual accessible chapter pages/locators. List concepts, source limits, audience prerequisites, objectives, misconceptions and dependencies. No invented content from unseen headings.
2. **Provisional lesson outline.** Cluster related objectives into proposed lessons. Note tentative coverage, a usable learner outcome and which prerequisites each cluster requires. Treat these as hypotheses, not an arbitrary one-book-section-one-lesson rule.
3. **Connected working drafts.** For a manageable **chapter or neighboring-lesson block**, write one cohesive draft per proposed lesson. A draft may have natural paragraphs, editorial headings, practice breaks, questions and separately marked feedback, but must **not be forced into production scene cuts yet**. Rough visual ideas are welcome.
4. **Whole-draft critique.** Review scientific/source accuracy, essential concept bridges, natural bilingual terms, coherence, conceptual novelty, worked examples, independent transfer questions and load. Locate exactly where the learner is asked to handle too many new concepts without consolidation.
5. **Boundary decision.** Explicitly choose for each draft: **keep as one**, **retain one lesson with short internal learning parts**, **split into lessons**, **merge with an adjacent lesson**, or **rescope/defer content**. Record a reason based on conceptual unity, dependency order, practical independent attempts, source coverage and learner burden. Length alone cannot decide.
6. **Finalize and re-review.** For every resulting lesson, write/revise its own opening, complete explanation, guided application, independent question/feedback and recap. A split is **not** cutting a transcript into pieces. Check coverage of **all** source-backed intended objectives across the new sequence, with no duplicate/truncated prerequisites or answer leaks. Update the approved OUTLINE boundaries/ordered IDs/objectives/source locators and dependencies before scenes.
7. **Production freeze then decomposition.** Once the teaching map and wording are settled, create/rework scene JSON, semantic anchors, storyboard ratios and clips. Scene narration/feedback become canonical; a joined reading copy must be generated from them, not independently edited. Run stage checks and real review before paid audio.

Do **not** wait for the entire curriculum to have completed drafts; review small connected blocks as sources become available. A course outline may be partly provisional while finished lessons stay stable.

## Boundary decision: evidence and checklist

Use a short note in the curriculum/lesson STATUS or PR (no invented approval badge or fixed numeric scoring):

- **Input:** source pages, proposed lesson/ID, prerequisite concept map, learner goal and reviewed working draft.
- **Symptoms:** where a cluster introduces multiple new ideas, demands another prerequisite, repeats the same demonstration, lacks independent transfer, or becomes exhausting without a meaningful checkpoint.
- **Decision:** keep / internal learning parts / split / merge / rescope, **with a learner-centered reason**; name proposed source coverage and objectives per resulting lesson.
- **Integrity:** check topic coverage, narrative transitions, distinct openings/recaps, guided vs genuinely independent questions, and English/math spoken clarity.
- **Status:** note any unreviewed science, unknown source access, collaboration needed, and **no false human sign-off**.

An independent learning part has a coherent micro-goal and chance to consolidate; it does **not** have to become a new stable lesson. Split into separate lessons only when each result has a teachable/assessable goal, enough supporting content, and a sensible dependency boundary.

## Stable identities and existing work

- **Working labels ≠ stable IDs.** Before formal lesson creation, revise candidate headings and orders freely in planning notes. Once a stable lesson ID is present in an agreed OUTLINE, or in a committed lesson, treat it as **issued**: do not silently rename, reuse, recycle or assume ID = order.
- For a changed boundary in an **active** course, propose an explicit before/after map and coordinate with the curriculum owner before editing the shared OUTLINE or another editor's work. New lessons get new stable IDs; preserve approved IDs where their identity/content remain continuous.
- If scenes, accepted recordings, timing, reviews, handoff or released student editions already exist, do **not** silently redistribute their clips. Record rework scope, preserve previous takes, regenerate affected scripts/anchors, invalidate outdated hashes/timing/review evidence, and run the permitted review/release process. Published editions stay immutable.
- If the user asks for **script only**, apply this reasoning privately and output the requested script; do not alter OUTLINE, create files, dispatch TTS or perform unauthorized collaboration actions.

## Example decision, not a mandated split

A textbook section may contain basic quantities, idealized models, Newton's laws, and gravitational weight. A continuous teaching draft could show these as multiple distinct concept clusters. Depending on learner level and how the independent questions land, keep one lesson with small internal parts **or** split into multiple sequenced lessons. Do not assume a specific number of lessons, remove essential explanations, or silently teach unseen textbook content.
