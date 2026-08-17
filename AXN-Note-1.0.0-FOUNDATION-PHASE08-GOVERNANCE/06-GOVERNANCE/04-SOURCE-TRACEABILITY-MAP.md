# AXN Note 1.0.0 — Source Traceability Map

**Purpose:** Replace ambiguous numeric citation chains with stable repository-relative source locators for all new governance decisions.

**Information Classification:** AI/ENGINEERING INTERNAL

## Canonical Trace Format

`[TRACE: Source Path=<repo-relative path>; Source Section=<exact section heading>]`

For a specific artifact claim, add a line or paragraph-level locator where available:

`[TRACE: Source Path=<path>; Source Section=<heading>; Evidence Scope=<claim>]`

## Core Sources

| Source Path | Source Section | Use |
|---|---|---|
| `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` | `P0-01` … `P0-12` | Authoritative Owner requirements. |
| `01-OWNER/02-OWNER-DIRECTIONS-LATEST.txt` | Owner directions | Latest non-P0 Owner instructions; promotion requires governance. |
| `02-FOUNDATION/03-FOUNDATION-AUDIT.md` | Foundation baseline / Phase Gate | Foundation rules and required pre-implementation artifacts. |
| `02-FOUNDATION/04-TOOLCHAIN-RESEARCH.md` | Current version snapshot | Research evidence only; must be converted into BUILD-001. |
| `03-AUDIT/05-AUDIT-REPORT.md` | §3–§6 Findings | Historical primary audit findings. |
| `03-AUDIT/15-AUDIT-CORPUS-&-SOURCE-AUTHORITY.md` | Corpus / authority map | Source hierarchy and document authority. |
| `03-AUDIT/17-AUDIT-ARCHITECTURE-&-DATA.md` | §6 Confirmed Findings | Architecture/data blockers. |
| `03-AUDIT/19-AUDIT-DOCUMENTATION-&-GOVERNANCE.md` | §7–§9 | Governance findings and required next documents. |
| `03-AUDIT/20-PHASE-GATE-&-IMPLEMENTATION-REDINESS.md` | §1–§6 | Required artifacts, blockers, readiness matrix, verdict. |
| `03-AUDIT/21-FINAL-INDEPENDENT-AUDIT.md` | §3–§7 | Final findings, readiness matrix, verdict, required actions. |
| `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` | §9–§19 | Independent technical corroboration. |
| `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` | §24–§30 | Confirmed blockers, findings, closure exclusions, final conclusion. |

## Canonical Finding Traceability

### F-GOV-001

- `03-AUDIT/20-PHASE-GATE-&-IMPLEMENTATION-REDINESS.md` — `§1. REQUIRED ARTIFACTS`
- `03-AUDIT/20-PHASE-GATE-&-IMPLEMENTATION-REDINESS.md` — `§4. BLOCKERS`
- `03-AUDIT/21-FINAL-INDEPENDENT-AUDIT.md` — `§3. FINAL FINDINGS`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§24. CONFIRMED BLOCKERS`

### F-GOV-002

- `03-AUDIT/21-FINAL-INDEPENDENT-AUDIT.md` — `§3. FINAL FINDINGS`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§9. DATA MODEL AUDIT`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§11. TECHNICAL VERSION IDENTITY`

### F-GOV-003

- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§12. SECURITY AUDIT`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§13. BACKUP AUDIT`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§14. IMPORT AUDIT`
- `03-AUDIT/21-FINAL-INDEPENDENT-AUDIT.md` — `§4. FINAL READINESS MATRIX`

### F-GOV-004

- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§7. ARCHITECTURE AUDIT`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§15. LARGE TEXT AUDIT`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§18. TOOLCHAIN AUDIT`
- `03-AUDIT/20-PHASE-GATE-&-IMPLEMENTATION-REDINESS.md` — `§3. PHASE GATE ASSESSMENT`

### F-GOV-005

- `03-AUDIT/19-AUDIT-DOCUMENTATION-&-GOVERNANCE.md` — `§7. Confirmed Findings`
- `03-AUDIT/20-PHASE-GATE-&-IMPLEMENTATION-REDINESS.md` — `§5. READINESS MATRIX`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§26. MEDIUM FINDINGS`
- `05-INDEPENDENT-CROSS-AUDIT/Report-01.md` — `§29. MOST IMPORTANT OBSERVATION`

## Evidence Integrity Rule

Historical audit files are evidence records. Their numeric citations such as `[1]` are not rewritten in-place because doing so would alter the historical record without a deterministic reference bibliography. The canonical registry and this map are the machine-traceable closure layer. New governance artifacts must not introduce bare numeric references.
