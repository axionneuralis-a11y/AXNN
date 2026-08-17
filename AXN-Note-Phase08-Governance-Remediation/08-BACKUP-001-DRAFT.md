# BACKUP-001 — Full Backup Contract
Status: **DRAFT — OWNER REVIEW REQUIRED / NOT FROZEN**

## Evidence basis

- `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` P0-07
- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §9
- `05-INDEPENDENT-CROSS-AUDIT/01-AUDIT-REPORT.md` §13

## Owner-backed scope

Backup is a full-recovery contract and must include the state required to recover the application completely, including Trash.

Evidence explicitly identifies:
- active notes
- Trash
- attachments
- relevant metadata
- relevant preferences
- schema/version
- integrity information

## Contract sections required

- container format
- manifest
- format version
- integrity/checksum
- encryption relationship
- compression policy
- attachment representation
- corruption detection
- atomic restore
- interrupted restore
- incompatible-version handling
- recovery failure behavior
- compatibility policy
- validation

## Boundary

Backup is distinct from export:
- Export = user portability
- Backup = full recovery state including Trash
- Import = non-destructive ingestion

## Owner Decision Required

P0-07 is marked `APPROVED — Owner Revision`. The semantic scope is substantially clear, but closure cannot reinterpret the status or silently choose unresolved product policy. The remaining ambiguity must be resolved by Owner before freezing BACKUP-001.
