📘 AXN NOTE --- PROJECT BIBLE v3.1 FINAL
Dokumen ini adalah sumber kebenaran tunggal (Single Source of Truth) untuk seluruh tim.
Setiap anggota tim WAJIB membaca, memahami, dan mematuhi seluruh isi dokumen ini.
Pelanggaran terhadap aturan dalam dokumen ini dapat menyebabkan kontribusi ditolak.

📋 DAFTAR ISI
Informasi Proyek
Changelog
Hirarki & Resolusi Konflik
Status Proyek
Definition of Done (DoD)
Deskripsi Aplikasi
Daftar Tim & Tugas
Aturan Wajib --- Umum
Aturan Wajib --- Fitur
Aturan Wajib --- Tampilan & Design Tokens
Aturan Wajib --- Tipografi
Aturan Wajib --- Kode & Teknis
Aturan Wajib --- Keamanan
Aturan Wajib --- Build & Deploy
Data Contract --- LocalStorage Schema
Aturan Backup / Restore / Export
Aturan Auto-Save
Error Handling Policy
Non-Functional Requirements
Out of Scope
Struktur Folder
Daftar File
Spesifikasi Teknis
Roadmap
Blueprint Arsitektur
Testing & Acceptance Criteria
Aturan Komunikasi Tim
Lampiran

INFORMASI PROYEK
| Item | Detail |
|---|---|
| Nama Proyek | AXN Note |
| Application Version | 2.5.0 (target) |
| Bible Version | 3.1 FINAL |
| Jenis Aplikasi | Aplikasi Manajemen File & Catatan (File/Folder Manager + Note-Taking) |
| Platform Target | Android (via WebView / AppMint) |
| Teknologi Inti | HTML + CSS + JavaScript (Single-File, Vanilla) |
| Penyimpanan | LocalStorage (offline-first) |
| Lisensi | MIT |
| Repository | https://github.com/axionneuralis-a11y/AXNN |
| Pemilik Proyek | User (Project Owner) |

«Catatan: Repository dan lisensi di atas mengikuti informasi yang terdapat pada Bible v2.0. Keduanya tidak diubah dalam revisi ini.»

1.1 Pemisahan Versi
Application Version dan Bible Version adalah dua versi yang terpisah.
Perubahan pada Bible tidak otomatis mengubah versi aplikasi.
Perubahan pada aplikasi tidak otomatis mengubah versi Bible.
Perubahan yang memengaruhi spesifikasi proyek harus dicatat pada Bible Changelog.
Perubahan implementasi aplikasi harus dicatat pada Application Changelog.

CHANGELOG

2.1 Bible Changelog
| Tanggal | Bible Ver | Scope | Tipe | Deskripsi |
|---|---|---|---|---|
| 2026-08-08 | 1.0 | DOC | INIT | Inisialisasi Project Bible v1.0 |
| 2026-08-09 | 2.0 | DOC | CHANGE | Revisi besar: status, DoD, Data Contract, Backup/Restore, Design Tokens, NFR, Out of Scope, Testing, Error Handling, dan resolusi konflik |
| 2026-08-09 | 2.1 | DOC | FIX | Perbaikan bagian dokumen yang terpotong, pelengkapan LocalStorage Schema, NFR, Build Specification, Acceptance Criteria, Test Matrix, aturan schema migration, serta konsistensi status dan terminology |
| 2026-08-09 | 3.0 | DOC | CHANGE | Finalisasi resmi berdasarkan Project Bible v2.1, Blueprint Final, dan Roadmap Final; Project Owner approval; Blueprint dan Roadmap ditetapkan sebagai dokumen pendukung resmi |
| 2026-08-09 | 3.1 | BUILD | CHANGE | Menetapkan keputusan Project Owner untuk nilai TBD pada Build Specification: Package/Application ID production adalah `com.axionneuralis.axnnote`. |
| 2026-08-09 | 3.1 | BUILD | CHANGE | Menetapkan Version Name production `2.5.0` dan Version Code production `2`. |
| 2026-08-09 | 3.1 | BUILD | CHANGE | Menetapkan Min Android `Android 7` / API 24. |
| 2026-08-09 | 3.1 | BUILD | CHANGE | Menetapkan Target Android pada rentang `Android 11–15`. Untuk build AppMint, target eksekusi dipilih sebagai target tertinggi yang tersedia dalam rentang tersebut, yaitu Android 15 / API 35, selama didukung oleh AppMint. |
| 2026-08-09 | 3.1 | BUILD | CHANGE | Menetapkan orientation tetap Portrait. |
| 2026-08-09 | 3.1 | BUILD | CHANGE | Menetapkan Build Type Production sebagai Release. Release key telah tersedia dan hanya digunakan pada proses signing AppMint. Release key, alias, password, atau secret tidak boleh disimpan di repository, ZIP, atau dokumentasi. |
| 2026-08-09 | 3.1 | BUILD | ADD | Menambahkan identitas build beta/testing sebagai jalur build terpisah: Package/Application ID beta/testing adalah `com.axnnotebeta.app`. Jalur beta/testing tidak mengubah identitas production. |
| 2026-08-09 | 3.1 | BUILD | ADD | Menambahkan keputusan Project Owner untuk custom user agent. Suffix UA production: `AXNNote/2.5.0 (Android; com.axionneuralis.axnnote)`. Suffix UA beta/testing: `AXNNote-Beta/2.5.0 (Android; com.axnnotebeta.app)`. |
| 2026-08-09 | 3.1 | BUILD | ADD | Menambahkan full user agent production resmi: `Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 AXNNote/2.5.0 (com.axionneuralis.axnnote)`. |
| 2026-08-09 | 3.1 | DOC | CHANGE | Menyinkronkan Blueprint dan Roadmap dengan keputusan build terbaru. Tidak ada perubahan pada Data Contract, Design Tokens, security policy, atau scope fitur. |
| 2026-08-09 | 3.1 | ASSET | CHANGE | Mencatat bahwa 23 file SVG placeholder build-ready telah disiapkan untuk memenuhi inventaris file dan menghilangkan missing asset reference pada manifest. Aset SVG final tetap menunggu GP-04 / Project Owner. |
| 2026-08-09 | 3.1 | DOC | CHANGE | Mencatat bahwa source package telah disiapkan sebagai paket build-ready untuk AppMint, tetapi status release final tetap menunggu AppMint build, APK validation, regression, dan Project Owner sign-off. |

2.2 Application Changelog
| Tanggal | App Ver | Scope | Tipe | Deskripsi |
|---|---|---|---|---|
| 2026-08-09 | 2.5.0 | APP | INIT | Finalisasi source build-ready `index.html` untuk AXN Note v2.5.0 sesuai Bible dan Blueprint: single-file core, vanilla JavaScript, offline-first, LocalStorage, safe DOM rendering, tanpa `console.log()`, tanpa `eval()`, tanpa external runtime dependency. |
| 2026-08-09 | 2.5.0 | APP | ADD | Implementasi core feature release-critical: create folder, create file, edit file, rename, move, delete, search, breadcrumb, dark/light mode, backup, restore, local notification, statistics, context menu, dan feedback. |
| 2026-08-09 | 2.5.0 | APP | ADD | Implementasi validation layer untuk root schema, folder object, file object, ID uniqueness, parent reference, circular folder reference, timestamp, dan settings. |
| 2026-08-09 | 2.5.0 | APP | ADD | Implementasi backup JSON lengkap dengan preservasi `schemaVersion`, folders, files, IDs, timestamps, dan settings. |
| 2026-08-09 | 2.5.0 | APP | ADD | Implementasi restore dengan validasi penuh, konfirmasi pengguna, dan proteksi data aktif dari input invalid. |
| 2026-08-09 | 2.5.0 | APP | ADD | Implementasi Service Worker local-only untuk cache aset lokal, tanpa `/api/sync`, tanpa `/api/notes/latest`, tanpa `sync`/`periodicsync`, dan tanpa upload data pengguna. |
| 2026-08-09 | 2.5.0 | BUILD | CHANGE | Konfigurasi `manifest.json` untuk AppMint production: package `com.axionneuralis.axnnote`, version `2.5.0`, version code `2`, min SDK/API 24, target SDK/API 35, orientation portrait, custom user agent production. |
| 2026-08-09 | 2.5.0 | ASSET | ADD | Menambahkan 23 file SVG placeholder build-ready pada `assets/icons/icon-1.svg` sampai `assets/icons/icon-23.svg` untuk memenuhi file inventory dan mencegah missing asset reference. |
| 2026-08-09 | 2.5.0 | DOC | ADD | Finalisasi README.md untuk kebutuhan build dan release. |
| 2026-08-09 | 2.5.0 | DOC | ADD | Finalisasi `.gitignore` untuk mencegah release key, keystore, build output, dan file sensitif masuk ke repository. |
| 2026-08-09 | 2.5.0 | DOC | ADD | Finalisasi LICENSE MIT sesuai keputusan lisensi proyek. |

2.3 Legenda Scope
| Kode | Arti |
|---|---|
| APP | Perubahan pada kode aplikasi |
| DOC | Perubahan dokumentasi |
| BUILD | Perubahan konfigurasi build/packaging |
| ASSET | Perubahan aset |

2.4 Legenda Tipe Perubahan
🟢 ADD --- Penambahan fitur/entri baru
🔵 CHANGE --- Perubahan yang sudah ada
🟡 FIX --- Perbaikan bug atau kesalahan
🔴 REMOVE --- Penghapusan
⚪ INIT --- Inisialisasi/pembuatan awal

2.5 Aturan Changelog
Setiap perubahan pada kode, file, aset, build configuration, atau dokumen WAJIB dicatat pada changelog yang sesuai.
Perubahan Bible dicatat pada Bible Changelog.
Perubahan aplikasi dicatat pada Application Changelog.
Perubahan build dicatat dengan Scope "BUILD".
Perubahan aset dicatat dengan Scope "ASSET".
GP-01 bertanggung jawab memperbarui changelog.
Format tanggal wajib "YYYY-MM-DD".
Setiap entri harus singkat, jelas, dan dapat ditelusuri.

HIRARKI & RESOLUSI KONFLIK
3.1 Hirarki Otoritas
Jika terdapat perbedaan informasi antar sumber, urutan otoritas adalah:
1. Keputusan eksplisit Project Owner
2. Project Bible
3. Blueprint
4. Roadmap
5. Source Code
6. Catatan/komunikasi informal

3.2 Keputusan Project Owner
Keputusan Project Owner dapat disampaikan secara lisan maupun tertulis, tetapi:
- Keputusan yang mengubah spesifikasi proyek WAJIB dicatat kembali dalam Bible.
- Keputusan yang mengubah implementasi WAJIB dicatat pada changelog.
- Keputusan sementara harus ditandai sebagai "TEMPORARY" atau "TBD".
- Keputusan yang belum didokumentasikan tidak boleh digunakan sebagai dasar untuk mengubah bagian lain secara permanen.

3.3 Aturan Konflik
Jika terjadi konflik antara dokumen atau antara dokumen dan kode:
1. Identifikasi konflik.
2. Laporkan kepada GP-01.
3. GP-01 menganalisis konflik.
4. GP-01 mengajukan resolusi kepada Project Owner.
5. Project Owner membuat keputusan final.
6. Bible/Blueprint diperbarui sesuai keputusan.
7. Source Code disesuaikan.
8. Changelog diperbarui.
9. Testing dilakukan ulang jika konflik memengaruhi perilaku aplikasi.
Implementasi yang bertentangan dengan spesifikasi terbaru dianggap TIDAK VALID sampai konflik diselesaikan.

STATUS PROYEK
4.1 Legenda Status
| Ikon | Status | Definisi |
|---|---|---|
| ⬜ | BELUM DIMULAI | Belum ada implementasi |
| 🔵 | IMPLEMENTASI | Sedang dikerjakan |
| 🟡 | VALIDASI | Implementasi tersedia tetapi belum lulus seluruh validasi |
| 🟢 | SELESAI | Memenuhi seluruh DoD dan Acceptance Criteria |
| 🔴 | TERBLOKIR / DIBATALKAN | Tidak dapat dilanjutkan atau secara resmi dibatalkan |

«Penting: "File sudah ada" tidak sama dengan "SELESAI".»
Status 🟢 hanya boleh digunakan apabila seluruh kriteria DoD terpenuhi.

4.2 Lifecycle
⬜ BELUM DIMULAI ↓ 🔵 IMPLEMENTASI ↓ 🟡 VALIDASI ↓ 🟢 SELESAI
Dari tahap mana pun: ↓ 🔴 TERBLOKIR / DIBATALKAN

4.3 Status Komponen
| Komponen | Implementasi | Validasi | Status | Keterangan |
|---|---|---|---|---|
| Frontend Core | Ada | Belum | 🟡 VALIDASI | "index.html" tersedia, perlu validasi |
| Service Worker Core | Ada | Belum | 🟡 VALIDASI | "sw.js" tersedia, perlu validasi |
| Manifest Core | Ada | Belum | 🟡 VALIDASI | "manifest.json" tersedia, perlu validasi |
| Ikon & Aset SVG | Ada (Placeholder) | Belum | 🟡 VALIDASI | 23 file SVG placeholder build-ready telah disiapkan |
| Testing Fungsional | Belum | Belum | ⬜ BELUM DIMULAI | Menunggu implementasi final |
| Testing UI/UX | Belum | Belum | ⬜ BELUM DIMULAI | Menunggu implementasi final |
| Testing Offline | Belum | Belum | ⬜ BELUM DIMULAI | Menunggu validasi Service Worker |
| Bug Fixing | Belum | Belum | ⬜ BELUM DIMULAI | Menunggu hasil testing |
| Build AppMint | Belum | Belum | ⬜ BELUM DIMULAI | Menunggu seluruh komponen siap |
| README.md | Ada | Belum | 🟡 VALIDASI | Disiapkan untuk build |
| .gitignore | Ada | Belum | 🟡 VALIDASI | Disiapkan untuk build |
| LICENSE | Ada | Belum | 🟡 VALIDASI | Mengikuti keputusan lisensi proyek |

4.4 Temuan Kondisi Kode Saat Ini
Berdasarkan review yang telah dicatat pada Bible v2.0 dan pembaruan v3.1:
- "index.html" saat ini merupakan File/Folder Manager dengan editor plain text.
- Rich Text Editing belum tersedia.
- "sw.js" referensi endpoint API yang tidak sesuai dengan konsep offline-only telah dibersihkan.
- "manifest.json" merujuk aset placeholder yang telah disiapkan.
- "console.log()" telah dibersihkan.
- "SUBSCRIPTION_KEY" yang tidak digunakan telah dibersihkan.
- Versi footer aplikasi telah disesuaikan.
Temuan tersebut adalah Current Known Issues yang telah diselesaikan pada fase persiapan build, bukan spesifikasi fitur baru.

DEFINITION OF DONE (DoD)
Sebuah fitur atau komponen hanya dapat diberi status 🟢 SELESAI apabila seluruh kriteria berikut terpenuhi.
| No. | Kriteria | Ketentuan |
|---|---|---|
| 1 | Implementasi | Kode telah diimplementasikan sesuai Bible/Blueprint |
| 2 | Functional correctness | Perilaku sesuai Acceptance Criteria |
| 3 | Tidak ada error kritis | Tidak ada crash, uncaught exception kritis, atau data loss pada penggunaan normal |
| 4 | Offline | Fitur dapat digunakan tanpa internet jika memang termasuk fitur offline |
| 5 | Persistence | Data yang memang harus disimpan tetap tersedia setelah reload |
| 6 | Regression | Tidak merusak fitur yang sebelumnya sudah selesai |
| 7 | Manual test | Implementer telah melakukan pengujian dasar |
| 8 | QA | GP-05 memberikan status PASS |
| 9 | Dokumentasi | Dokumentasi terkait sudah diperbarui |
| 10 | Changelog | Perubahan sudah dicatat |

Jika salah satu kriteria belum terpenuhi, status maksimum adalah 🟡 VALIDASI.

5.1 Perbedaan DoD dan Acceptance Criteria
Definition of Done (DoD) menentukan kapan pekerjaan dianggap selesai secara engineering.
Acceptance Criteria menentukan perilaku yang harus dipenuhi oleh fitur.
QA bertugas memverifikasi bahwa Acceptance Criteria dan DoD telah terpenuhi.

DESKRIPSI APLIKASI
6.1 Definisi Produk
AXN Note adalah aplikasi hybrid File/Folder Manager + Note-Taking.
Struktur utama aplikasi menggunakan folder dan file, sedangkan file dapat digunakan sebagai catatan.
Aplikasi dirancang sebagai aplikasi lokal/offline-first tanpa akun dan tanpa backend eksternal.

6.2 Deskripsi Beta
AXN Note adalah aplikasi manajemen file dan catatan ringan berbasis web yang berjalan secara offline-first. Aplikasi memungkinkan pengguna membuat, mengelola, mengorganisir, mencari, mengedit, memindahkan, dan menghapus folder serta file catatan. Aplikasi juga menyediakan mode gelap/terang, backup/restore, notifikasi lokal, dan statistik penggunaan.

6.3 Deskripsi Production
AXN Note adalah aplikasi manajemen file dan catatan ringan, cepat, dan sepenuhnya offline untuk Android. Dibangun dengan HTML, CSS, dan JavaScript serta dibungkus menggunakan AppMint, AXN Note menyediakan pengelolaan folder dan file catatan dengan pencarian, navigasi hirarki, backup/restore, mode gelap/terang, serta fitur pencatatan yang dapat dikembangkan tanpa memerlukan akun atau koneksi internet.

DAFTAR TIM & TUGAS
| Kode | Nama | Peran | Tanggung Jawab |
|---|---|---|---|
| GP-01 | QWEN | Project Lead / Architect | Bible, Blueprint, Roadmap, README, struktur proyek, governance |
| GP-02 | TBD | Data Engineer | LocalStorage schema, backup/restore, migration |
| GP-03 | TBD | Frontend Developer | HTML/CSS/JS, UI, interaction |
| GP-04 | TBD | Asset / Design | SVG, visual asset, konsistensi desain |
| GP-05 | TBD | QA / Tester | Functional test, UI/UX test, bug report |
| GP-06 | TBD | Build & Deploy | AppMint, ZIP, APK, release configuration |

"TBD" berarti belum ditentukan dan bukan berarti posisi tersebut wajib diisi segera.
Project Owner dapat menambah, menghapus, atau mengubah anggota tim.

ATURAN WAJIB --- UMUM
Semua aturan dalam Bible ini wajib dipatuhi.
- Bible adalah acuan utama proyek.
- Resolusi konflik mengikuti Bab 3.
- Jika informasi tidak jelas, jangan membuat asumsi.
- Perubahan wajib mendapatkan persetujuan Project Owner.
- Perubahan wajib dicatat pada changelog yang sesuai.
- Fitur yang sudah disetujui tidak boleh dihapus tanpa persetujuan Project Owner.
- Backward compatibility LocalStorage wajib dijaga.
- Dokumentasi proyek menggunakan Bahasa Indonesia.
- Kode, komentar kode, identifier, nama variabel, fungsi, class, dan konstanta menggunakan Bahasa Inggris.
- Implementasi tidak boleh menyimpang dari Bible/Blueprint tanpa proses perubahan resmi.
- File yang tidak tercantum pada Daftar File tidak boleh ditambahkan secara permanen tanpa pembaruan Bible.
- Semua keputusan permanen harus dapat ditelusuri melalui dokumentasi.

ATURAN WAJIB --- FITUR
9.1 Fitur yang Sudah Ada pada Kode
| No. | Fitur | Keterangan | Status |
|---|---|---|---|
| 1 | Buat Folder | Membuat folder baru | 🟡 VALIDASI |
| 2 | Buat File | Membuat file catatan plain text | 🟡 VALIDASI |
| 3 | Edit File | Mengubah nama dan konten | 🟡 VALIDASI |
| 4 | Hapus Folder/File | Menghapus dengan konfirmasi | 🟡 VALIDASI |
| 5 | Rename | Mengubah nama item | 🟡 VALIDASI |
| 6 | Pindahkan Item | Memindahkan item ke folder lain | 🟡 VALIDASI |
| 7 | Search | Pencarian nama dan konten | 🟡 VALIDASI |
| 8 | Breadcrumb | Navigasi hirarki folder | 🟡 VALIDASI |
| 9 | Dark/Light Mode | Pergantian tema | 🟡 VALIDASI |
| 10 | Backup | Export seluruh data JSON | 🟡 VALIDASI |
| 11 | Restore | Import backup JSON | 🟡 VALIDASI |
| 12 | Local Notification | Notifikasi lokal | 🟡 VALIDASI |
| 13 | Statistics | Statistik folder, file, storage | 🟡 VALIDASI |
| 14 | Context Menu | Menu aksi item | 🟡 VALIDASI |
| 15 | Feedback | Feedback melalui "mailto:" | 🟡 VALIDASI |

9.2 Fitur yang Direncanakan
| No. | Fitur | Status |
|---|---|---|
| 16 | Rich Text Editing | ⬜ BELUM DIMULAI |
| 17 | Kategori/Tag | ⬜ BELUM DIMULAI |
| 18 | Pin Catatan | ⬜ BELUM DIMULAI |
| 19 | Checklist | ⬜ BELUM DIMULAI |
| 20 | Link | ⬜ BELUM DIMULAI |
| 21 | Highlight Warna | ⬜ BELUM DIMULAI |
| 22 | Ukuran Font Editor | ⬜ BELUM DIMULAI |
| 23 | Penghitung Karakter & Kata | ⬜ BELUM DIMULAI |
| 24 | Auto-Save | ⬜ BELUM DIMULAI |
| 25 | Undo/Redo | ⬜ BELUM DIMULAI |
| 26 | Sortir Catatan | ⬜ BELUM DIMULAI |
| 27 | Grid/List View | ⬜ BELUM DIMULAI |
| 28 | Export Catatan Individual | ⬜ BELUM DIMULAI |

9.3 Lifecycle Fitur
Setiap fitur harus memiliki status:
PLANNED → IMPLEMENTATION → VALIDATION → DONE
atau
→ BLOCKED → CANCELLED
Fitur tidak boleh dihapus diam-diam dari roadmap.
Jika dibatalkan, status harus diubah menjadi 🔴 DIBATALKAN dan alasan dicatat pada changelog.

9.4 Aturan Fitur
- Dilarang menambahkan fitur tanpa persetujuan Project Owner.
- Dilarang mengubah perilaku fitur tanpa persetujuan.
- Fitur baru harus didokumentasikan sebelum implementasi.
- Fitur yang memengaruhi Data Contract harus memperbarui Bab 15 sebelum implementasi.
- Fitur yang memengaruhi UI harus memperbarui Design Tokens/UI specification jika diperlukan.
- Fitur yang memengaruhi keamanan harus memperbarui Bab 13.

ATURAN WAJIB --- TAMPILAN & DESIGN TOKENS
10.1 Prinsip Desain
| Prinsip | Ketentuan |
|---|---|
| Minimalis | UI bersih dan tidak berlebihan |
| Fungsional | Setiap elemen memiliki tujuan |
| Konsisten | Visual dan interaksi konsisten |
| Responsif | Mendukung ukuran layar target |
| Aksesibel | Mengikuti kriteria aksesibilitas |
| Offline-friendly | Tidak bergantung pada resource eksternal |

10.2 Design Tokens --- Light Mode
Bible menentukan nilai; "index.html" mengimplementasikan.
| Token | Nilai |
|---|---|
| "--bg-primary " | "#f0f2f5 " |
| "--bg-secondary " | "#ffffff " |
| "--bg-card " | "#ffffff " |
| "--bg-nav " | "#1a1a2e " |
| "--text-primary " | "#1a1a2e " |
| "--text-secondary " | "#4a4a6a " |
| "--text-nav " | "#ffffff " |
| "--border-color " | "#e0e0e0 " |
| "--shadow " | "0 2px 12px rgba(0,0,0,0.08) " |
| "--radius " | "16px " |
| "--radius-sm " | "10px " |
| "--accent " | "#6c5ce7 " |
| "--accent-hover " | "#5a4bd1 " |
| "--danger " | "#e74c6f " |
| "--success " | "#00b894 " |
| "--warning " | "#fdcb6e " |
| "--transition " | "0.3s cubic-bezier(0.4,0,0.2,1) " |
| "--font " | "'Segoe UI', system-ui, -apple-system, sans-serif " |
| "--folder-color " | "#fdcb6e " |
| "--file-color " | "#74b9ff " |

10.3 Design Tokens --- Dark Mode
| Token | Nilai |
|---|---|
| "--bg-primary " | "#0f0f1a " |
| "--bg-secondary " | "#1a1a2e " |
| "--bg-card " | "#252541 " |
| "--text-primary " | "#eeeef8 " |
| "--text-secondary " | "#a0a0c0 " |
| "--border-color " | "#3a3a5a " |
| "--shadow " | "0 2px 12px rgba(0,0,0,0.4) " |
| "--bg-nav " | "#0a0a16 " |
| "--text-nav " | "#eeeef8 " |

10.4 Aturan Tampilan
- Design Tokens tidak boleh diubah tanpa persetujuan Project Owner.
- Layout utama tidak boleh diubah tanpa persetujuan.
- Ikon menggunakan SVG.
- Ukuran ikon harus konsisten.
- Transisi default berada pada rentang 200--400ms.
- Tidak boleh terjadi clipping atau overflow pada ukuran layar target.
- Lebar utama aplikasi: Mobile: maksimum 480px. Tablet/Desktop: maksimum 600px.
- UI harus tetap usable pada lebar 360px.
- Tidak boleh bergantung pada font atau aset eksternal untuk fungsi inti.

10.5 Aksesibilitas
| Kriteria | Standar |
|---|---|
| Kontras teks normal | Minimal WCAG 2.1 AA, 4.5:1 |
| Kontras teks besar | Minimal WCAG 2.1 AA, 3:1 |
| Touch target | Minimal 44×44px |
| Focus state | Harus terlihat pada elemen interaktif yang relevan |
| Label ikon | "aria-label", "title", atau teks alternatif |
| Warna | Tidak boleh menjadi satu-satunya indikator status |
| Error | Harus dapat dipahami tanpa bergantung pada warna |
| Form/input | Harus memiliki label atau konteks yang jelas |

ATURAN WAJIB --- TIPOGRAFI
| Item | Spesifikasi |
|---|---|
| Font Utama | "'Segoe UI', system-ui, -apple-system, sans-serif" |
| Body | 14px default |
| Judul h1 | 20px |
| Judul h3 | 15px |
| Meta/Subtitle | 11--13px |
| Line Height | 1.5--1.6 |
| Body Weight | 400 |
| Label Weight | 600 |
| Heading Weight | 700 |

11.1 Aturan Tipografi
- Dilarang menggunakan font eksternal.
- Font harus tersedia melalui system font stack.
- Teks harus terbaca pada Light dan Dark Mode.
- Ukuran font editor harus dapat diubah pengguna ketika fitur #22 diimplementasikan.
- Ukuran teks tidak boleh digunakan sebagai satu-satunya pembeda status.

ATURAN WAJIB --- KODE & TEKNIS
12.1 Struktur Kode
| Aturan | Ketentuan |
|---|---|
| Single File | HTML, CSS, JS berada di "index.html" |
| Vanilla JS | Tidak menggunakan framework/library eksternal |
| No CDN | Tidak menggunakan CDN |
| No External Runtime Dependency | Fungsi inti tidak bergantung pada URL eksternal |
| No Build Tool | Tidak membutuhkan webpack/babel/build tool |
| ES6+ | Menggunakan JavaScript modern |
| CSS Inline | CSS berada dalam "index.html" |
| JS Inline | JavaScript berada dalam "index.html" |

12.2 Penamaan
| Elemen | Konvensi | Contoh |
|---|---|---|
| Variabel JS | camelCase | "noteTitle " |
| Fungsi JS | camelCase | "saveNote() " |
| Konstanta | UPPER_SNAKE_CASE | "STORAGE_KEY " |
| CSS Class | kebab-case | ".note-card " |
| HTML ID | kebab-case | "#note-editor " |
| File | lowercase/kebab-case | "index.html " |
| CSS Custom Property | "--kebab-case " | "--bg-primary " |

12.3 Aturan Kode
- Dilarang menggunakan "eval()".
- Dilarang menggunakan "Function()" untuk mengeksekusi input pengguna.
- Dilarang menggunakan "document.write()" dengan input pengguna.
- Dilarang menggunakan "innerHTML" dengan data pengguna yang belum disanitasi.
- Semua data pengguna yang dirender ke DOM harus di-escape atau disanitasi.
- Tidak boleh ada "console.log()" pada production build.
- "console.warn()" hanya digunakan untuk diagnostic/error yang relevan.
- Komentar kode menggunakan Bahasa Inggris.
- Komentar harus singkat dan menjelaskan alasan/perilaku penting.
- Jangan menggunakan "try/catch" hanya sebagai formalitas; gunakan error handling sesuai risiko operasi.

ATURAN WAJIB --- KEAMANAN
13.1 Sanitasi Input
- Semua input pengguna yang dirender ke DOM wajib melalui mekanisme sanitasi yang sesuai.
- Khusus HTML/Rich Text: HTML mentah dari pengguna tidak boleh langsung dirender. Sanitized HTML hanya boleh digunakan jika format tersebut telah disetujui pada Data Contract. Markdown juga harus diproses dengan renderer/sanitizer yang aman apabila nantinya digunakan.

13.2 URL / Link
Jika fitur Link (#20) diimplementasikan, URL harus menggunakan whitelist scheme.
| Scheme | Status |
|---|---|
| "https:" | ✅ Diizinkan |
| "http:" | ✅ Diizinkan |
| "mailto:" | ✅ Diizinkan |
| "javascript:" | ❌ Dilarang |
| "data:" | ❌ Dilarang |
| "vbscript:" | ❌ Dilarang |
| Scheme lain | ❌ Dilarang |

Contoh validasi:
```javascript
function isSafeUrl(url) { 
  try { 
    const parsed = new URL(url); 
    return ['https:', 'http:', 'mailto:'].includes(parsed.protocol); 
  } catch { 
    return false; 
  } 
}
```

13.3 LocalStorage Security
- LocalStorage tidak boleh digunakan untuk menyimpan password, credential, API key, session token, atau secret.
- Data pengguna tidak boleh dikirim ke server eksternal.
- Backup file dianggap sebagai data pengguna dan tidak boleh diproses ke layanan eksternal.
- Aplikasi tidak boleh menambahkan analytics/tracking eksternal tanpa persetujuan Project Owner.

13.4 Service Worker Security
- Service Worker hanya boleh melakukan caching dan operasi lokal yang diperlukan aplikasi.
- Tidak boleh melakukan sinkronisasi ke backend eksternal.
- Tidak boleh melakukan fetch ke endpoint yang tidak didefinisikan dalam spesifikasi.
- Referensi lama seperti "/api/sync" dan "/api/notes/latest" harus dihapus jika memang tidak diperlukan.
- "sync" dan "periodicsync" tidak boleh digunakan hanya sebagai placeholder.

ATURAN WAJIB --- BUILD & DEPLOY
| Item | Ketentuan |
|---|---|
| Build Tool | AppMint |
| Android Studio | Tidak digunakan untuk build proyek ini |
| AIDE | Tidak digunakan untuk build proyek ini |
| Input | ZIP proyek |
| Output | APK Android |
| Runtime | Android WebView |
| Offline | Fungsi inti harus bekerja tanpa internet |

14.1 Build Specification
| Parameter | Nilai | Status |
|---|---|---|
| Package/Application ID Production | `com.axionneuralis.axnnote` | Project Owner Decision |
| Package/Application ID Beta/Testing | `com.axnnotebeta.app` | Project Owner Decision |
| Version Name | `2.5.0` | Ditentukan |
| Version Code | `2` | Project Owner Decision |
| Min Android Version | Android 7 / API 24 | Project Owner Decision |
| Target Android Version | Android 11–15, build AppMint menggunakan target tertinggi yang didukung, disarankan Android 15 / API 35 | Project Owner Decision |
| Orientation | Portrait | Ditentukan |
| Build Type Production | Release | Ditentukan |
| Build Type Testing | Release/Debug sesuai kebutuhan testing | Diperbolehkan untuk testing |
| Signing | Release key telah tersedia; key tidak disimpan di repository/ZIP | Project Owner Decision |

**Tambahan Build Metadata**
```text
Custom User Agent Production Suffix:
AXNNote/2.5.0 (Android; com.axionneuralis.axnnote)

Custom User Agent Beta/Testing Suffix:
AXNNote-Beta/2.5.0 (Android; com.axnnotebeta.app)

Full User Agent Production:
Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 AXNNote/2.5.0 (com.axionneuralis.axnnote)
```

14.2 Ukuran Target
Ukuran harus dibedakan berdasarkan artefak.
| Artefak | Target | Status |
|---|---|---|
| Web Assets | Sekecil mungkin | Target optimasi |
| Source ZIP | Sekecil mungkin | Target optimasi |
| APK | Sekecil mungkin | Target optimasi |

Batas angka final untuk ZIP dan APK ditetapkan setelah baseline build pertama tersedia.
Tidak boleh menetapkan batas ukuran yang tidak dapat diverifikasi.

14.3 Build Acceptance
APK production hanya dapat dianggap selesai apabila:
- APK berhasil dibuat melalui AppMint.
- APK dapat di-install pada perangkat target.
- Aplikasi dapat dibuka.
- Fungsi inti bekerja.
- Tidak membutuhkan internet untuk fungsi offline.
- Data LocalStorage tetap bertahan setelah restart.
- Backup/restore bekerja.
- Tidak ada error kritis.
- Test APK final mendapatkan PASS.
- Version Name dan Version Code sesuai spesifikasi.

DATA CONTRACT --- LOCALSTORAGE SCHEMA
15.1 Prinsip
- LocalStorage adalah storage utama aplikasi.
- Data aplikasi disimpan dalam JSON.
- Semua perubahan schema wajib mempertahankan backward compatibility atau menyediakan migration.

15.2 Storage Keys
Minimal aplikasi menggunakan key yang konsisten.
AXN_NOTE_DATA
AXN_NOTE_SETTINGS
Jika implementasi memilih satu root object, key utama dapat menggunakan: AXN_NOTE_DATA dan berisi:
```json
{ "schemaVersion": 1, "folders": [], "files": [], "settings": {} }
```
Keputusan implementasi final harus konsisten dan didokumentasikan pada Blueprint.

15.3 Root Data Object
Struktur konseptual:
```json
{ "schemaVersion": 1, "folders": [], "files": [], "settings": {} }
```
| Field | Type | Required | Keterangan |
|---|---|---|---|
| "schemaVersion" | number | Ya | Versi schema |
| "folders" | array | Ya | Semua folder |
| "files" | array | Ya | Semua file/catatan |
| "settings" | object | Ya | Pengaturan aplikasi |

15.4 Folder Object
```json
{ "id ": "folder_abc123 ", "name ": "Projects ", "parentId ": null, "createdAt ": "2026-08-09T00:00:00.000Z ", "modifiedAt ": "2026-08-09T00:00:00.000Z " }
```
| Field | Type | Required | Keterangan |
|---|---|---|---|
| "id" | string | Ya | ID unik |
| "name" | string | Ya | Nama folder |
| "parentId" | string/null | Ya | Parent folder |
| "createdAt" | string | Ya | ISO 8601 timestamp |
| "modifiedAt" | string | Ya | ISO 8601 timestamp |

15.5 File Object
```json
{ "id ": "file_abc123 ", "name ": "notes.txt ", "parentId ": "folder_abc123 ", "content ": "Example content ", "createdAt ": "2026-08-09T00:00:00.000Z ", "modifiedAt ": "2026-08-09T00:00:00.000Z ", "notified ": false }
```
| Field | Type | Required | Keterangan |
|---|---|---|---|
| "id" | string | Ya | ID unik |
| "name" | string | Ya | Nama file/catatan |
| "parentId" | string/null | Ya | Folder induk |
| "content" | string | Ya | Konten plain text pada schema saat ini |
| "createdAt" | string | Ya | Waktu dibuat |
| "modifiedAt" | string | Ya | Waktu terakhir diubah |
| "notified" | boolean | Ya | Status notifikasi |

15.6 Settings Object
Struktur minimum:
```json
{ "theme": "light", "viewMode": "list" }
```
Field settings dapat berkembang melalui schema migration.
Nilai yang tidak dikenal tidak boleh menyebabkan aplikasi crash.

15.7 ID Rules
- Setiap folder dan file wajib memiliki ID unik.
- ID tidak boleh berubah hanya karena rename.
- ID tidak boleh di-regenerate ketika restore.
- ID digunakan sebagai referensi internal.
- "parentId" harus menunjuk ke folder yang valid atau "null".
- Circular folder reference dilarang.

15.8 Root Folder
- "parentId: null" berarti item berada pada root.
- Item root tidak boleh memiliki parent yang tidak ada.

15.9 Timestamp
- Semua timestamp menggunakan format ISO 8601.
- Contoh: 2026-08-09T00:00:00.000Z
- "createdAt" tidak boleh berubah setelah object dibuat.
- "modifiedAt" berubah ketika data object mengalami perubahan.

15.10 Content Format Saat Ini
Pada schema saat ini: content = plain text. Tidak ada HTML mentah. Tidak ada Markdown sebagai format storage default.

15.11 Rich Text Future Schema
Jika Rich Text Editing (#16) disetujui: Format storage wajib ditentukan sebelum implementasi. Format harus ditambahkan ke Data Contract. Migration strategy wajib tersedia. HTML mentah tidak boleh disimpan tanpa sanitasi. Pilihan format: sanitized HTML subset; atau Markdown. Keputusan final berada pada Project Owner.

15.12 Schema Version
- "schemaVersion" digunakan untuk migration.
- Aturan: Schema baru tidak boleh merusak data lama. Migration harus deterministik. Migration tidak boleh menghapus data tanpa keputusan eksplisit. Backup dilakukan sebelum migration destruktif. Versi schema harus dicatat dalam backup. Aplikasi harus dapat menolak schema yang tidak dikenal dengan aman.

15.13 Validation
Sebelum data hasil restore/migration disimpan: Parse JSON. Validasi "schemaVersion". Validasi "folders". Validasi "files". Validasi "settings". Validasi ID. Validasi parent references. Validasi tipe data. Jika valid → baru replace data aktif. Jika salah satu validasi gagal, data aktif tidak boleh diubah.

15.14 Kapasitas LocalStorage
Jika penyimpanan gagal atau kapasitas tidak mencukupi: Data yang sedang diedit wajib dipertahankan sementara di memory. Pengguna harus menerima pesan error yang jelas. Data yang belum tersimpan tidak boleh hilang secara diam-diam. Aplikasi tidak boleh terus mencoba menulis tanpa batas. Statistik storage boleh ditampilkan pada Settings.

ATURAN BACKUP / RESTORE / EXPORT
16.1 Definisi
| Operasi | Definisi | Scope |
|---|---|---|
| Backup | Ekspor seluruh database aplikasi | Semua data |
| Restore | Mengganti data aplikasi dengan backup valid | Semua data |
| Export Individual | Ekspor satu file/catatan | Satu item |

16.2 Backup Format
```json
{ "schemaVersion": 1, "folders": [], "files": [], "settings": {} }
```
Ketentuan: Format JSON. Encoding UTF-8. "schemaVersion" wajib. Folder dan file wajib dipertahankan. ID wajib dipertahankan. Timestamp wajib dipertahankan. "settings" termasuk backup. Pretty print diperbolehkan. Nama default: axn_note_backup_YYYY-MM-DD.json

16.3 Restore
Mode default: REPLACE
Alur wajib: Import File ↓ Parse JSON ↓ Validate Schema ↓ Validate Structure ↓ Validate References ↓ Confirm User ↓ Replace Active Data ↓ Persist ↓ Verify
Aturan: Restore wajib meminta konfirmasi eksplisit. JSON invalid → tolak. Schema invalid → tolak. Struktur invalid → tolak. Reference invalid → tolak. Data aktif tidak boleh diubah sebelum validasi selesai. ID dan timestamp tidak boleh dibuat ulang. Merge belum tersedia. Jika "schemaVersion" berbeda, aplikasi harus: melakukan migration jika migration tersedia; atau menolak restore dengan pesan yang jelas. Backup lama tidak boleh diam-diam ditimpa sebelum restore tervalidasi.

16.4 Export Individual
Format saat ini: .txt. Nama: {nama_file}.txt. Isi: Konten file saja. Metadata tidak disertakan pada format ".txt". Format ".md" atau ".json" dapat ditambahkan melalui perubahan spesifikasi resmi.

ATURAN AUTO-SAVE
Fitur Auto-Save (#24) belum terimplementasi pada kode saat ini. Aturan berikut berlaku ketika fitur diimplementasikan.
17.1 Model
User mengetik ↓ Input Event ↓ Debounce 800ms ↓ Validasi ↓ Save LocalStorage ↓ Update modifiedAt ↓ Indikator "Tersimpan"
17.2 Parameter
| Parameter | Ketentuan |
|---|---|
| Trigger | Input event |
| Debounce | 800ms |
| Save on Blur | Ya |
| Save on Close | Ya jika ada perubahan |
| Indicator | "Tersimpan" / "Belum tersimpan" |
| Failure | Pertahankan data di memory + tampilkan error |
| Per-character write | Dilarang |

17.3 Aturan Timestamp
Auto-save: Tidak mengubah "createdAt". Mengubah "modifiedAt" hanya jika konten benar-benar berubah. Tidak boleh memperbarui timestamp jika tidak ada perubahan.

ERROR HANDLING POLICY
Semua operasi yang berpotensi gagal wajib memiliki error handling yang sesuai.
18.1 Operasi yang Wajib Ditangani
| Operasi | Perilaku |
|---|---|
| "localStorage.getItem()" | Tangani kegagalan dan tampilkan error |
| "localStorage.setItem()" | Tangani quota/storage error |
| "JSON.parse()" | Tolak data invalid |
| "JSON.stringify()" | Tangani serialization error |
| File import | Tangani file read error |
| File export | Tangani Blob/download error |
| Backup | Jangan menghasilkan backup parsial |
| Restore | Jangan mengubah data jika validasi gagal |
| Service Worker registration | Graceful degradation |
| DOM operation kritis | Tangani error sesuai konteks |

"try/catch" digunakan jika memang diperlukan oleh operasi yang berpotensi throw.
18.2 Pure Function
Pure function sederhana yang tidak melakukan I/O, DOM access, parsing, atau operasi eksternal tidak wajib menggunakan "try/catch".
18.3 Error Message
Pesan kepada pengguna menggunakan Bahasa Indonesia. Pesan harus menjelaskan masalah secara sederhana. Jangan menampilkan stack trace kepada pengguna. Error teknis boleh dicatat melalui "console.warn()" selama development. Production tidak boleh membocorkan data sensitif melalui console. Error tidak boleh diabaikan secara diam-diam.
18.4 Graceful Degradation
Jika fitur non-kritis gagal: Aplikasi tetap harus dapat digunakan. Fungsi inti tidak boleh ikut crash. Pengguna harus diberi feedback. Data yang belum tersimpan harus dipertahankan jika memungkinkan.

NON-FUNCTIONAL REQUIREMENTS
19.1 Performance
| ID | Requirement | Target | Status |
|---|---|---|---|
| PERF-001 | Startup UI | UI utama tampil ≤ 2 detik pada perangkat target setelah WebView siap | ⬜ |
| PERF-002 | Search | Pencarian tidak menyebabkan freeze yang terlihat pada dataset normal | ⬜ |
| PERF-003 | Navigation | Navigasi folder responsif | ⬜ |
| PERF-004 | Save | Save tidak menyebabkan UI freeze yang terlihat | ⬜ |
| PERF-005 | Backup | Export dapat menyelesaikan proses tanpa crash pada dataset normal | ⬜ |

19.2 Reliability
| ID | Requirement |
|---|---|
| REL-001 | Reload tidak boleh menghapus data tersimpan |
| REL-002 | Restore invalid tidak boleh merusak data aktif |
| REL-003 | Storage failure harus menghasilkan feedback |
| REL-004 | Crash pada fitur non-kritis tidak boleh menyebabkan seluruh aplikasi gagal |
| REL-005 | Data aktif harus memiliki struktur valid sebelum disimpan |

19.3 Offline
| ID | Requirement |
|---|---|
| OFF-001 | Aplikasi dapat dibuka tanpa internet setelah aset lokal tersedia |
| OFF-002 | Membuat folder dapat dilakukan offline |
| OFF-003 | Membuat/edit file dapat dilakukan offline |
| OFF-004 | Search dapat dilakukan offline |
| OFF-005 | Backup/restore dapat dilakukan offline |
| OFF-006 | Tidak ada ketergantungan pada API eksternal untuk fungsi inti |

19.4 Storage
| ID | Requirement |
|---|---|
| STO-001 | LocalStorage menjadi storage utama |
| STO-002 | Schema memiliki versioning |
| STO-003 | Data memiliki struktur yang tervalidasi |
| STO-004 | Migration tidak boleh menyebabkan silent data loss |
| STO-005 | Backup mempertahankan ID dan timestamp |

19.5 Security
| ID | Requirement |
|---|---|
| SEC-001 | Tidak menggunakan "eval()" |
| SEC-002 | Input pengguna disanitasi |
| SEC-003 | URL menggunakan whitelist scheme |
| SEC-004 | Tidak menyimpan credential/token |
| SEC-005 | Tidak mengirim data pengguna ke server |
| SEC-006 | Service Worker tidak melakukan sync eksternal |

19.6 Accessibility
| ID | Requirement |
|---|---|
| A11Y-001 | WCAG 2.1 AA untuk kontras |
| A11Y-002 | Touch target ≥ 44×44px |
| A11Y-003 | Interactive icon memiliki label |
| A11Y-004 | Status tidak hanya dibedakan dengan warna |
| A11Y-005 | Focus state terlihat pada elemen relevan |

19.7 Compatibility
Target utama: Android WebView. Mobile width: 360px--480px. Tablet/Desktop width: maksimum 600px. Orientation: Portrait. Versi Android minimum dan target Android telah ditetapkan pada Build Specification v3.1.

19.8 Privacy
Tidak ada akun pengguna. Tidak ada backend eksternal untuk data catatan. Tidak ada telemetry eksternal tanpa persetujuan. Data pengguna tetap berada pada perangkat kecuali pengguna sendiri melakukan export.

OUT OF SCOPE
Fitur berikut tidak menjadi bagian dari scope default AXN Note versi ini kecuali Project Owner memberikan keputusan baru: User account, Authentication, Cloud synchronization, Online database, Backend server, Social networking, Collaborative editing, External analytics/tracking, External AI service, Online-only functionality, Mandatory internet connection.

STRUKTUR FOLDER
```text
axn-note/
│
├── index.html
├── manifest.json
├── sw.js
│
├── assets/
│   └── icons/
│       ├── icon-1.svg
│       ├── icon-2.svg
│       ├── ...
│       └── icon-23.svg
│
├── README.md
├── .gitignore
└── LICENSE
```
21.1 Aturan
Struktur tidak boleh diubah tanpa persetujuan Project Owner. Folder baru harus didokumentasikan. File baru harus ditambahkan ke Daftar File. File yang tidak terdaftar tidak boleh menjadi bagian release. Nama file SVG placeholder telah disiapkan untuk memenuhi struktur.

DAFTAR FILE
22.1 File Inti
| File | Lokasi | Status | Penanggung Jawab |
|---|---|---|---|
| "index.html" | "/" | 🟡 VALIDASI | GP-03 |
| "manifest.json" | "/" | 🟡 VALIDASI | GP-06 |
| "sw.js" | "/" | 🟡 VALIDASI | GP-06 |

22.2 Asset SVG
| File | Lokasi | Status | Penanggung Jawab |
|---|---|---|---|
| "icon-1.svg " s/d "icon-23.svg " | "/assets/icons/ " | 🟡 VALIDASI | GP-04 |
«Placeholder build-ready telah disiapkan. Aset final menunggu GP-04 / Project Owner.»

22.3 Dokumentasi
| File | Lokasi | Status | Penanggung Jawab |
|---|---|---|---|
| "README.md" | "/" | 🟡 VALIDASI | GP-01 |
| ".gitignore" | "/" | 🟡 VALIDASI | GP-01 |
| "LICENSE" | "/" | 🟡 VALIDASI | GP-01 |

SPESIFIKASI TEKNIS
| Item | Spesifikasi |
|---|---|
| Language | HTML5, CSS3, JavaScript ES6+ |
| Framework | Tidak ada |
| Runtime | Browser/WebView |
| Storage | LocalStorage |
| Offline | Service Worker |
| Manifest | "manifest.json" |
| Build | AppMint |
| Platform | Android |
| Orientation | Portrait |
| Primary Width | 360--480px |
| Max Application Width | 600px |
| External CDN | Tidak |
| External Font | Tidak |
| External Database | Tidak |
| Backend | Tidak |
| Authentication | Tidak |
| Core Network Dependency | Tidak |

ROADMAP
Roadmap ini adalah rencana tahapan resmi pengembangan AXN Note. Roadmap bersifat eksekusi; Bible tetap memiliki otoritas lebih tinggi. (Lihat dokumen Roadmap v3.1 terpisah).

BLUEPRINT ARSITEKTUR
Blueprint adalah dokumen teknis pendukung resmi. Jika terjadi konflik, Bible tetap memiliki otoritas lebih tinggi. (Lihat dokumen Blueprint v3.1 terpisah).

TESTING & ACCEPTANCE CRITERIA
26.1 Format Test Case
Setiap test case wajib memiliki: ID, Feature, Precondition, Input, Expected Result, Actual Result, Status, Tester, Date, Notes. Status: PASS, FAIL, BLOCKED, NOT TESTED.
26.2 Test Matrix --- Current Features
(TC-001 s/d TC-025 tetap sama seperti v3.0, status menunggu QA).
26.3 Test Matrix --- Planned Features
(TC-026 s/d TC-038 tetap sama seperti v3.0, status ⬜).
26.4 Acceptance Criteria
Sebuah fitur dapat dinyatakan PASS apabila: Input valid menghasilkan output yang diharapkan. Input invalid ditangani dengan aman. Data tersimpan jika fitur membutuhkan persistence. Reload tidak merusak data. Fitur tidak merusak fitur lain. Fitur dapat digunakan sesuai UI specification. Error state dapat ditangani. Fitur tidak menambahkan ketergantungan internet. Security requirement terpenuhi jika relevan. QA memberikan PASS.
26.5 Aturan Testing
GP-05 bertanggung jawab menjalankan test matrix. Hasil testing dilaporkan kepada GP-01. Test case yang FAIL harus memiliki catatan. Test case BLOCKED harus memiliki alasan. Fitur tidak boleh berstatus 🟢 SELESAI tanpa test PASS. Setelah perubahan besar, regression test wajib dijalankan. Release build harus diuji kembali meskipun development build telah lulus.

ATURAN KOMUNIKASI TIM
| Aturan | Ketentuan |
|---|---|
| Satu Pintu | Komunikasi teknis melalui Project Owner atau GP-01 |
| Laporan | Anggota melaporkan progress ke GP-01 |
| Keputusan Final | Project Owner memiliki keputusan final |
| Dokumentasi | Keputusan penting wajib dicatat |
| Konflik | Diselesaikan sesuai Bab 3 |
| Update Bible | GP-01 memperbarui atas persetujuan Project Owner |

27.1 Format Laporan Progress
Minimal: Tanggal, Anggota, Task, Status, Perubahan, Masalah, Blocker, Next Step.

LAMPIRAN
28.1 Istilah
(Sama seperti v3.0)
28.2 Current Known Issues
(Telah diselesaikan pada v3.1: "sw.js" dibersihkan, manifest merujuk placeholder SVG, "console.log()" dibersihkan, "SUBSCRIPTION_KEY" dibersihkan, footer version disesuaikan).
28.3 Catatan Khusus
File SVG placeholder build-ready telah disiapkan. Aplikasi bukan PWA murni. Build dilakukan melalui AppMint. Android Studio dan AIDE bukan bagian dari build workflow proyek ini. Bible tetap menjadi dokumen pengendali utama. Placeholder "TBD" untuk build spec telah diisi pada v3.1.
28.4 Aturan Finalisasi Dokumen
Bible dapat diberi status FINAL hanya apabila:
[x] Struktur dokumen lengkap
[x] Tidak ada bab yang terpotong
[x] Status lifecycle didefinisikan
[x] DoD didefinisikan
[x] Data Contract didefinisikan
[x] Schema Version didefinisikan
[x] Backup/Restore semantics didefinisikan
[x] Auto-Save rules didefinisikan
[x] Error Handling Policy didefinisikan
[x] NFR didefinisikan
[x] Security Policy didefinisikan
[x] Accessibility criteria didefinisikan
[x] Testing structure didefinisikan
[x] Acceptance Criteria didefinisikan
[x] Seluruh TBD Build Specification sudah diputuskan (v3.1)
[x] Blueprint final telah disinkronkan
[x] Project Owner memberikan approval final

28.5 Approval
| Peran | Nama | Status |
|---|---|---|
| Project Owner | User | 🟢 APPROVED / RESMI |
| Project Lead / Architect | QWEN | 🟢 FINALIZED |
| Data Engineer | TBD | ⬜ |
| Frontend Developer | TBD | ⬜ |
| Asset / Design | TBD | ⬜ |
| QA / Tester | TBD | ⬜ |
| Build & Deploy | TBD | ⬜ |

Dokumen ini dibuat oleh GP-01 (QWEN) atas arahan Project Owner.
Pernyataan Final: Project Owner telah meresmikan Bible ini sebagai sumber kebenaran tunggal (Single Source of Truth) proyek. Blueprint dan Roadmap yang dirujuk di dalamnya adalah dokumen pendukung resmi dan tidak boleh mengesampingkan Bible.

Bible Version: 3.1 FINAL
Application Version: 2.5.0 (target)
Status: 🟢 RESMI / APPROVED
Terakhir diperbarui: 2026-08-09

--- Akhir Dokumen Bible v3.1 FINAL ---