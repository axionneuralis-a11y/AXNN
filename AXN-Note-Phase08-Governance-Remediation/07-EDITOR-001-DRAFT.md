# EDITOR-001 — Document / Editor Architecture Specification
Status: **DRAFT — NOT FROZEN**

## Evidence basis

- `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` P0-04 and P0-11
- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §8
- `05-INDEPENDENT-CROSS-AUDIT/01-AUDIT-REPORT.md` §§9 and 15

## Product requirement

The editor is a Structured Rich Text Editor with controlled scope. The canonical persisted representation must be structured rather than raw HTML.

## Performance targets

- 100,000 characters — normal workload
- 500,000 characters — large workload
- 1,000,000 characters — stress target

## Required design coverage

- document model
- editing model
- rendering
- state management
- persistence
- autosave
- memory behavior
- undo/redo
- cursor/selection
- large-text strategy
- failure recovery
- schema versioning and migration

## Evidence-backed design direction

The Foundation baseline allows editing/rendering representations to differ from persistence representation. The persistence representation must be versioned and migratable.

## Missing acceptance data

The cross-audit states performance is not verification-ready because the repository lacks:
- benchmark design
- measurement criteria
- representative devices
- memory threshold
- latency threshold
- test dataset
- editor benchmark
- persistence benchmark

Therefore no performance readiness claim is made.

## Closure rule

EDITOR-001 can be frozen only after DATA-001 serialization/storage decisions and TEST-001 acceptance criteria are aligned.
