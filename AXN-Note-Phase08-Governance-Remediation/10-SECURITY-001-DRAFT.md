# SECURITY-001 — Threat Model and Security Architecture
Status: **DRAFT — NOT FROZEN**

## Evidence basis

- `01-OWNER/01-OWNER-DECISIONS-BASELINE.md` P0-08
- `02-FOUNDATION/03-FOUNDATION-AUDIT.md` §10
- `05-INDEPENDENT-CROSS-AUDIT/01-AUDIT-REPORT.md` §12

## Owner-backed principle

AXN Note uses a Layered Security Architecture.

## Required analysis

- assets
- trust boundaries
- threat actors
- attack surfaces
- threats
- mitigations
- data-at-rest
- local storage
- backup
- import
- attachments
- logs
- secrets
- key management
- recovery
- failure modes
- explicit security limitations

## Evidenced design direction

- use platform/established cryptographic primitives
- no custom cryptography
- Android Keystore for key protection
- encrypted local data where justified by threat model
- encrypted backup representation
- optional app lock/device authentication
- log redaction
- recovery handling when keys/files/backup components fail

## Rule

The threat model must precede final encryption implementation. No production encryption implementation is authorized by this document.
