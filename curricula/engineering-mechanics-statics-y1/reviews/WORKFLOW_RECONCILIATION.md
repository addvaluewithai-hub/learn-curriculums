# Workflow alignment note — 2026-10-09

**Request:** User said “ظبط الهيكل الجديد” after reviewing the newly changed `main` stage-gates and source-handling instructions. It authorizes **structure/source-control reconciliation only**, not forward gate progression.

## What changed
1. Retained the current source ID, measured and recorded source SHA-256, bytes and pages, and recorded **chat-only-temporary** storage with rights/retrieval blockers in `references/SOURCE_MANIFEST.md`.
2. Added `references/SOURCE_COVERAGE.md` to separate actual body availability from table-of-contents-only chapters, PDF scan pages from printed pages, and earlier reviews from new complete source inspections.
3. Reframed `OUTLINE.md` as a **provisional whole-course B01–B09 roadmap**, preserving the entire existing B01 final lesson/order/objective/question/source mapping and its three stable IDs.
4. Separated course `STATUS.md` (global source/roadmap/active B01) from `blocks/B01/STATUS.md` (actual editorial gate and next human choice).
5. Updated `course.json` source metadata to align with measured originals and documented nonpersistent storage, **without changing the source ID or course ID**.

## Preserved and not retroactively certified
- Previous Stage 01–03 history in PR #7 is real and is retained. **A standalone Stage 00 was never executed at the beginning**; the new intake files were added under explicit user-requested alignment. No need to undo/rewrite three complete scripts or issue new IDs.
- B01 Stage 03 remains the last **completed** production gate; Stage 04 is not authorized by this message.
- No copied original pages or PDF binary in public GitHub, no verified private source upload, no TTS, no independent human science/learning review, no runtime preview, no main merge, no publication.
- Current branch is intentionally not rebased/force-pushed while adapting; GitHub PR base is `main`, which now carries the new workflow instructions.

## Open explicit next question
Where is the approved **private** durable location for storing the PDF with future-author access? The user will need to authorize access/location; the assistant must not silently make the scan public.
