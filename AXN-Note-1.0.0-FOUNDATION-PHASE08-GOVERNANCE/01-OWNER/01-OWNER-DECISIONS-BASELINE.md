# AXN Note v3 — Owner Decisions Baseline

**Document Status:** Owner-Approved Baseline  
**Decision Set:** P0 Owner Decisions  
**Completed:** 2026-08-15  
**Purpose:** Menjadi sumber acuan resmi selama audit, arsitektur, dokumentasi, dan implementasi AXN Note v3.

> **Version label supersede:** Nomenklatur `v3` pada dokumen ini digantikan oleh **AXN Note 1.0.0** per keputusan Owner tanggal 2026-08-16. Isi 12 keputusan P0 tetap berlaku penuh; yang berubah hanya label versi dan identitas release line.


> **Important:** Dokumen ini berisi keputusan Owner yang telah disetujui. Implementasi teknis final tetap harus melalui consistency audit, dependency audit, security audit, dan validasi terhadap dokumen proyek resmi.

---

## P0-01 — Android Compatibility Target

**Status:** APPROVED — 100%

### Decision

AXN Note v3 secara resmi mendukung:

**Android 8.0 Oreo / API 26 dan lebih baru.**

### Rules

- `minSdk` target: API 26.
- Target/compile SDK mengikuti SDK Android modern yang digunakan saat implementasi.
- Compatibility di bawah API 26 tidak menjadi target resmi AXN Note v3.
- Arsitektur dan testing harus memperlakukan API 26 sebagai baseline compatibility.

### Rationale

Keputusan ini menyeimbangkan device coverage dengan maintainability, security, API availability, dan kompleksitas compatibility.

---

## P0-02 — Analytics & Data-Exit Policy

**Status:** APPROVED — 100%

### Decision

AXN Note v3 menggunakan prinsip:

**Privacy-first + Offline-first + User-owned data.**

### Rules

- Isi note tidak dikirim untuk analytics.
- Judul note, attachment, clipboard, teks yang sedang diketik, dan data pribadi pengguna tidak boleh dikirim sebagai telemetry.
- Technical telemetry, jika nantinya diperlukan, harus minimal, transparan, dan tidak mengandung user content.
- User harus dapat melakukan export data tanpa bergantung pada server AXION Neuralis.
- User harus dapat import kembali data yang telah diekspor.
- AXN Note tidak boleh menciptakan vendor lock-in terhadap data pengguna.
- Export dan backup adalah mekanisme yang berbeda.
- Data portability adalah requirement produk.

### Principle

**User owns the data.**

---

## P0-03 — Trash / Delete Lifecycle

**Status:** APPROVED — 100%

### Decision

Delete biasa menggunakan lifecycle:

**Active → Trash → Restore / Permanent Delete**

### Rules

- Delete biasa tidak langsung menghancurkan data.
- Deleted notes masuk ke Trash.
- User dapat Restore.
- User dapat Delete Permanently kapan saja.
- User dapat Empty Trash.
- Default automatic purge setelah **30 hari**.
- 30 hari adalah batas auto-purge, bukan masa tunggu wajib.
- Permanent deletion harus menangani note, attachment, metadata, dan data terkait.
- Tidak boleh meninggalkan orphaned user data.
- Attachment mengikuti lifecycle note.

### Lifecycle Examples

`Active → Trash → Restore → Active`

`Active → Trash → Permanent Delete`

`Active → Trash → 30 days → Permanent Delete`

---

## P0-04 — Editor v3.0 Scope

**Status:** APPROVED — 100%

### Decision

AXN Note v3 menggunakan:

**Structured Rich Text Editor dengan controlled scope.**

### Core Scope

Editor diprioritaskan untuk:

- Plain text.
- Rich text dasar.
- Heading.
- Bold.
- Italic.
- Underline.
- Strikethrough.
- Bulleted list.
- Numbered list.
- Checklist/task list.
- Quote.
- Code block / monospace.
- Hyperlink.
- Undo/redo.
- Find/search.
- Select/copy/paste.
- Keyboard-friendly editing.
- Large-text handling.
- Autosave.
- Crash-safe recovery.
- Offline editing.

### Explicit Non-Goal

AXN Note bukan full word processor.

Tidak menjadi prioritas core v3:

- Spreadsheet-style table kompleks.
- Page-layout system seperti word processor.
- Advanced typography.
- Mail merge.
- Track changes.
- Real-time collaborative editing.

### Architectural Principle

Structured document model lebih diutamakan daripada menyimpan seluruh dokumen hanya sebagai raw HTML.

---

## P0-05 — Arbitrary File / Attachment Scope

**Status:** APPROVED — 100%

### Decision

AXN Note v3 mendukung:

**Arbitrary user-selected file attachments sebagai first-class note assets.**

AXN Note tetap merupakan aplikasi catatan, bukan file manager.

### Rules

- User secara eksplisit memilih file untuk dilampirkan.
- AXN Note tidak meminta broad filesystem access secara default.
- Berbagai tipe file dapat disimpan sebagai attachment.
- Native preview/rendering hanya tersedia untuk format yang didukung.
- File yang tidak didukung tetap dapat:
  - disimpan;
  - diekspor;
  - dibuka melalui aplikasi eksternal;
  - dihapus.
- Attachment memiliki relationship dengan note.
- Attachment mengikuti lifecycle Trash/Restore/Permanent Delete.
- Attachment mengikuti kebijakan Backup dan Export.

### Attachment Metadata

Arsitektur dapat menyimpan informasi seperti:

- Attachment ID.
- Parent Note ID.
- Original filename.
- MIME type.
- Size.
- Created time.
- Modified time.
- Checksum/hash.
- Storage reference.

### Principle

**Storage support ≠ native rendering support.**

---

## P0-06 — ZIP Import Conflict Behavior

**Status:** APPROVED — 100%

### Decision

Import AXN Note v3 bersifat:

**Non-destructive by default.**

### Rules

- Import tidak boleh melakukan silent overwrite.
- Stable unique ID digunakan sebagai identity utama.
- Judul note bukan primary identity.
- Judul yang sama tidak otomatis berarti conflict.
- ID yang sama dapat menunjukkan kemungkinan bahwa data berasal dari entity yang sama.
- Conflict harus dideteksi dan ditangani secara eksplisit.
- Pilihan resolution dapat mencakup:
  - Keep Existing.
  - Import Version.
  - Keep Both.
  - Skip.
  - Merge jika aman dan didukung.
- Import harus menjaga data integrity dan atomicity.
- Import bukan replace operation.

### AXN Identifier / Namespace

AXN Note akan menggunakan identifier/namespace khusus sehingga aplikasi dapat mengenali struktur identity AXN Note.

Namun:

**Format ID saja bukan bukti authenticity.**

Identity system akan menggunakan kombinasi:

- Stable unique ID.
- Identifier namespace/format.
- Format/schema metadata.
- Source/origin metadata.
- Integrity verification.
- Authenticity/signature jika nantinya dibutuhkan.

### Import Principle

**IMPORT ≠ REPLACE**

**CONFLICT ≠ ERROR**

---

## P0-07 — Full-App Backup Scope

**Status:** APPROVED — Owner Revision

### Decision

Full Backup harus mencakup:

**seluruh state pengguna yang diperlukan untuk melakukan recovery aplikasi secara lengkap, termasuk Trash.**

### Included

- Active notes.
- Note contents.
- Titles.
- Timestamps.
- IDs.
- Metadata.
- Attachments.
- Attachment metadata.
- Trash.
- User preferences/configuration yang relevan.
- Schema/version metadata.
- Integrity information.

### Excluded

- Cache yang dapat diregenerasi.
- Temporary files.
- Analytics/telemetry.
- Data non-user yang tidak diperlukan untuk recovery.

### Critical Rule — Trash

Trash **WAJIB termasuk dalam Full Backup**.

Jika sebuah note berada di Trash ketika backup dibuat:

`Trash → Backup → Restore → Trash`

Bukan otomatis menjadi active note.

### Backup Format

Backup harus:

- Versioned.
- Self-describing.
- Memiliki integrity verification.
- Dapat divalidasi.
- Dirancang untuk restore secara konsisten.

### Separation

**Export = portability**

**Backup = recovery**

**Android system backup = additional system-level protection**

AXN Note tidak boleh bergantung sepenuhnya pada Android Auto Backup.

Encryption/security detail ditetapkan melalui P0-08.

---

## P0-08 — Encryption & Security Level

**Status:** APPROVED — 100%

### Decision

AXN Note v3 menggunakan:

**Layered Security Architecture.**

### Security Layers

- Android application sandbox.
- Secure local storage practices.
- Encryption-at-rest untuk data yang relevan.
- Encrypted full backup security model.
- Secure Android key management.
- Optional App Lock.
- Android device authentication/biometric jika tersedia.
- Optional password/PIN mechanism.
- Strict protection terhadap diagnostic/log leakage.

### Rules

- AXN Note tidak membuat algoritma kriptografi sendiri.
- Cryptographic primitives harus berasal dari standar/library terpercaya.
- Key management harus menggunakan mekanisme secure storage Android yang sesuai.
- User content tidak boleh masuk diagnostic logs secara default.
- AXN Note tidak membutuhkan AXION account untuk penggunaan lokal.
- Security harus tetap bekerja secara offline.
- E2EE bukan requirement v3 selama tidak ada cloud synchronization.
- Security harus mempertahankan recoverability.
- Jangan membuat mekanisme security yang mudah menyebabkan user kehilangan data secara permanen.

### Authentication Principle

AXN Note tidak perlu membuat sistem biometric sendiri.

Jika perangkat mendukung biometric/device authentication, gunakan mekanisme autentikasi Android.

Password/PIN khusus aplikasi tetap dapat dipertimbangkan sebagai mekanisme opsional.

### Security Principle

**Strong security without destroying recoverability.**

---

## P0-09 — Software License

**Status:** APPROVED — 100%

### Decision

Source code AXN Note v3 menggunakan:

**Apache License 2.0**

dengan syarat dependency/license audit dilakukan sebelum release final.

### Rules

- Dependency licenses harus diaudit.
- Dependency harus kompatibel dengan licensing strategy proyek.
- Source code berada di bawah Apache-2.0.
- AXION Neuralis branding/trademark/identity dipisahkan dari software license.

### Protected Identity

Apache-2.0 atas source code tidak memberikan hak otomatis untuk menggunakan:

- Nama AXION Neuralis.
- Nama AXN Note.
- Logo AXION Neuralis.
- Logo AXN Note.
- Icon resmi.
- Branding resmi.
- Identitas resmi produk.

Fork/derivative project harus menggunakan identitas mereka sendiri kecuali memperoleh izin dari AXION Neuralis.

Software license tidak boleh ditafsirkan sebagai endorsement atau produk resmi AXION Neuralis.

### Principle

**Code can be open; official identity remains controlled.**

---

## P0-10 — Version Identity & Repository Governance

**Status:** APPROVED — 100%

### Versioning Decision

Public application version menggunakan:

**Semantic Versioning: MAJOR.MINOR.PATCH**

Contoh:

- `3.0.0`
- `3.1.0`
- `3.1.1`

### Independent Version Identities

AXN Note tidak menggunakan satu nomor versi untuk seluruh sistem.

Version identity dapat dipisahkan menjadi:

- Application/Product Version.
- Database Schema Version.
- Backup Format Version.
- Export Format Version.
- Document/Editor Schema Version.
- Build Identifier.

### Purpose

Migration dan compatibility system harus dapat mengetahui:

`source version → target version`

tanpa bergantung hanya pada application version.

### Git Repository Governance

Repository GitHub menggunakan lebih dari satu branch sesuai lifecycle development.

Branch dapat mencakup konsep seperti:

- `main` — stable/release code.
- `develop` — active development/integration.
- `audit` — audit, QA, security review, validation.
- `beta` — beta/pre-release testing.

### Branch Principle

Branch tidak dibuat hanya untuk terlihat banyak.

Setiap branch harus memiliki fungsi yang jelas dan lifecycle yang terdefinisi.

### Release Tags

Official releases menggunakan Git tags/releases.

Contoh:

- `v3.0.0`
- `v3.0.1`
- `v3.1.0`

Pre-release dapat menggunakan identity seperti:

- `v3.0.0-beta.1`
- `v3.0.0-rc.1`

### Separation

**Branch = development workflow**

**Tag/Release = snapshot identity**

**Version number = product/format identity**

`main` tidak boleh menjadi tempat eksperimen langsung.

---

## P0-11 — Large-Text Performance Target

**Status:** APPROVED — 100%

### Decision

AXN Note v3 harus dirancang dan diuji untuk large-text workloads.

### Target

**Normal workload**
- sekitar 100.000 karakter.

**Large workload**
- sekitar 500.000 karakter.

**Stress target**
- sekitar 1.000.000 karakter.

### Required Benchmark Areas

Pengujian harus mencakup:

- Opening/loading.
- Editing/typing.
- Scrolling.
- Search.
- Save.
- Autosave.
- Undo/redo.
- Export.

### Device Coverage

Benchmark harus dilakukan pada perangkat yang representatif, termasuk perangkat kelas bawah/menengah yang masih berada dalam target Android API 26+.

### Principle

Target tersebut adalah:

**Engineering / QA acceptance criteria**

bukan janji performa absolut untuk setiap perangkat.

### UX Requirement

Large note tidak cukup hanya "tidak crash".

Large note harus tetap:

**usable, responsive, dan aman dari data loss.**

---

## P0-12 — Navigation / UI Direction

**Status:** APPROVED — 100%

### Decision

AXN Note v3 menggunakan:

**Adaptive + Content-first UI**

dengan information architecture yang konsisten di berbagai ukuran layar.

### Mobile

Navigasi utama harus sederhana dan predictable, misalnya:

- Notes.
- Search.
- Trash.
- Settings.

### Larger Screens

Layar lebih besar dapat menggunakan:

- Navigation rail.
- Sidebar.
- Multi-pane layout.
- Note list + editor.

Namun tetap menggunakan satu information architecture, bukan dua aplikasi berbeda.

### Editor

Editor adalah pusat pengalaman ketika user membuka note.

UI harus memprioritaskan:

**Content > unnecessary controls**

Toolbar dan controls harus context-aware dan tidak memenuhi layar tanpa alasan.

### Navigation Principles

- Predictable navigation.
- Consistent back behavior.
- Minimal cognitive load.
- Autosave meminimalkan unnecessary unsaved-change dialogs.
- Delete → Trash.
- Attachment tetap berada dalam konteks note.
- Search mudah diakses.
- Settings menjadi pusat konfigurasi.

### Responsive Direction

Pendekatan:

**Mobile-first + adaptive**

bukan mobile UI yang sekadar diperbesar untuk layar besar.

### Event / Theme Rule

Event/theme hanya mengubah:

**Presentation Layer**

dan tidak mengubah:

- Core information architecture.
- Core navigation.
- Core data model.
- Fundamental usability.

Contoh event dapat mengubah visual theme atau greeting, tetapi Notes tetap Notes dan Trash tetap Trash.

### UX Principles

- Content-first.
- Minimal cognitive load.
- Consistent navigation.
- Adaptive layout.
- Accessibility-aware.
- Dark/light/system theme.
- Event-aware presentation.
- No unnecessary animation.
- UI melayani note-taking, bukan sekadar visual spectacle.

### Settings — About & Transparency

Settings harus menyediakan area informasi yang mudah diakses user, termasuk konsep:

**About AXN Note**
- Nama aplikasi.
- Versi.
- Build/version information.
- Informasi AXION Neuralis.
- Repository/project information.
- License information.

**Privacy & Data**
- Cara data disimpan.
- Data yang tidak dikirim.
- Analytics/telemetry policy.
- Data export.
- Backup information.

**Security**
- Security architecture secara ringkas.
- Encryption information.
- App Lock/device authentication.
- Backup encryption information.
- Security limitations yang relevan.

**Open Source & Licenses**
- Apache-2.0.
- Third-party licenses.
- Attribution.

### Transparency Principle

Informasi kepada user harus:

- jelas;
- jujur;
- dapat diverifikasi oleh implementasi;
- tidak menggunakan klaim keamanan absolut seperti "100% aman".

---

# Cross-P0 Principles

Ke-12 keputusan di atas harus dibaca sebagai satu sistem, bukan 12 keputusan terpisah.

Prinsip lintas keputusan:

1. **Privacy-first**
2. **Offline-first**
3. **User-owned data**
4. **Data portability**
5. **Non-destructive operations**
6. **Recoverability**
7. **Security without unnecessary complexity**
8. **Maintainability**
9. **Controlled scope**
10. **Content-first UX**
11. **Accessibility and usability**
12. **No unnecessary vendor lock-in**
13. **No silent data destruction**
14. **No silent overwrite**
15. **No unnecessary filesystem access**
16. **AXN Note remains a note application, not a file manager or full word processor**
17. **Brand identity remains distinct from open-source code licensing**
18. **Versioning must remain explicit and migration-aware**

---

# Mandatory Consistency Audit Before Implementation

Sebelum keputusan ini digunakan untuk mengubah kode, audit harus memverifikasi minimal:

- P0-01 kompatibel dengan dependency dan Gradle/toolchain.
- P0-02 konsisten dengan analytics implementation.
- P0-02 konsisten dengan backup/export.
- P0-03 konsisten dengan database/storage lifecycle.
- P0-03 konsisten dengan backup/restore.
- P0-04 konsisten dengan document schema.
- P0-05 konsisten dengan storage architecture.
- P0-05 konsisten dengan Trash/Backup/Export.
- P0-06 konsisten dengan data identity dan migration.
- P0-06 konsisten dengan ZIP/container format.
- P0-07 konsisten dengan restore architecture.
- P0-08 konsisten dengan backup/export/key management.
- P0-09 konsisten dengan seluruh dependency licenses.
- P0-10 konsisten dengan migration/versioning strategy.
- P0-10 konsisten dengan GitHub workflow.
- P0-11 dapat diuji secara objektif.
- P0-12 konsisten dengan seluruh UX requirements.
- Tidak ada contradiction antar-P0.
- Tidak ada requirement yang belum memiliki owner decision.
- Tidak ada implementasi lama yang dianggap benar hanya karena sudah ada di codebase.

---

# Authority Rule

Selama audit dan implementasi:

**Owner Decisions Baseline > asumsi developer/AI > implementasi lama.**

Jika codebase, Blueprint, Roadmap, Bible, atau dokumen lama bertentangan dengan Owner Decision yang telah disetujui, konflik harus dicatat dan diselesaikan melalui audit.

**Jangan mengubah Owner Decision secara diam-diam.**

Jika diperlukan perubahan terhadap P0, keputusan tersebut harus kembali kepada Owner untuk approval.

---

# Current Decision State

**P0 Decisions Completed: 12 / 12**

**Owner Approval: Complete**

**Next Phase: P0 Consistency Audit**

**Implementation Status: Not yet authorized by this document**

Dokumen ini adalah baseline keputusan, bukan instruksi untuk langsung melakukan coding.
