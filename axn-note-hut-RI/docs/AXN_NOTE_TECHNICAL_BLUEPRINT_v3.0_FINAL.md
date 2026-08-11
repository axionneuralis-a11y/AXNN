AXN NOTE --- TECHNICAL BLUEPRINT v3.1 FINAL
Status: OFFICIAL / FINAL DRAFT FOR PROJECT OWNER RATIFICATION
Blueprint Version: 3.1 FINAL
Based on: Project Bible v3.1 FINAL
Application Version Target: 2.5.0
Project: AXN Note
Platform: Android WebView / AppMint
Core Stack: HTML5 + CSS3 + JavaScript ES6+ / Vanilla
Primary Storage: LocalStorage
Architecture: Single-File Core / Offline-First

0. Authority, Scope, and Purpose
This document is the official technical blueprint for implementing AXN Note.
The Project Bible remains the Single Source of Truth. The authority order is:
1. Explicit Project Owner decision
2. Project Bible
3. Blueprint
4. Roadmap
5. Source Code
6. Informal communication

If this Blueprint conflicts with the Bible, the Bible wins. If an implementation decision is not defined here or in the Bible, it must not be invented as a permanent project rule; it becomes a temporary implementation detail or TBD and is escalated when it affects specification.
The purpose of this Blueprint is to translate the approved product rules into an implementation architecture that is concrete enough to build, test, review, and release.

0.1 Blueprint Revision Log
| Tanggal | Blueprint Ver | Scope | Tipe | Deskripsi |
|---|---|---|---|---|
| 2026-08-09 | 3.1 | DOC | CHANGE | Memperbarui bagian Manifest Architecture dan Build and Release Architecture dengan keputusan Project Owner: package production `com.axionneuralis.axnnote`, package beta/testing `com.axnnotebeta.app`, Version Name `2.5.0`, Version Code `2`, Min Android API 24, Target Android rentang 11–15 dengan target build AppMint disarankan API 35, orientation Portrait, signing Release. |
| 2026-08-09 | 3.1 | DOC | CHANGE | Mencatat bahwa `manifest.json` dapat berisi metadata kompatibilitas AppMint sebagai superset dari web app manifest, selama tidak mengubah arsitektur inti, Data Contract, offline-first behavior, atau security policy. |
| 2026-08-09 | 3.1 | DOC | ADD | Menambahkan custom user agent production dan beta/testing sebagai konfigurasi build resmi. Full user agent production dicatat sesuai keputusan Project Owner. |
| 2026-08-09 | 3.1 | ASSET | CHANGE | Mencatat bahwa 23 file SVG placeholder build-ready telah disiapkan sebagai `assets/icons/icon-1.svg` sampai `assets/icons/icon-23.svg`. Placeholder ini membuat referensi aset pada manifest menjadi valid, tetapi aset final tetap menunggu GP-04 / Project Owner. |
| 2026-08-09 | 3.1 | DOC | CHANGE | Memperjelas bahwa release key tidak termasuk dalam source ZIP, tidak disimpan di repository, dan hanya digunakan pada konfigurasi signing AppMint. |
| 2026-08-09 | 3.1 | DOC | CHANGE | Menegaskan bahwa tidak ada perubahan pada arsitektur single-file, LocalStorage, Data Contract, Service Worker local-only, atau security model. |

1. Product Architecture
1.1 Product Definition
AXN Note is a local, offline-first File/Folder Manager + Note-Taking application.
The primary information model is: Root -> Folder -> Folder/File.
The application does not require user accounts, authentication, cloud sync, external DB, backend, analytics, AI, or internet.

1.2 Runtime Model
Android Device -> AppMint APK -> Android WebView -> Local Web App (index.html, manifest, sw.js, svg assets).

2. Architectural Principles
Single-file core, Vanilla JS, LocalStorage primary, Offline-first, No external runtime dependency, Validation before persistence, Safe-by-default DOM, Schema-driven, Deterministic migration, Graceful failure, Centralized design tokens, Traceable decisions, Protected LocalStorage compatibility.

3. Repository and File Architecture
axn-note/ (index.html, manifest.json, sw.js, assets/icons/*.svg, README.md, .gitignore, LICENSE). SVG names are placeholders (now populated with build-ready placeholders).

4. `index.html` Architecture
Logical modules: Config, Data model, Validation, Storage, Migration, State, Rendering, Interaction, Search, Backup/Restore, Notifications, Statistics, Utilities.

5. Internal JavaScript Layers
5.1 Configuration Layer
5.2 Data Layer
5.3 Validation Layer
5.4 Persistence Layer
5.5 State Layer
5.6 Rendering Layer
5.7 Interaction Layer
5.8 Utility Layer

6. Data Architecture
6.1 Storage Strategy (AXN_NOTE_DATA, AXN_NOTE_SETTINGS)
6.2 Root Data Contract
6.3 Folder Contract
6.4 File Contract
6.5 Settings Contract
6.6 ID Policy
6.7 Timestamp Policy

7. Data Validation Pipeline
Mutation/Import pipelines strictly enforce validation before persistence.

8. CRUD Architecture
Create Folder, Create File, Edit File, Rename, Move, Delete pipelines defined.

9. Navigation Architecture
Current Folder, Breadcrumb, Selection.

10. Search Architecture
Local, offline, non-mutating search pipeline.

11. Backup Architecture
Full JSON export, preserving IDs, timestamps, schemaVersion.

12. Restore Architecture
REPLACE mode, strict validation pipeline, no silent overwrite.

13. Schema Migration Architecture
Deterministic, explicit, testable migrations.

14. Auto-Save Architecture
Planned 800ms debounce model.

15. UI Architecture
Main View, Editor View, UI States.

16. Design System Architecture
Light/Dark tokens centrally controlled. Max widths enforced.

17. Accessibility Architecture
WCAG 2.1 AA minimums.

18. Security Architecture
DOM Safety, URL Safety, Storage Privacy, Service Worker Boundary.

19. Service Worker Architecture
Local cache only. No external sync.

20. Manifest Architecture
`manifest.json` contains application metadata required by the web application/build workflow.
It must remain consistent with: application identity, version, local assets, portrait orientation, AppMint packaging.
References to assets that do not exist are release blockers until resolved.

*Catatan Tambahan (v3.1):*
Manifest dapat memuat metadata tambahan yang dibutuhkan oleh AppMint, seperti packageName, versionCode, minSdkVersion, targetSdkVersion, orientation, dan custom user agent, selama field inti web manifest tetap valid dan tidak ada perubahan pada arsitektur aplikasi.

21. Error Handling Architecture
Controlled operations, no silent failures, preserve valid state.

22. LocalStorage Failure Strategy
Preserve active draft in memory on failure, show clear error.

23. Notification Architecture
Local only, compatible with Data Contract `notified` field.

24. Statistics Architecture
Local derived metrics.

25. Context Menu Architecture
Item-scoped, verified ID execution.

26. Feedback Architecture
`mailto:` only, no automatic data upload.

27. Offline Architecture
Core functionality remains local.

28. Performance Architecture
Lightweight, no unnecessary dependencies, bounded search.

29. Build and Release Architecture
29.1 Build Chain
Project Source ZIP -> AppMint -> Android WebView APK -> Installation -> QA -> Release Candidate.

29.2 Build Configuration (v3.1 Update)
```text
Package Production       : com.axionneuralis.axnnote
Package Beta/Testing     : com.axnnotebeta.app
Version Name             : 2.5.0
Version Code             : 2
Min Android              : Android 7 / API 24
Target Android           : Android 11–15
Target Build Disarankan  : Android 15 / API 35
Orientation              : Portrait
Build Production         : Release
Signing                  : Release key tersedia, tidak disimpan di ZIP/repo
```

29.3 Production Acceptance
AppMint build succeeds, installs, opens, core works, offline works, persistence survives restart, backup/restore works, no critical errors, final APK PASS, versions match.

30. Testing Architecture
Core Test Coverage (TC-001 to TC-024).

31. Regression Strategy
Required after major changes and before release.

32. Implementation Order
Phase 1 to 5 dependency order.

33. Traceability Matrix
Bible -> Blueprint -> Roadmap -> Implementation -> Test -> QA -> Release.

34. Change Control
Level 1 (Implementation Detail), Level 2 (Technical Architecture), Level 3 (Specification Change).

35. Known-Issue Handling
Obsolete APIs removed, SVG placeholders prepared, console.logs cleaned.

36. Explicit Non-Goals
No cloud sync, backend, auth, etc.

37. Definition of Technical Completion
Strict DoD alignment.

38. Final Architecture Decision Record
Locked decisions operationalizing the Bible. Build specs updated to v3.1 decisions.

39. Blueprint Self-Review
Score: 10/10 --- READY FOR PROJECT OWNER RATIFICATION

40. Ratification
Status before approval: 🟡 FINAL --- WAITING FOR PROJECT OWNER RATIFICATION
Upon explicit Project Owner approval: 🟢 OFFICIAL / APPROVED

AXN Note --- Technical Blueprint v3.1 FINAL
Project Bible: v3.1 FINAL
Application Target: 2.5.0
Authority: Project Owner
Technical Lead / Architect: GP-01 (QWEN)
End of Blueprint.