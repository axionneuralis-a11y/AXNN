# AXN Note

AXN Note adalah aplikasi manajemen file dan catatan ringan, cepat, dan sepenuhnya offline untuk Android. Aplikasi dibangun menggunakan HTML, CSS, dan JavaScript single-file, lalu dibungkus menjadi APK melalui AppMint dengan runtime Android WebView.

## Versi

- Application Version: 2.5.0
- Version Code: 2
- Status source: final build-ready
- Build tool: AppMint
- Platform: Android WebView
- Orientasi: Portrait

## Konfigurasi Build Production

Gunakan nilai berikut pada AppMint:

| Item | Nilai |
|---|---|
| Package / Application ID | `com.axionneuralis.axnnote` |
| Version Name | `2.5.0` |
| Version Code | `2` |
| Min Android | Android 7 / API 24 |
| Target Android | Android 15 / API 35, atau target tertinggi yang tersedia pada rentang 11–15 |
| Orientation | Portrait |
| Signing | Release |
| Input | ZIP proyek |
| Output | APK Android |

### Custom User Agent Production

```text
Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 AXNNote/2.5.0 (com.axionneuralis.axnnote)
```

## Konfigurasi Build Beta / Testing

Jika membangun APK beta/testing, ganti identitas berikut pada AppMint atau pada salinan manifest:

| Item | Nilai Beta |
|---|---|
| Package / Application ID | `com.axnnotebeta.app` |
| Version Name | `2.5.0` |
| Version Code | `2` |
| Min Android | Android 7 / API 24 |
| Target Android | Android 15 / API 35, atau target tertinggi yang tersedia pada rentang 11–15 |
| Orientation | Portrait |
| Signing | Release / testing sesuai kebutuhan |

### Custom User Agent Beta

```text
Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 AXNNote-Beta/2.5.0 (com.axnnotebeta.app)
```

## Struktur Proyek

```text
axn-note/
├── index.html
├── manifest.json
├── sw.js
├── assets/
│   └── icons/
│       ├── icon-1.svg
│       ├── icon-2.svg
│       ├── ...
│       └── icon-23.svg
├── README.md
├── .gitignore
└── LICENSE
```

## Penyimpanan

Aplikasi menggunakan LocalStorage sebagai storage utama dengan key:

```text
AXN_NOTE_DATA
```

Format data:

```json
{
  "schemaVersion": 1,
  "folders": [],
  "files": [],
  "settings": {
    "theme": "light",
    "viewMode": "list"
  }
}
```

Jika ditemukan data lama yang tidak valid, aplikasi menyimpan salinan mentah ke key recovery:

```text
AXN_NOTE_DATA_RECOVERY
```

## Fitur Release-Critical

Fitur yang tersedia pada build ini:

- Buat folder
- Buat file
- Edit file plain text
- Rename
- Move
- Delete
- Search
- Breadcrumb
- Dark/Light mode
- Backup JSON
- Restore JSON
- Local notification
- Statistics
- Context menu
- Feedback mailto

## Catatan Keamanan

- Tidak menggunakan `eval()`.
- Tidak menggunakan `Function()` untuk input pengguna.
- Tidak menggunakan `document.write()`.
- Konten pengguna dirender melalui API DOM text-safe.
- Tidak ada endpoint API eksternal.
- Service Worker hanya untuk cache lokal.
- Tidak ada sinkronisasi cloud.
- Tidak ada credential/token/secret di LocalStorage.

## Catatan Aset

File SVG pada `assets/icons/` saat ini adalah placeholder valid build-ready. Jika aset final dari GP-04 tersedia, replace file SVG tanpa perlu mengubah `index.html`, `sw.js`, atau struktur proyek.

## Release Key

Release key tidak boleh dimasukkan ke repository atau ZIP. Setelah key tersedia:

1. Gunakan signing Release pada AppMint.
2. Pastikan alias/key password disimpan aman.
3. Build APK production.
4. Jalankan validasi APK sesuai roadmap Phase E.

## Application Changelog

| Tanggal | App Ver | Scope | Tipe | Deskripsi |
|---|---|---|---|---|
| 2026-08-09 | 2.5.0 | APP | INIT | Source final build-ready AXN Note untuk AppMint production ZIP |