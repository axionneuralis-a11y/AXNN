# AXN Note 1.0.0 — Authority Map

## Authority order

1. Latest Owner instruction
2. Approved Owner Decisions
3. Approved official project documents
4. Frozen technical specifications
5. Foundation documentation
6. Audit findings
7. Existing implementation
8. AI recommendation

## Current map

| Source | Authority | Status | Use |
|---|---:|---|---|
| `01-OWNER/02-OWNER-DIRECTIONS-LATEST.txt` | 1 | latest Owner direction | authoritative for new directions |
| `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` | 2 | approved P0 baseline, except P0-07 marked Owner Revision | authoritative Owner decisions |
| `02-FOUNDATION/03-FOUNDATION-AUDIT.md` | 5 | WORKING BASELINE | architectural/project baseline, not complete freeze |
| `02-FOUNDATION/04-TOOLCHAIN-RESEARCH.md` | 5/6 | research snapshot | external/toolchain evidence, not final authority |
| `03-AUDIT/*` | 6 | audit corpus | findings and evidence |
| `05-INDEPENDENT-CROSS-AUDIT/*` | 6 | independent cross-audit | corroboration / challenge |
| `06-GOVERNANCE/*` | governance control | active; gate not passed | closure/registry mechanics |
| `04-DOCUMENTATION-PLACEHOLDERS/*` | placeholder | not final specification | future Bible/Blueprint/Roadmap only |

## Explicit supersession / conflict handling

No conflict is to be silently resolved. Where a lower-authority document conflicts with a higher-authority source, the lower source must be marked superseded/obsolete/incorrect according to the governance process, while preserving the evidence trail.

## Important known conflict/clarification

`P0-07 — Full Backup` is `APPROVED — Owner Revision` in the Owner baseline. The audit corpus consistently treats the meaning of that status as insufficiently clarified for technical closure. This is therefore `OWNER DECISION REQUIRED`, not an AI-resolvable technical assumption.
