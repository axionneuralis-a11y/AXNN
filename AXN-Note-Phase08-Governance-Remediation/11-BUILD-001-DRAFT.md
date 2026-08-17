# BUILD-001 — Build and Toolchain Specification
Status: **DRAFT — NOT VERIFIED / NOT FROZEN**

## Evidence basis

- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §11
- `02-FOUNDATION/04-TOOLCHAIN-RESEARCH.md`
- `05-INDEPENDENT-CROSS-AUDIT/01-AUDIT-REPORT.md` §18

## Repository-stated snapshot

The Foundation baseline records:
- AGP 9.3.0
- Gradle 9.5.0
- JDK 17
- compileSdk 37
- targetSdk 37
- Kotlin 2.4.10 as the referenced stable line in the audit snapshot
- Compose/current stable BOM direction
- Room
- build/test/lint/CI expectations

These are repository facts/research claims, not a final verified build contract.

## Verification gate

Required sequence:
1. clean checkout
2. clean Gradle build
3. unit tests
4. instrumented tests if the environment supports them
5. lint
6. reproducibility check

## Rule

No toolchain combination is frozen solely because it is described as "current stable". A real clean build must establish the repository fact.

## Current status

`TOOLCHAIN = NOT VERIFIED`
