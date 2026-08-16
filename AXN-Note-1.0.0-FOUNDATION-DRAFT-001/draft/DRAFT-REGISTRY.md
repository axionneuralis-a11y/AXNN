# AXN Note 1.0.0 — DRAFT Registry

**Status:** Working registry — NOT OFFICIAL  
**Purpose:** Prevent loss of planning decisions while protecting approved documents from accidental edits.

## Authority order

1. Owner Decisions — approved authority.
2. Approved project documents — only after explicit Owner approval.
3. Draft artifacts — working proposals only.
4. AI recommendations — non-authoritative.
5. Legacy source/documents — reference only.

## Rule

A draft MUST NOT silently overwrite or modify an approved document.

Promotion path:

`Draft -> Review -> Owner Decision/Approval -> Official Document`

If an approved document needs a change, create a new draft/change proposal first.

## Current drafts

- `draft/DATA-001-DATA-MODEL.md` — Data & Document Model Specification.
- Future planned drafts:
  - `ARCH-001`
  - `EDITOR-001`
  - `SECURITY-001`
  - `BACKUP-001`
  - `IMPORT-001`
  - `BUILD-001`
  - `UI-001`
  - `DOCS-001`
  - `TEST-001`

## Versioning rule

The current product codebase is intentionally being restarted as **AXN Note 1.0.0**.

The existing P0 Owner Decisions document remains an approved requirement baseline even though its historical document title says "v3". This naming discrepancy is a documentation/governance item and MUST NOT be resolved by editing the approved Owner Decisions file without Owner approval.

## Documentation rule

AXION website documentation and in-app transparency are planned documentation surfaces. Their exact publishing architecture remains a draft until `DOCS-001` is reviewed.
