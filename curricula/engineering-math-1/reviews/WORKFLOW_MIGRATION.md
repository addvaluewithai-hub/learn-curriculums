# Curriculum migration — legacy Stage 02 to Stage 00/Block governance

**Date:** 2026-10-09  
**PR:** [#8](https://github.com/addvaluewithai-hub/learn-curriculums/pull/8) (draft/unmerged)  
**Source governance:** `main` commit `ba4706956c2c8ee3bf4103c08124b28b74c3390e`, merged into curriculum branch as merge commit `866cf0c64e254da4718d7fbc115f719e654b4be6`, preserving the existing curriculum content.

## Why this migration happened
The previous repository workflow began authoring immediately at Stage 01 (several contiguous lesson drafts), later Stage 02 critique, and only then Stage 03 final boundaries. The new repository policy adds a one-time **Stage 00** (safe source inventory, provisional whole-course roadmap, selected B01) and **separate per-Block** status/gates; after B01 Stage 04 human inspection `next block` may move to B02 editorial authoring without waiting for optional audio.

**The user explicitly requested structural alignment before Stage 03.** This migration does **not** retroactively imply a human ran/approved Stage 00 at original inception, authorize Stage 03, or move/duplicate nine drafts.

## Exact source controls now added
- `references/SOURCE_MANIFEST.md`: original identity, measured size **18,199,705 bytes**, real SHA-256 `a4d6e631fd887071db151c6e494519424dc46369376c5aeff6a5b58f72c99623`, actual **43 PDF pages**, unknown redistribution rights and **chat-only-temporary** storage classification.
- `references/SOURCE_COVERAGE.md`: cover/contents, PDF and printed-page distinctions, inspected/sampled vs contents-only vs not supplied.
- **Future retrieval is NOT VERIFIED.** The original was mountable in the current conversation session, but neither permanent private storage nor access by a future agent has been established. The scanned original was **not** committed to the public repository; request user-authorized safe private storage if needed.
- Historical source observations remain in `references/SOURCE_REVIEW.md`, with their original meaning and limitations preserved.

## New production Blocks and original artifacts

| Production block | Source printed range | What is actually available | Editorial files retained | New control |
|---|---|---|---|---|
| **B01 — Preliminaries (active)** | **1–20** | Body supplied, exercises on pp. 19–20 | `working-drafts/prelim-01-*.md` to `prelim-04-*.md`, critique P-A–P-D | `blocks/B01/STATUS.md`: historical Stage 02, awaiting `next` for B01 Stage 03 |
| **B02 — Functions/limits/continuity** | **21–53** | Body supplied | `working-drafts/01-functions.md` to `05-continuity.md`, critique A–E | `blocks/B02/STATUS.md`: historical Stage 01/02 work preserved, currently inactive |
| B03 — Differentiation | **54–80** | Body supplied, only skimmed/planned | No scripts | Course roadmap; future source reinspection |
| B04–B07 | **81–181 (page ranges inferred from TOC)** | **No supplied body**, titles in contents only | No scripts | Explicitly blocked until actual source pages arrive |

Global `OUTLINE.md` now owns provisional **whole-course Blocks**; curriculum `STATUS.md` tracks active B01 and deferred B02–B07. No new lesson IDs, final student lesson boundaries or scene JSON were issued.

## Preservation, audit, and checks
- **9/9** old complete working drafts remain readable under unchanged original paths.
- **29** independent question prompts and **29** separate post-attempt explanatory feedback sections remain; all nine scripts retain the **Stage 02** editorial state and were not silently rewritten for migration.
- Preserved original source and critique IDs; no source scans, audio, timing, runtime/SDK modules or credentials uploaded.
- Verified from GitHub the new manifests and both Block STATUS files, a whole-course master outline and exact new instructions on the feature branch.
- The branch was **54 commits ahead of main, 0 behind** after its two-parent governance merge (at migration read-back time); no content conflict and no merge into `main` was performed.
- Local checkout/test attempt `git clone --depth=1 --single-branch ...` **FAILED** because `github.com` could not be resolved in the container. Therefore `tools/quality.py`, Python unit tests, full CLI draft validation, build and runtime playback were **not** run. Structural file/marker checks performed via GitHub are documented separately and **not** falsely called those local tests.

## Human stage contract after migration
1. **Now:** B01 is the only active Block. The last historical editorial work is Stage 02. Migration was structural and didn't trigger Stage 03.
2. **Later `next`:** if source access and prerequisites are adequate, do **B01 Stage 03 only** (reasoned keep/split/chunk decisions and complete resulting scripts) and STOP.
3. After a separate `next` and B01 Stage 04 human checkpoint, human `next block` can activate B02. B02 already has historical scripts/critique; do not throw them away, silently redo Stage 00, or auto-mark a newly required per-Block gate complete. First reconcile/source-check its historical evidence and explicitly record the chosen resumed gate.
4. **No paid TTS** from `next`; no academic passes, merge to main or student publication from this PR.

## Pending owner inputs
- Choose an **authorized private durable folder/storage** that future authorized agents can access for this exact PDF edition. No source/public redistribution permission is assumed.
- Later: accept/revise the Block roadmap and final B01 lesson boundaries; have a competent mathematics reviewer validate scan conditions and new examples.
