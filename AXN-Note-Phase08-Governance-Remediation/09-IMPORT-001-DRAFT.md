# IMPORT-001 — Non-Destructive Import Contract
Status: **DRAFT — NOT FROZEN**

## Evidence basis

- `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` P0-06
- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §9
- `05-INDEPENDENT-CROSS-AUDIT/01-AUDIT-REPORT.md` §14

## Owner-backed rule

Import is non-destructive by default. Import must not behave as replace.

## Required pipeline

`validation → identity detection → schema validation → conflict detection → resolution → atomic commit`

## Required edge cases

- malformed ZIP
- oversized ZIP
- duplicate IDs
- duplicate attachments
- invalid attachment
- unsupported schema
- future schema
- partial failure
- interrupted import

## Required contract areas

- supported format
- parsing
- validation
- conflict behavior
- duplicate behavior
- ID collision
- attachment handling
- metadata handling
- rollback/failure behavior
- atomicity

## Dependency

IMPORT-001 depends on DATA-001 identity/schema semantics and must be cross-validated against BACKUP-001 without conflating the contracts.
