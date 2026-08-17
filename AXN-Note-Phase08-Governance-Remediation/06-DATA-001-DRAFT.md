# DATA-001 — Data Model / Schema Specification
Status: **DRAFT — BLOCKED / OWNER REVIEW REQUIRED**

## Evidence basis

Primary:
- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §§7–9
- `03-AUDIT/17-AUDIT-ARCHITECTURE-&-DATA.md` §§3–4
- `05-INDEPENDENT-CROSS-AUDIT/01-AUDIT-REPORT.md` §§9 and 11

## Core entities identified

- Note
- NoteDocument / structured editor content
- Attachment
- Trash metadata/state
- UserPreference
- Backup metadata
- Import session/conflict record
- Format/schema metadata
- Security metadata where required

## Frozen principles

- Note identity is stable and independent from title.
- Trash lifecycle is `Active → Trash → Restore / Permanent Delete`.
- Foundation audit records approved automatic purge at 30 days.
- Attachments are first-class note assets.
- Product version and schema/format versions are independent.

## Open decisions explicitly evidenced

The audit explicitly identifies 11 open DATA-001 decisions. The current evidence names these categories, without enough evidence to safely invent final values:

1. Exact ID encoding.
2. Exact Room entity/DAO/relationship mapping.
3. Document block nesting model.
4. Inline span representation.
5. Final note-document serialization format.
6. Large-text storage/persistence strategy for 1M characters.
7. Remaining schema/lifecycle details needed for complete migration and persistence closure.

The corpus establishes that there are 11 open decisions total, but does not enumerate all 11 with enough precision to reconstruct the missing seven without risking fabrication. Therefore the missing seven remain `UNKNOWN / OWNER DECISION REQUIRED` rather than being invented.

## Technical version identity

P0-10 requires independent identities for:
- application version
- database schema version
- backup format version
- export format version
- editor schema version
- build identifier

Current audit status:
- DB schema: UNINITIALIZED
- Backup format: UNINITIALIZED
- Export format: UNINITIALIZED
- Editor schema: UNINITIALIZED

`OWNER DECISION REQUIRED` for the initial-version policy. The audit gives `1` only as an example, not as an approved value.

## Closure blockers

DATA-001 cannot be frozen until all open decisions and initial technical version policy are explicit, reviewable, and consistent with EDITOR-001, BACKUP-001, IMPORT-001, and TEST-001.
