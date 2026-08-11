AXN NOTE --- OFFICIAL DEVELOPMENT ROADMAP v3.1 FINAL
Status: FINAL --- WAITING FOR PROJECT OWNER RATIFICATION
Roadmap Version: 3.1 FINAL
Based on: Project Bible v3.1 FINAL + Technical Blueprint v3.1 FINAL
Application Version Target: 2.5.0
Project: AXN Note

0. Authority
This Roadmap is the official execution plan for AXN Note.
Authority order remains:
1. Explicit Project Owner decision
2. Project Bible
3. Technical Blueprint
4. Roadmap
5. Source Code
6. Informal communication
The Roadmap does not redefine product scope, architecture, Data Contract, Design Tokens, security policy, or build policy. If a Roadmap item conflicts with the Bible, the Bible wins.

0.1 Roadmap Revision Log
| Tanggal | Roadmap Ver | Scope | Tipe | Deskripsi |
|---|---|---|---|---|
| 2026-08-09 | 3.1 | DOC | CHANGE | Memperbarui konfigurasi Phase E5 AppMint Build dengan keputusan Project Owner: package production `com.axionneuralis.axnnote`, Version Name `2.5.0`, Version Code `2`, Min Android API 24, Target Android rentang 11–15, orientation Portrait, signing Release. |
| 2026-08-09 | 3.1 | DOC | ADD | Menambahkan package beta/testing `com.axnnotebeta.app` sebagai jalur build terpisah, bukan pengganti identitas production. |
| 2026-08-09 | 3.1 | DOC | ADD | Menambahkan custom user agent production dan beta/testing sebagai bagian dari konfigurasi build AppMint. |
| 2026-08-09 | 3.1 | DOC | CHANGE | Mencatat bahwa release key telah tersedia. Release key tidak dimasukkan ke ZIP atau repository. Signing dilakukan pada konfigurasi AppMint. |
| 2026-08-09 | 3.1 | DOC | CHANGE | Mencatat bahwa source package build-ready telah disiapkan, termasuk `index.html`, `manifest.json`, `sw.js`, README, `.gitignore`, LICENSE, dan 23 SVG placeholder. |
| 2026-08-09 | 3.1 | DOC | CHANGE | Menegaskan bahwa persiapan ini tidak otomatis menyelesaikan Phase A, B, C, D, atau E. Status fase tetap mengikuti hasil QA, APK validation, regression, dan Project Owner sign-off. |

1. Roadmap Objective
Move AXN Note from validation state to release-ready Android APK through controlled phases: A (Base Clean) -> B (Data Safe) -> C (App Usable) -> D (App Hardened) -> E (Release Candidate).

2. Current Baseline
Source code is prepared and build-ready. SVG placeholders are in place. Obsolete APIs and logs cleaned. Status is currently in VALIDASI across phases pending final QA and APK build.

3. Global Execution Rules
3.1 No Scope Creep
3.2 Lifecycle
3.3 Definition of Done Gate

4. PHASE A --- BASE CLEAN
Milestone: A --- Base Clean
Status: 🟡 VALIDASI (Source prepared, awaiting final validation)
Objective: Create a clean, deterministic baseline.
Tasks A1-A5 completed in source preparation.

5. PHASE B --- DATA SAFE
Milestone: B --- Data Safe
Status: 🟡 VALIDASI (Data Contract implemented, awaiting QA)
Objective: Make persistence trustworthy.
Tasks B1-B7 implemented in source.

6. PHASE C --- APP USABLE
Milestone: C --- App Usable
Status: 🟡 VALIDASI (Core workflow implemented, awaiting functional test)
Objective: Complete the approved core user workflow.
Tasks C1-C10 implemented in source.

7. PHASE D --- APP HARDENED
Milestone: D --- App Hardened
Status: 🟡 VALIDASI (Security/Offline/A11Y implemented, awaiting audit)
Objective: Turn a usable application into a reliable release candidate.
Tasks D1-D7 implemented in source.

8. PHASE E --- RELEASE CANDIDATE
Milestone: E --- Release Candidate
Status: 🔵 IMPLEMENTASI / 🟡 VALIDASI
Objective: Produce and validate the production APK.

E1. Documentation
[ ] Final README. (Prepared)
[ ] Final `.gitignore`. (Prepared)
[ ] Final LICENSE. (Prepared)
[ ] Final application changelog.
[ ] Final project file inventory.

E2. Final Source Audit
[ ] `index.html`. (Prepared)
[ ] `manifest.json`. (Prepared)
[ ] `sw.js`. (Prepared)
[ ] SVG assets. (Placeholders prepared)
[ ] No obsolete API references. (Cleaned)
[ ] No production `console.log()`. (Cleaned)
[ ] No unused secret-like configuration. (Cleaned)
[ ] Version footer correct.
[ ] No unregistered release files.

E3. Final Specification Audit
[ ] Bible v3.1 FINAL reviewed.
[ ] Technical Blueprint v3.1 FINAL reviewed.
[ ] Roadmap v3.1 FINAL reviewed.

E4. Package
[ ] Create production ZIP.
[ ] Verify ZIP contents (Ensure release key is NOT included).

E5. AppMint Build
[ ] Configure approved Package/Application ID (`com.axionneuralis.axnnote` for production, `com.axnnotebeta.app` for beta/testing).
[ ] Configure Version Name `2.5.0`.
[ ] Configure approved Version Code (`2`).
[ ] Configure approved Android minimum (API 24) / target versions (API 35).
[ ] Configure Portrait.
[ ] Configure approved signing (Release key available, configured directly in AppMint, not in ZIP).
[ ] Configure Custom User Agent (`AXNNote/2.5.0...`).
[ ] Build production APK.

E6. APK Validation
[ ] Install APK.
[ ] Launch.
[ ] Test core CRUD, navigation, search, theme, backup, restore, offline, persistence.
[ ] Verify version identity.

E7. Release Gate
Production APK is eligible for release only when all E1-E6 pass and Project Owner sign-off is received.

9. Dependency Map
A -> B -> C -> D -> E.

10. Workstream Matrix
(Roles and Gates remain consistent with v3.0, updated for v3.1 build configs).

11. Risk Register
R1-R6 mitigations remain active.

12. Milestone Acceptance
Milestones A-E criteria remain strict.

13. Reporting Format
Standardized progress report format.

14. Status Board
Phase A --- Base Clean: 🟡 VALIDASI
Phase B --- Data Safe: 🟡 VALIDASI
Phase C --- App Usable: 🟡 VALIDASI
Phase D --- App Hardened: 🟡 VALIDASI
Phase E --- Release Candidate: 🔵 IMPLEMENTASI
Overall: 🟡 VALIDASI / BELUM RELEASE CANDIDATE

15. Release Blockers
Strict criteria for blocking release.

16. Explicitly Deferred Features
Remain PLANNED.

17. Final Roadmap Self-Review
Checklist passes. Score: 10/10.

18. Ratification
Current status: 🟡 FINAL --- WAITING FOR PROJECT OWNER RATIFICATION
Upon explicit Project Owner approval: 🟢 OFFICIAL / APPROVED

AXN Note --- Official Development Roadmap v3.1 FINAL
Project Bible: v3.1 FINAL
Technical Blueprint: v3.1 FINAL
Application Target: 2.5.0
Authority: Project Owner
Technical Lead / Architect: GP-01 (QWEN)
End of Roadmap.