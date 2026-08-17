# P0 Owner Decision Compliance Matrix

| P0 | Owner decision from baseline | Current evidence status | Technical implication | Action |
|---|---|---|---|---|
| P0-01 | Android 8.0 / API 26+ | PASS at requirement level | minSdk must remain 26+ | preserve |
| P0-02 | Privacy-first + Offline-first + User-owned data | PASS at principle level | no core cloud dependency; data ownership/export implications | operationalize in ARCH/DATA/DOCS |
| P0-03 | Active → Trash → Restore / Permanent Delete | PASS at lifecycle level | Trash is a real state and must be modeled | operationalize DATA/UI/TEST |
| P0-04 | Structured Rich Text Editor with controlled scope | PASS at principle/scope level | structured editor is required; exact schema is not frozen | EDITOR-001 required |
| P0-05 | Arbitrary user-selected file attachments as first-class assets | PASS at requirement level | attachment lifecycle/storage/backup must be specified | DATA/BACKUP/UI/TEST |
| P0-06 | Non-destructive ZIP import by default | PASS at decision level | import must not replace existing content by default | IMPORT-001 required |
| P0-07 | Full backup includes complete recovery state, including Trash | REVIEW REQUIRED | backup scope is clear; status/remaining ambiguity blocks closure | OWNER DECISION REQUIRED |
| P0-08 | Layered Security Architecture | PASS at principle level | threat model and security architecture still required | SECURITY-001 required |
| P0-09 | Apache License 2.0 + dependency/license audit before release | PASS at policy level | release governance must include dependency/license check | DOCS/BUILD |
| P0-10 | SemVer + independent technical version identities | PASS at policy level | DB/Backup/Export/Editor versions need explicit initial-version policy | DATA-001 + OWNER REVIEW |
| P0-11 | 100k / 500k / 1M character large-text targets | PASS at requirement level | benchmark and acceptance criteria absent | EDITOR-001 + TEST-001 |
| P0-12 | Adaptive + Content-first UI | PASS at principle level | navigation, large-screen, accessibility details absent | UI-001 + TEST-001 |

## Decision integrity rule

No row above authorizes an AI-chosen product decision that is not present in the Owner baseline. Missing operational details must be specified as derived technical contracts or escalated as Owner Decision Required when they change product behavior.
