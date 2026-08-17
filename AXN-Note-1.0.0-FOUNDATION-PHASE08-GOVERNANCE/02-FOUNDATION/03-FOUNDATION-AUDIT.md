# AXN Note 1.0.0 — Foundation Audit & Initial Architecture Baseline

Status: WORKING BASELINE
Date: 2026-08-16
Owner authority: AXION Neuralis Project Owner

## 1. Source-of-truth determination

The uploaded package was inventoried as follows:

- `owner-decisions/AXN_NOTE_V3_OWNER_DECISIONS_BASELINE.md` — authoritative approved P0 decisions.
- `notes/catatan-keputusan-terbaru.txt` — new owner directions that must be promoted into project governance.
- `docs/AXN-NOTE-ROADMAP.md` — placeholder only (`templates`).
- `docs/AXN-NOTE-BIBLE.md` — placeholder only (`templates`).
- `docs/AXN-NOTE-BLUEPRINT.md` — placeholder only (`templates`).

The legacy docs are therefore not used as requirements for the new implementation.

## 2. Product reset

The new codebase is a clean start.

Product identity: AXN Note
Initial application version: `1.0.0`
Minimum Android: API 26
Architecture direction: native Android + Gradle
Legacy WebView code: reference/archive only, not a migration base.

Version `1.0.0` denotes the first release line of the new implementation and is not a continuation of the legacy WebView release numbering.

## 3. Newly promoted owner requirement

Project specifications must be published on the AXION Neuralis site under the AXN Note documentation namespace, for example:

- `/axnnote`
- `/axnnote/source`
- `/axnnote/audit`
- `/axnnote/specification`
- `/axnnote/security`
- `/axnnote/technology`

The exact URL structure remains an implementation decision, but the governing principle is approved: documentation must be modular so future AI agents and reviewers can load only the artifact relevant to their task.

The application itself must expose equivalent user-facing transparency for relevant specifications, privacy, data handling, security, licensing, and version information.

## 4. Initial architecture direction

Recommended stack for the clean-start implementation:

- Kotlin/JVM for application code.
- Gradle Kotlin DSL.
- Android Gradle Plugin 9.3.0 as the current stable baseline at the time of this audit.
- JDK 17.
- `minSdk = 26`.
- `compileSdk = 37`.
- `targetSdk = 37`.
- Jetpack Compose with the current stable Compose BOM.
- Material 3 for the component foundation, with custom AXN design tokens where needed.
- Room for structured local persistence.
- Android app-private storage for attachments.
- Android Keystore-backed key management for encryption keys.
- Android system document picker / Storage Access Framework for explicit attachment selection and export/import.
- Kotlin coroutines/Flow for asynchronous work and state propagation.
- Version catalogs for dependency governance.
- Unit, instrumented, UI, migration, import/export, backup, security, and performance tests as first-class project artifacts.

This stack is a recommendation, not an Owner Decision yet. It must pass the architecture consistency review before being frozen.

## 5. Proposed module boundary

Start with a deliberately small modular structure. Do not create dozens of Gradle modules prematurely.

```text
AXN Note 1.0.0
├── app
├── core:model
├── core:common
├── core:security
├── core:storage
├── feature:notes
├── feature:search
├── feature:trash
├── feature:settings
├── feature:editor
├── feature:attachments
├── feature:backup
└── feature:importexport
```

The exact module split can be reduced before implementation if it introduces unnecessary build complexity. The logical boundaries are more important than the number of Gradle modules.

## 6. Architectural rules

1. UI must not own persistence logic.
2. Domain/application rules must not depend on Compose UI.
3. Storage access must be abstracted behind repositories/data sources.
4. Security operations must be centralized and auditable.
5. Note identity is stable and independent from title.
6. Trash is a real lifecycle state, not a UI filter.
7. Attachments are first-class data related to notes.
8. Backup and export are different use cases and formats.
9. Import is non-destructive by default and atomic.
10. No user content is written to diagnostic logs.
11. Event themes may modify presentation only.
12. No cloud account is required for core local operation.
13. No broad filesystem permission is required for normal attachment selection.
14. Format/schema versions are independent from product version.
15. Every persisted schema must have a migration path or an explicit incompatible-version policy.

## 7. Initial data model direction

Core entities to be designed before implementation:

- Note
- NoteDocument / structured editor content
- Attachment
- Trash metadata/state
- UserPreference
- Backup metadata
- Import session/conflict record
- Format/schema metadata
- Security metadata where required

Do not finalize field names until the schema review. The stable identity model and lifecycle semantics must be finalized before UI CRUD code is written.

## 8. Editor strategy

The editor should use a structured document model rather than raw HTML as the canonical persisted form.

The canonical model must support the approved v3 editor scope while remaining deliberately smaller than a word processor.

Rendering and editing representations may differ from the persistence representation. The persistence representation must be versioned and migratable.

Large-text engineering must be designed into the editor/storage pipeline from the beginning. The 100k/500k/1M character targets are acceptance criteria, not a late optimization step.

## 9. Backup/export/import separation

Three contracts must remain distinct:

- Export: user portability.
- Backup: full recovery state, including Trash.
- Import: non-destructive ingestion with identity/conflict handling.

A shared low-level serialization library may be used, but the product contracts must remain separate and independently versioned.

## 10. Security direction

Use platform and established cryptographic primitives. Do not implement custom cryptography.

At minimum, the design must cover:

- encrypted local data as required by the threat model;
- secure key storage using Android Keystore mechanisms;
- encrypted backup representation;
- optional app lock/device authentication;
- redaction rules for logs and diagnostics;
- recovery behavior when keys, files, or backup components are damaged;
- explicit security limitations shown to users.

The threat model must be written before the encryption implementation is finalized.

## 11. Build/toolchain snapshot

As of the 2026-08-16 audit, official Android documentation lists AGP 9.3.0 as the stable release, supporting Gradle 9.5.0, JDK 17, and Android API up to 37. Android Studio Quail 2 (2026.1.2) is the current stable Studio release. Kotlin 2.4.10 is the current stable Kotlin release line used here; 2.4.20 was still a preview/beta at the audit date.

The implementation must still validate the exact Kotlin/AGP/Compose combination in a real build before the toolchain is frozen.

## 12. Architecture risks requiring explicit review

- Structured rich-text persistence versus large-text performance.
- Encryption-at-rest versus recoverability and migrations.
- Attachment storage versus backup size and atomic restore.
- ZIP import atomicity versus large imports.
- Full backup including Trash versus automatic purge semantics.
- API 26 support versus modern library minimums.
- Compose adaptive UI behavior across phone/tablet/desktop-like window sizes.
- Documentation synchronization between repository and AXION site.
- How the app exposes technical/security transparency without exposing unsafe implementation details.

## 13. Phase gate

No production feature coding should begin until these artifacts are frozen:

1. Architecture Decision Record.
2. Data model/schema specification.
3. Document/editor schema.
4. Backup/export/import format contracts.
5. Threat model and security architecture.
6. Build/toolchain specification.
7. Navigation and responsive UI specification.
8. Documentation publishing model.
9. Test strategy and acceptance criteria.

After those are frozen, the first code target is the smallest buildable Gradle project plus a vertical slice proving:

`launch -> local database -> create note -> edit -> autosave -> close/reopen -> verify persistence`.

Only after that vertical slice is stable should attachments, Trash, backup/import, encryption, and broader UI features be layered in.
