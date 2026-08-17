# ARCH-001 — Architecture Decision Record
Status: **DRAFT — NOT FROZEN**

## Evidence basis

Primary inputs:
- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §§2–6
- `03-AUDIT/17-AUDIT-ARCHITECTURE-&-DATA.md` §§1–2
- `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` P0-01/P0-02/P0-08/P0-12

## Architectural direction

The project is a clean-start native Android application using Gradle. Legacy WebView/PWA code is reference/archive only.

The Foundation baseline proposes:
- Kotlin/JVM
- Gradle Kotlin DSL
- Android native
- Compose + Material 3
- Room
- Android app-private attachment storage
- Android Keystore-backed key management
- Storage Access Framework for explicit file selection/import/export
- coroutines/Flow
- version catalogs

These remain **provisional recommendations** until build and architecture validation.

## Logical boundaries

The Foundation baseline proposes these logical modules:
`app`, `core:model`, `core:common`, `core:security`, `core:storage`, `feature:notes`, `feature:search`, `feature:trash`, `feature:settings`, `feature:editor`, `feature:attachments`, `feature:backup`, `feature:importexport`.

The logical boundaries are authoritative as a design direction; the exact Gradle module count is not frozen.

## Rules already evidenced

1. UI does not own persistence logic.
2. Domain/application rules do not depend on Compose UI.
3. Storage is abstracted behind repositories/data sources.
4. Security operations are centralized and auditable.
5. Note identity is stable and independent from title.
6. Trash is a lifecycle state.
7. Attachments are first-class related data.
8. Backup and export are distinct contracts.
9. Import is non-destructive by default and atomic.
10. User content is excluded from diagnostic logs.
11. Event themes affect presentation only.
12. Core local operation does not require a cloud account.
13. Normal attachment selection does not require broad filesystem permission.
14. Format/schema versions are independent of product version.
15. Every persisted schema has a migration path or explicit incompatibility policy.

## Still unresolved

- exact module dependency graph;
- interface contracts between modules;
- observability boundary;
- configuration management;
- exact persistence/serialization boundary;
- toolchain combination validated by clean build.

These are not to be invented silently.
