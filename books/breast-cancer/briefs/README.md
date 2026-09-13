# Development briefs

One brief per part. A brief is the writing instruction for its chapters, not draft prose.

Each chapter entry carries four things:

- **Carries** the single argument the chapter must land. If the draft does not land it, the draft is wrong.
- **Threads** the load-bearing content, in the order it should be built.
- **Anchors** the current evidence, written in chapter citation syntax so it can be lifted directly into prose.
- **Controversy** the live disagreement a fellow-level reader needs named rather than smoothed over.

## How Claude Code should use these

1. Open `briefs/PT-XX.md` and find the chapter entry.
2. Open `outline.yaml` and read that chapter's `BS-####` sections. The sections are the skeleton, the brief is the argument.
3. Draft `chapters/BC-###.md`, one `## BS-####` heading per section, in the order the outline gives.
4. Lift the anchors. They are already in `[@key]` and `{{trial:key}}` syntax.
5. Add at least one ` ```interplay ` block to any disease chapter in Parts IX and X.
6. Run `python3 tools/validate.py`.

**Do not publish prose citing an unverified reference.** Entries in `references.yaml` with
`verify: true` record a claim whose identifier is not yet confirmed. Run `make verify-queue`
to see what is outstanding. Resolve an identifier before the key reaches a published chapter.

## Provenance

These briefs merge an Open Evidence evidence-synthesis pass with the book's own structure.
Trial data are current to 2026. Numbers are anchors for the writer, not a substitute for the
primary text. Every number in a brief must be checked against its source before it is published.
