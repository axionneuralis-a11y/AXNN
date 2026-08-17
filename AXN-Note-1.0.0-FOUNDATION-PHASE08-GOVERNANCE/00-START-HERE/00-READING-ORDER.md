# AXN Note 1.0.0 — Reading Order

This package is reorganized into a single global reading sequence. The number at the beginning of each file is the recommended reading order.

The goal is to let a new reviewer or AI agent understand the project structure without opening every file.

## Reading order

| No. | File | Role | Status |
|---:|---|---|---|
| 1 | `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` | Source of truth for the 12 approved P0 Owner Decisions. | **Authoritative** |
| 2 | `01-OWNER/02-OWNER-DIRECTIONS-LATEST.txt` | Latest Owner directions that need to be reflected in governance/documentation. | **Authoritative direction** |
| 3 | `02-FOUNDATION/03-FOUNDATION-AUDIT.md` | Establishes the clean-start 1.0.0 foundation, architecture direction, rules, and phase gate. | **Foundation baseline** |
| 4 | `02-FOUNDATION/04-TOOLCHAIN-RESEARCH.md` | Current toolchain research snapshot. | **Research baseline; build validation still required** |
| 5 | `03-AUDIT/05-AUDIT-REPORT.md` | Main foundation audit and blocking findings. | **Audit record** |
| 6 | `03-AUDIT/06-AUDIT-CONTINUATION.md` | Follow-up audit with revalidation and current toolchain findings. | **Audit record** |
| 7 | `03-AUDIT/07-AUDIT-ADDENDUM-02.md` | Second addendum; sharpens version-authority, version-identity, and governance findings. | **Audit addendum** |
| 8 | `03-AUDIT/08-AUDIT-ADDENDUM-03.md` | Latest addendum; records the Owner resolution of the v3 → 1.0.0 version conflict and remaining traceability gaps. | **Latest audit state** |
| 9 | `04-DOCUMENTATION-PLACEHOLDERS/09-ROADMAP.md` | Planned roadmap document. | **Placeholder / incomplete** |
| 10 | `04-DOCUMENTATION-PLACEHOLDERS/10-BIBLE.md` | Planned project/product bible. | **Placeholder / incomplete** |
| 11 | `04-DOCUMENTATION-PLACEHOLDERS/11-BLUEPRINT.md` | Planned blueprint. | **Placeholder / incomplete** |

## How to use this package

For a quick understanding, read files **1 → 4** first.

For audit status, continue with files **5 → 8**.

Files **9 → 11** are intentionally last because they are currently placeholders and contain no substantive requirements.

## Current structural interpretation

The project currently has four distinct information layers:

1. **Owner layer** — what is decided and what the Owner additionally requires.
2. **Foundation layer** — how those decisions are translated into architecture and implementation constraints.
3. **Audit layer** — what is missing, contradictory, stale, or still blocking implementation.
4. **Documentation placeholders** — future artifacts that have not yet been populated.

## Important naming rule

Use the global numeric prefix as the reading-order identifier. Keep the descriptive filename stable after the number.

Recommended convention:

`NN-DOCUMENT-TYPE-DESCRIPTION.ext`

Examples:

- `01-OWNER-DECISIONS-BASELINE.md`
- `03-FOUNDATION-AUDIT.md`
- `05-AUDIT-REPORT.md`
- `08-AUDIT-ADDENDUM-03.md`

Do not use dates as the primary ordering mechanism; dates belong in document metadata/content when needed.

## Important status note

The latest audit addendum records that the Owner resolved the version conflict and confirmed **AXN Note 1.0.0**. The remaining blocker is documentation/phase-gate completeness rather than an unresolved v3-versus-1.0.0 authority conflict.

## Directory map

```text
AXN-Note-1.0.0-FOUNDATION-REORGANIZED/
├── 00-START-HERE/
│   └── 00-READING-ORDER.md
├── 01-OWNER/
│   ├── 01-OWNER-DECISIONS-BASELINE.md
│   └── 02-OWNER-DIRECTIONS-LATEST.txt
├── 02-FOUNDATION/
│   ├── 03-FOUNDATION-AUDIT.md
│   └── 04-TOOLCHAIN-RESEARCH.md
├── 03-AUDIT/
│   ├── 05-AUDIT-REPORT.md
│   ├── 06-AUDIT-CONTINUATION.md
│   ├── 07-AUDIT-ADDENDUM-02.md
│   └── 08-AUDIT-ADDENDUM-03.md
└── 04-DOCUMENTATION-PLACEHOLDERS/
    ├── 09-ROADMAP.md
    ├── 10-BIBLE.md
    └── 11-BLUEPRINT.md
```

## Phase 08 — Governance & Closure Readiness

The following documents are the canonical closure control surface and must be read after the historical audit corpus:

| Order | Source Path | Role | Status |
|---|---|---|---|
| 22 | `06-GOVERNANCE/01-CANONICAL-FINDINGS-REGISTRY.md` | Canonical consolidated findings registry | **ACTIVE** |
| 23 | `06-GOVERNANCE/02-FOUNDATION-CLOSURE-PROTOCOL.md` | Foundation-to-Bible/Blueprint gate checklist | **ACTIVE / GATE NOT PASSED** |
| 24 | `06-GOVERNANCE/03-DOCUMENT-CLASSIFICATION-REGISTRY.md` | Information classification for every corpus document | **ACTIVE** |
| 25 | `06-GOVERNANCE/04-SOURCE-TRACEABILITY-MAP.md` | Machine-traceable source path/section map | **ACTIVE** |
| 26 | `06-GOVERNANCE/05-REGISTRY-VERIFICATION.md` | Verification of canonical IDs and current gate state | **ACTIVE** |

### Governance Interpretation

Historical audit records are immutable evidence. The canonical registry is the operational source for current finding status. `Finding Status` and `Artifact Status` are independent states.

The current Foundation verdict remains **BLOCKED**. No Bible/Blueprint transition is authorized until all P0/P1 gate blockers are closed/verified and all required technical artifacts are `FROZEN`.

