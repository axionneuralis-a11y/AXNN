# AXN Note 1.0.0 — DATA-001
## Data & Document Model Specification — DRAFT

**Status:** DRAFT — NOT OWNER-APPROVED  
**Phase:** Architecture / Foundation  
**Product baseline:** AXN Note 1.0.0  
**Created:** 2026-08-16

> This document is a working design artifact. It MUST NOT be treated as an approved Bible, Roadmap, Blueprint, or Owner Decision. Changes are expected during review.

## 1. Purpose

DATA-001 defines the proposed persistence and domain model for the new AXN Note 1.0.0 codebase.

The legacy WebView data model is not the implementation baseline. Legacy behavior may be referenced only when useful.

## 2. Core design principles

1. Stable identity is independent from title.
2. Persisted formats are explicitly versioned.
3. Trash is a lifecycle state, not a UI-only filter.
4. Attachments are first-class note assets.
5. Rich text is represented by a structured document model, not canonical raw HTML.
6. Database state is the source of truth for application data.
7. Large documents must remain compatible with the 100k/500k/1M character acceptance targets.
8. Backup, export, and import are distinct contracts.
9. No silent destructive mutation during import or recovery.
10. Schema changes require an explicit migration or incompatible-version policy.

## 3. Identity model

### 3.1 Note ID

Each note has a stable unique `noteId`.

The ID is the primary entity identity and MUST NOT be derived from:

- title;
- file name;
- creation timestamp alone;
- list position.

### 3.2 Attachment ID

Each attachment has an independent stable `attachmentId`.

An attachment references its parent note through `noteId`.

### 3.3 Origin / namespace

Persisted AXN data should carry format/origin metadata sufficient to identify the data family and schema version.

An identifier namespace is not an authenticity proof. Integrity/authenticity must be handled separately.

### 3.4 ID implementation

Exact ID encoding is intentionally NOT frozen in DATA-001 yet. Candidate approaches may include UUID/UUIDv7-like identifiers or another collision-resistant stable identifier.

This decision requires a short implementation/security review before freeze.

## 4. Note entity

Proposed conceptual fields:

- `noteId`
- `title`
- `documentId` or embedded document reference
- `status`
- `createdAt`
- `updatedAt`
- `deletedAt` (nullable)
- `metadata`
- `schemaVersion`

The exact relational mapping is implementation-specific and must be reviewed before Room entities are frozen.

### 4.1 Status

Initial lifecycle:

- `ACTIVE`
- `TRASHED`

Permanent deletion removes the entity and all owned data that must be removed with it.

## 5. Trash semantics

Delete operation:

`ACTIVE -> TRASHED`

Restore operation:

`TRASHED -> ACTIVE`

Permanent deletion:

`TRASHED -> removed`

Automatic purge:

`TRASHED + deletedAt >= 30 days -> eligible for permanent deletion`

The 30-day value comes from approved P0-03 and is not to be silently changed in implementation.

Permanent deletion must account for:

- note record;
- document content;
- attachment metadata;
- attachment binary;
- related recovery/derived data;
- any other user-owned dependent state.

The implementation must prevent orphaned user data.

## 6. Document model

### 6.1 Canonical representation

The persisted document is a structured document model.

Raw HTML is NOT the canonical persistence format.

The model must be able to represent the approved editor scope:

- plain text;
- heading;
- bold;
- italic;
- underline;
- strikethrough;
- bulleted list;
- numbered list;
- checklist;
- quote;
- code/monospace;
- hyperlink.

Undo/redo state does not need to be permanently persisted as part of the canonical note document unless a later design requires crash/session recovery to do so.

### 6.2 Block model

Conceptual block types:

- `Paragraph`
- `Heading`
- `BulletList`
- `NumberedList`
- `Checklist`
- `Quote`
- `CodeBlock`

The exact nesting model is intentionally open for review.

### 6.3 Inline model

Conceptual inline attributes:

- bold
- italic
- underline
- strikethrough
- hyperlink
- code/monospace

The implementation should avoid a model that duplicates large strings unnecessarily.

## 7. Large-text requirements

The persistence and editor pipeline must be designed around:

- 100,000 characters: normal target
- 500,000 characters: large target
- 1,000,000 characters: stress target

The final representation should minimize repeated full-document copies during:

- editing;
- autosave;
- search;
- serialization;
- export.

Performance architecture must be benchmarked rather than assumed.

## 8. Attachment entity

Conceptual fields:

- `attachmentId`
- `noteId`
- `originalName`
- `mimeType`
- `sizeBytes`
- `createdAt`
- `modifiedAt` where meaningful
- `checksum`
- `storageReference`
- `schemaVersion` if required

Binary content should be stored in app-private file storage rather than as large Room blobs by default.

`storageReference` MUST NOT expose raw filesystem assumptions to higher layers.

## 9. Attachment lifecycle

Attachment lifecycle follows its parent note:

`Active note -> active attachment`

`Trashed note -> attachment retained for restore`

`Permanent note deletion -> attachment permanently removed`

Restore must not create duplicate attachment identity.

## 10. Preferences

User preferences are separate from note content.

Candidate categories:

- theme mode;
- event/theme presentation settings where applicable;
- editor preferences;
- app-lock preference;
- UI preferences;
- other non-content configuration.

Exact preference keys belong to a separate Settings specification.

Preferences MUST NOT become a hidden storage location for note data.

## 11. Recovery draft

Crash-safe recovery is distinct from backup.

Conceptual state:

`Committed document + optional recovery draft`

A recovery draft may be created during editing/autosave.

On abnormal termination:

1. detect candidate recovery data;
2. validate it;
3. determine whether it is newer than committed state;
4. offer safe recovery when appropriate;
5. never silently overwrite a valid committed note with corrupted recovery data.

Recovery data is temporary/derived state and is not automatically part of Full Backup unless later required by the backup contract.

## 12. Schema/version model

Application version and persisted schema versions are independent.

At minimum, future implementation must be able to identify:

- database schema version;
- document/editor schema version;
- backup format version;
- export format version;
- import format version.

A schema migration must declare:

`source version -> target version`

and have deterministic behavior.

## 13. Backup relationship

Full Backup MUST preserve:

- active notes;
- trashed notes;
- document content;
- attachments;
- relevant preferences;
- metadata;
- schema/format information;
- integrity information.

A restored trashed note MUST remain trashed.

## 14. Import identity/conflict preparation

Import conflict detection will primarily use stable identity.

Same title alone is NOT a conflict.

Potential conflict states may include:

- same ID, equivalent content;
- same ID, different content;
- missing referenced attachment;
- schema version unsupported;
- integrity failure.

Conflict resolution belongs to IMPORT-001 and is not fully specified here.

## 15. Integrity

Checksums/hashes may be used to detect accidental corruption.

Integrity verification is not equivalent to authenticity verification.

The final security design must determine:

- algorithms;
- scope;
- where hashes are stored;
- backup integrity structure;
- whether signatures are required.

No custom cryptography is permitted.

## 16. Open decisions before freeze

The following remain deliberately unresolved:

1. Exact ID encoding.
2. Exact Room relational mapping.
3. Document block nesting model.
4. Inline span representation.
5. Serialization format for documents.
6. Recovery draft storage mechanism.
7. Exact attachment storage naming scheme.
8. Checksum algorithm and canonicalization rules.
9. Database encryption implementation details.
10. How document migrations are represented and tested.
11. Whether document content is stored as normalized rows, a versioned serialized document, or a hybrid.

These require review before DATA-001 becomes a frozen specification.

## 17. Phase gate

DATA-001 is ready to become a candidate frozen artifact only after:

- ARCH-001 consistency review;
- EDITOR-001 review;
- SECURITY-001 threat-model review;
- BACKUP-001 compatibility review;
- IMPORT-001 identity review;
- large-text performance design review.

**No approved Bible/Blueprint/Roadmap content is modified by this draft.**
