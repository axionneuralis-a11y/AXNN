Saya akan membuatkan README.md dan .gitignore yang disesuaikan dengan 3 dokumen (Roadmap, Blueprint, dan Bible) yang Anda berikan.

---

README.md

```markdown
# 🌿 AXNN - AXN Note

**All-in-One Productivity Suite** • Native Android • Editor Kode Portabel

[![Version](https://img.shields.io/badge/version-v1.1.0--dev-green.svg)](https://github.com/axnnote/axnn)
[![Platform](https://img.shields.io/badge/platform-Android-green.svg)]()
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)]()
[![Kivy](https://img.shields.io/badge/kivy-2.3.0-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/build-Buildozer-brightgreen.svg)]()

---

## 📖 Tentang AXNN

AXNN (AXN Note) adalah aplikasi produktivitas all-in-one native Android yang menggabungkan:

- 📝 **Catatan** — CRUD lengkap dengan folder & filter
- ✅ **To-Do List** — Manajemen tugas dengan prioritas & deadline
- 📁 **Folder System** — Organisasi konten hierarkis
- 🧮 **Kalkulator** — Operasi dasar + riwayat
- 📅 **Kalender** — Indikator tugas/catatan per tanggal
- 🔔 **Notifikasi** — Pengingat & reminder
- 💻 **Editor Kode** — Syntax highlighting + autocomplete (Fitur Unggulan v1.1.0)
- 📤 **Export Multi Format** — 20+ format teks

Dibangun dengan **Kivy + Buildozer**, berjalan native di Android 10+ (API 29-34).

---

## 🎯 Visi & Misi

**Visi:** Menjadi aplikasi catatan & produktivitas all-in-one ringan untuk Android, yang menggabungkan fungsi catatan, tugas, kalender, kalkulator, dan editor kode portabel dalam satu paket native tanpa iklan mengganggu.

**Misi v1.1.0:**
1. Migrasi penuh dari AppMint (HTML/JS) ke Kivy + Buildozer (Python)
2. Pertahankan 100% fitur v1.0.0
3. Tambahkan Editor Kode Multibahasa dengan Autocomplete + Syntax Highlighting
4. Tema baru Green Matrix
5. Export multi format ke storage Android

---

## 🗺️ Roadmap

| Milestone | Waktu | Target | Status |
|-----------|-------|--------|--------|
| M1 Setup Proyek Dasar | Minggu 1 (05-11/08) | Struktur folder, database, tema dasar, APK pertama | ⚪ |
| M2 Migrasi Fitur Lama 50% | Minggu 2 (12-18/08) | Catatan, Todo, Folder, Kalkulator, Kalender | ⚪ |
| M3 Migrasi Fitur Lama 100% | Minggu 3 (19-25/08) | SEMUA fitur v1.0.0 berfungsi | ⚪ |
| M4 Fitur Baru Dasar | Minggu 4 (26/08-01/09) | Export Multi Format, File Picker, Tema Matrix | ⚪ |
| M5 Editor Kode Inti | Minggu 5-6 (02-15/09) | Widget Editor, Syntax Highlight, Autocomplete | ⚪ |
| M6 Integrasi Storage Editor | Minggu 6 (09-15/09) | Save ke Storage, Auto Save | ⚪ |
| M7 Testing, Polishing & Rilis | Minggu 7-8 (16-30/09) | Bugfix, optimasi APK, rilis | ⚪ |

**Target Rilis:** 30 September 2026

---

## 🏗️ Struktur Proyek

```

AXNN/
│
├── main.py                  # Entry point aplikasi
├── buildozer.spec           # Konfigurasi build Android
├── requirements.txt         # Dependencies Python
│
├── models/                  # 📦 Model Data (Tim B)
│   ├── note_model.py
│   ├── todo_model.py
│   ├── folder_model.py
│   ├── calculator_model.py
│   ├── notification_model.py
│   ├── file_model.py
│   └── setting_model.py
│
├── controllers/             # 🧠 Controller & Logika (Tim B)
│   ├── note_controller.py
│   ├── todo_controller.py
│   ├── folder_controller.py
│   ├── calculator_controller.py
│   ├── notification_controller.py
│   ├── settings_controller.py
│   ├── stats_controller.py
│   └── editor_controller.py
│
├── screens/                 # 📱 Layar Aplikasi (Tim C & Tim D)
│   ├── home_screen.py
│   ├── notes_screen.py
│   ├── todos_screen.py
│   ├── calculator_screen.py
│   ├── calendar_screen.py
│   ├── settings_screen.py
│   ├── folder_screen.py
│   ├── note_detail_screen.py
│   ├── todo_detail_screen.py
│   ├── notification_screen.py
│   ├── backup_screen.py
│   └── editor_screen.py     # (Tim D)
│
├── kv_files/                # 🎨 UI Kivy Layout (Tim C & Tim D)
│   ├── main.kv
│   ├── home_screen.kv
│   ├── notes_screen.kv
│   ├── todos_screen.kv
│   ├── calculator_screen.kv
│   ├── calendar_screen.kv
│   ├── settings_screen.kv
│   ├── folder_screen.kv
│   ├── note_detail_screen.kv
│   ├── todo_detail_screen.kv
│   ├── notification_screen.kv
│   ├── backup_screen.kv
│   ├── editor_screen.kv    # (Tim D)
│   └── code_editor.kv      # (Tim D)
│
├── components/              # 🧩 Komponen UI (Tim C & Tim D)
│   ├── bottom_nav.py
│   ├── note_card.py
│   ├── todo_item.py
│   ├── calendar_widget.py
│   ├── badge_notification.py
│   ├── export_dialog.py
│   ├── create_folder_dialog.py
│   ├── create_file_dialog.py
│   ├── search_bar.py
│   ├── confirmation_dialog.py
│   └── code_editor.py       # (Tim D)
│
├── utils/                   # 🔧 Utility & Helpers
│   ├── database.py          # (Tim B)
│   ├── helpers.py           # (Tim B)
│   ├── constants.py         # (Tim B)
│   ├── file_picker.py       # (Tim B)
│   ├── theme.py             # (Tim C)
│   ├── syntax_highlighter.py # (Tim D)
│   ├── autocomplete.py      # (Tim D)
│   ├── permissions.py       # (Tim B)
│   ├── notification_helper.py # (Tim B)
│   ├── backup_restore.py    # (Tim B)
│   └── export_manager.py    # (Tim B)
│
├── assets/                  # 🖼️ Aset Visual
│   ├── icon.png
│   └── splash.png
│
├── data/                    # 📊 Data Files
│   ├── code_templates.json
│   └── sample_data.json
│
├── docs/                    # 📚 Dokumentasi
│   ├── PROJECT_BIBLE.md
│   ├── proposal.md
│   ├── changelog.md
│   ├── user_guide.md
│   ├── developer_guide.md
│   ├── test_case_checklist.md
│   ├── bug_tracker.md
│   └── wireframe_editor.md
│
├── notebooks/               # 📓 Build Notebook
│   └── build_axnn_colab.ipynb
│
├── .github/                 # 🤖 CI/CD
│   └── workflows/
│       └── ci.yml
│
└── bin/                     # 📦 APK Output

```

**Pembagian Tim:**
- **Tim A** — Manajemen Proyek: `docs/PROJECT_BIBLE.md`, `docs/proposal.md`, `.gitignore`
- **Tim B** — Backend & Logic: `models/*`, `controllers/*`, `utils/database.py`, `utils/file_picker.py`
- **Tim C** — UI/UX: `screens/*` (kecuali editor), `kv_files/*` (kecuali editor), `components/*` (kecuali code_editor), `utils/theme.py`, `assets/*`
- **Tim D** — Editor Kode: `screens/editor_screen.py`, `kv_files/editor_screen.kv`, `kv_files/code_editor.kv`, `components/code_editor.py`, `utils/syntax_highlighter.py`, `utils/autocomplete.py`, `models/file_model.py`, `controllers/editor_controller.py`
- **Tim E** — Build, QA, Rilis: `buildozer.spec`, `requirements.txt`, `README.md`, `docs/*` (kecuali PROJECT_BIBLE.md), `.github/*`, `notebooks/*`

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Versi |
|-------------|-------|
| Python | 3.11.x |
| pip | latest |
| Buildozer (untuk build Android) | 1.5.0 |

### 1. Clone Repository

```bash
git clone https://github.com/axionneuralis-a11y/AXNN.git
cd AXNN
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Jalankan Aplikasi (Desktop Testing)

```bash
python main.py
```

4. Build APK (Android)

Menggunakan Google Colab

Buka notebooks/build_axnn_colab.ipynb di Google Colab dan jalankan semua cell.

Menggunakan Buildozer Lokal

```bash
buildozer init
buildozer -v android debug
```

APK akan berada di folder bin/

---

📦 Dependencies

Library Versi Fungsi
Kivy 2.3.0 Framework UI utama
KivyMD 1.2.0 Komponen Material Design
Buildozer 1.5.0 Build APK
Cython 0.29.37 Dependency Buildozer
Plyer 2.1.0 Notifikasi, vibrate, email
androidstorage4kivy 2024.03.07 Akses storage Android
Pygments 2.18.0 Syntax highlighting
Jedi 0.19.1 Autocomplete Python
SQLite3 Built-in Database lokal

---

🎨 Design System

Tema Resmi

Elemen ☀️ Terang 🌙 Gelap 🟢 MATRIX
Background #FAFAFA #121212 #000000
Teks Utama #1A1A1A #F5F5F5 #00FF41
Aksen #2196F3 #64B5F6 #39FF14 (glow)

Aturan Tema Matrix (Ketat)

· Background: #000000 (hitam pekat)
· Teks biasa: #00FF41 (hijau neon)
· Keyword: #39FF14 + efek glow
· String: #7FFF00 (hijau muda)
· Angka: #ADFF2F (hijau kekuningan)
· Komentar: #006400 (hijau redup)

DILARANG menggunakan warna biru, merah, putih, atau kuning di tema Matrix.

---

📱 Fitur Lengkap v1.1.0

Fitur Warisan v1.0.0 (100% Dipertahankan)

ID Fitur Status
F001 CRUD Catatan + 3 Terbaru di Home ✅
F002 CRUD Todo + Tandai Selesai ✅
F003 Manajemen Folder + Filter ✅
F004 Kalkulator Dasar + Riwayat ✅
F005 Kalender Bulanan + Indikator Tanggal ✅
F006 Notifikasi Push + Reminder ✅
F007 Backup/Restore JSON ✅
F008 Export 1 Note→MD, 1 Todo→TXT ✅
F009 Share + Copy Clipboard ✅
F010 Tema Gelap/Terang + Simpan ✅
F011 Bottom Nav 6 Menu + Animasi ✅
F012 Fullscreen Mode Edit ✅
F013 Statistik Aplikasi ✅
F014 Kirim Feedback Email ✅
F015 Badge Notifikasi ✅
F016 Banner AXION Neuralis ✅

Catatan: Hanya 1 fitur yang dihapus dari v1.0.0: Menu Input VAPID Public Key.

Fitur Baru v1.1.0

ID Fitur Prioritas Status
N001 Migrasi Stack → Kivy/Buildozer P0 ⚪
N002 Rename Aplikasi → AXNN P0 ⚪
N003 Export Multi Format (20+ format) P0 ⚪
N004 File Picker Storage Android P0 ⚪
N005 Tema Green Matrix P0 ⚪
N006 Perbaikan Tata Letak P0 ⚪
N007 Tombol >_ Editor Kode P0 ⚪
N008 Widget Editor Kode Dasar P0 ⚪
N009 Syntax Highlighting Multibahasa P0 ⚪
N010 Autocomplete Berdasarkan Ekstensi P0 ⚪
N011 Popup Buat File + Validasi Ekstensi P0 ⚪
N012 Save File ke Storage User P0 ⚪
N013 Auto Save Sementara P0 ⚪
N014 Line Number P1 ⚪
N015 Undo/Redo Editor P1 ⚪
N016 Cari & Ganti Teks P1 ⚪
N017 Zoom Font Editor P2 ⚪

Daftar Ekstensi Bahasa Editor

Ekstensi Bahasa Prioritas
.py Python P0
.html .htm HTML P0
.css CSS P0
.js JavaScript P0
.json JSON P0
.md Markdown P0
.java Java P1
.kt Kotlin P1
.cpp .c .h C/C++ P1
.php PHP P1
.go Go P1
.rs Rust P1
.yaml .yml YAML P2

---

🔧 Development Guidelines

Code Standard

· Ikuti PEP 8 secara ketat
· Gunakan Black formatter (line length 88)
· Wajib Type Hints untuk semua fungsi
· Wajib Docstring untuk semua public function
· Maksimal 300 baris per file
· Maksimal 30 baris per fungsi

Git Flow

```bash
# Kerja di branch fitur
git checkout -b feature/tim-x-nama-fitur

# Commit sering dengan pesan jelas
git commit -m "feat(module): deskripsi jelas"

# Push dan buat Pull Request ke develop
git push origin feature/tim-x-nama-fitur
```

Commit Message Format

```
<type>(<scope>): <subject>

<type>:
  feat     - Fitur baru
  fix      - Perbaikan bug
  docs     - Dokumentasi
  style    - Formatting, whitespace
  refactor - Perbaikan kode tanpa mengubah fungsi
  test     - Menambah/memperbaiki test
  chore    - Maintenance

<scope>:
  model, controller, screen, editor, theme, build, docs

<subject>:
  Deskripsi singkat, maksimal 50 karakter
```

Pull Request Requirements

1. Lint lulus (Ruff/Flake8)
2. Type check lulus (mypy)
3. Unit test lulus
4. Minimal 1 reviewer + Ketua Tim approve

---

🧪 Testing

Test Coverage Target

· Unit Test: > 80% coverage
· Integration Test: Semua alur utama
· UI Test: Semua layar & komponen
· Performance Test: Startup < 2 detik, editor 1000 baris tidak lag

Run Tests

```bash
# Unit test
pytest tests/

# With coverage
pytest --cov=. --cov-report=html
```

---

📚 Dokumentasi

Dokumen Deskripsi
PROJECT_BIBLE.md Aturan & visi proyek (WAJIB BACA)
Blueprint Panduan teknis implementasi
Roadmap Rencana pengerjaan 8 minggu
User Guide Panduan penggunaan aplikasi
Developer Guide Panduan pengembangan
Changelog Riwayat perubahan versi
Test Cases Checklist pengujian

---

🏢 Tim Pengembang

Tim Kode Tugas Utama Ketua
Tim A 🟢 Manajemen Proyek & Keputusan Azriel
Tim B 🔵 Backend, Logika & Data [Nama]
Tim C 🟣 Frontend, UI/UX & Tema [Nama]
Tim D 🟠 Editor Kode (Fitur Unggulan) [Nama]
Tim E 🟡 Build, QA, Rilis & Docs [Nama]

Lihat PROJECT_BIBLE.md Bab 6 untuk detail tugas masing-masing tim.

---

📝 Changelog

🟡 v1.1.0 — Native Editor Upgrade (Dalam Pengembangan)

Target Rilis: 30 September 2026

✨ Added:

· Editor Kode Multibahasa dengan tombol >_
· Syntax Highlighting 10+ bahasa
· Autocomplete cerdas (Python + Jedi)
· Popup buat file + validasi ekstensi
· Save ke Storage User + Auto Save
· Tema Green Matrix
· Export Multi Format (20+ format teks)
· File Picker Storage Android

🔄 Changed:

· Migrasi penuh AppMint → Kivy/Buildozer
· Nama aplikasi: NoteMint → AXNN
· Perbaikan tata letak seluruh layar

❌ Removed:

· Menu Input VAPID Public Key (hanya fitur yang dihapus)

✅ v1.0.0 — Versi Stabil Awal

Tanggal Rilis: Sebelum Agustus 2026

Added:

· Rilis pertama NoteMint
· 16 fitur produktivitas lengkap

---

🤝 Kontribusi

Kami menyambut kontribusi! Pastikan untuk membaca:

1. PROJECT_BIBLE.md — Aturan utama proyek
2. Developer Guide — Panduan pengembangan
3. Coding Standard — Standar kode

Proses Kontribusi

1. Fork repository
2. Buat branch fitur (git checkout -b feature/amazing-feature)
3. Commit perubahan (git commit -m 'feat: add amazing feature')
4. Push ke branch (git push origin feature/amazing-feature)
5. Buka Pull Request ke branch develop

---

📄 Lisensi

Distributed under the MIT License.

---

📞 Kontak

· CEO / Project Owner: Azriel
· Repository: https://github.com/axionneuralis-a11y/AXNN
· Email: axionneuralis@gmail.com

---

🙏 Acknowledgments

· Kivy — Framework GUI
· KivyMD — Material Design Components
· Buildozer — Build tool for Android
· Pygments — Syntax highlighting
· Jedi — Autocomplete for Python

---

🌿 Made with ❤️ by AXNN Team

Dokumen ini sesuai dengan PROJECT BIBLE v1.1 dan Roadmap Resmi.

```
