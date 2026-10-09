# Source retention, rights and retrievable provenance

Applies to scanned PDFs, books, slides, multi-file curricula and other user-supplied source documents. The repository is **public**. This policy supplements [Stage 00](stage-gates.md) and [the authoring contract](contract.md).

## Keep actual originals accessible without leaking them

- **Do not automatically commit a scanned third-party book or confidential original** to public GitHub. Upload to public Git/Git LFS only after confirming the right to redistribute **and** explicit user authorization. Git LFS does not make files private.
- Prefer authorized durable **private** source storage with least-privilege access, if an appropriate connector is available. Actually verify upload/retrieval for the intended future agent. A chat attachment, local sandbox path, expired signed link, or a prior author's page notes are **not** reliable permanent access.
- If a secure persistence integration or permission is missing, keep an honest manifest with `storage=chat-only-temporary`/`unresolved`, record the blocker in STATUS and request supported storage/access. Do not invent a link, claim an upload occurred, or silently discard the source and later invent lesson details from headings.
- Never commit credentials, authorization headers, signed/expiring URLs, non-public raw bytes, or copied scans to this public repo. The local `references/private/` and `references/originals/` paths are gitignored against accidents; gitignore is **not** a substitute for publication rights checks.
- User-provided public-domain/open-licensed material may be added to a suitable storage path when rights and explicit public upload authorization are recorded.

## SOURCE_MANIFEST.md — one record per original/version

Place at `curricula/<course>/references/SOURCE_MANIFEST.md`:

- Stable `sourceId` matching `course.json`, original filename, title/author, edition/revision, original media type, byte length/page count **if checked**.
- Actual **SHA-256** if bytes were available and hashed; otherwise mark `not measured`. Never fabricate a digest. Separate files/editions get separate IDs/hashes.
- Storage class: `approved-private` / `public-redistributable` / `chat-only-temporary` / `unavailable`, safe non-secret retrieval instructions/locator, who can access it, and whether a future-agent retrieval was actually tested.
- Sharing-rights status/permission, file availability limitations, dated inspection scope, and associated `SOURCE_COVERAGE.md`. No secret links or user identifiers.

## SOURCE_COVERAGE.md — high-level map, then block-level inspection

- Record **PDF page index separately from printed page numbers**. For each chapter/topic, indicate `body-inspected` / `skimmed-available` / `contents-only` / `unreadable` / `not-provided` with evidence and missing segments.
- Stage 00 may index the table of contents and selected pages, with uninspected spans explicitly provisional; don't imply a 500-page document was fully reviewed just by seeing the index.
- At each Block's Stage 01 **reopen the actual pages** and inspect definitions, diagrams, formulas, examples and conditions in sufficient depth. Record exact locators and discrepancies; contents-only cannot ground detailed teaching.
- A source added/changed later requires updated manifests and coverage and appropriate reconsideration of dependent draft, review, timing and release evidence.

## Intake questions to verify

- Can a future **authorized** agent retrieve the exact original and edition without this conversation? If not, is the blocker visible and actionable?
- Do we have explicit rights before any raw original is made public?
- Does the roadmap distinguish actual supplied body pages from contents-only and missing/unreadable spans?
- Did we select a manageable B01 with an actual source and a dependency-based boundary, without drafting the entire book?
