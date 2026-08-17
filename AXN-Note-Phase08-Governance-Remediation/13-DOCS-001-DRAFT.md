# DOCS-001 — Documentation Publishing and Synchronization Model
Status: **DRAFT — OWNER REVIEW REQUIRED / NOT FROZEN**

## Evidence basis

- `01-OWNER/02-OWNER-DIRECTIONS-LATEST.txt`
- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §3
- `03-AUDIT/19-AUDIT-DOCUMENTATION-&-GOVERNANCE.md`
- `05-INDEPENDENT-CROSS-AUDIT/01-AUDIT-REPORT.md` §19 and governance findings

## Owner direction

Specifications must be published on the AXION Neuralis site under an AXN Note namespace, with modular sections so future AI/review agents can load only the required artifact.

Examples recorded by Owner:
- `/axnnote`
- `/axnnote/source`
- `/axnnote/audit`
- `/axnnote/specification`
- `/axnnote/security`
- `/axnnote/technology`

The exact URL structure remains an implementation detail, not an approved exact routing contract.

The app must expose equivalent relevant transparency to users.

## Required publishing model

- source documents
- public/generated documents
- authority level
- publication flow
- versioning
- supersession
- archive
- changelog
- reading order
- synchronization trigger
- ownership
- promotion rules
- conflict handling

## Current gap

The repository's `00-START-HERE/00-READING-ORDER.md` is reported by audit addenda as out of sync with the current structure. DOCS-001 must therefore define the canonical machine-readable order and synchronization rules.
