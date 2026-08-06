README.md

```markdown
# AXNN - All-in-One Productivity Suite

![AXNN Logo](assets/icon.png)

AXNN adalah aplikasi produktivitas all-in-one yang dirancang untuk membantu Anda mengelola catatan, tugas, folder, kalkulator, dan banyak lagi dalam satu platform terintegrasi. Dibangun dengan Kivy framework untuk mendukung multi-platform (Android, iOS, Windows, macOS, Linux).

## ✨ Fitur Utama

- 📝 **Notes Management** - Buat, edit, dan kelola catatan dengan rich text
- ✅ **To-Do Lists** - Manajemen tugas dengan prioritas dan deadline
- 📁 **Folder System** - Organisasi konten dengan sistem folder hierarkis
- 🧮 **Calculator** - Kalkulator cerdas dengan riwayat perhitungan
- 📅 **Calendar** - Kalender terintegrasi untuk manajemen jadwal
- 🔔 **Notifications** - Sistem notifikasi dan pengingat
- 💾 **Backup & Restore** - Backup dan restore data dengan mudah
- 📤 **Export/Import** - Ekspor dan impor data dalam berbagai format
- 🎨 **Custom Themes** - Dukungan tema gelap dan terang
- 📱 **Multi-Platform** - Berjalan di Android, iOS, Windows, macOS, dan Linux

## 🏗️ Struktur Proyek

```

AXNN/
├── main.py                 # Entry point aplikasi
├── models/                 # Model data
├── controllers/            # Logic controller
├── screens/                # Screen classes
├── kv_files/              # Kivy UI definitions
├── components/            # Reusable components
├── utils/                 # Utility functions
├── assets/                # Static assets
├── data/                  # Data files
├── docs/                  # Dokumentasi
└── bin/                   # Executable binaries

```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/AXNN.git
cd AXNN
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

Build for Android (APK)

Menggunakan Buildozer:

```bash
buildozer init
buildozer android debug deploy run
```

Build for Desktop

```bash
pip install pyinstaller
pyinstaller main.spec
```

📦 Dependencies

· kivy >= 2.1.0 - GUI Framework
· kivymd >= 1.1.1 - Material Design Components
· sqlite3 - Database (built-in)
· plyer - Platform-specific APIs
· pillow - Image processing
· requests - HTTP requests
· json - Data serialization (built-in)

📚 Documentation

Dokumentasi lengkap tersedia di folder docs/:

· Project Bible - Dokumentasi lengkap proyek
· Proposal - Proposal awal proyek
· User Guide - Panduan pengguna
· Developer Guide - Panduan developer
· Changelog - Riwayat perubahan
· Test Cases - Checklist pengujian

🧪 Testing

Untuk menjalankan tes:

```bash
python -m pytest tests/
```

🤝 Kontribusi

Kami menyambut kontribusi dari siapa pun! Silakan baca Developer Guide untuk panduan berkontribusi.

Cara Berkontribusi

1. Fork repository
2. Buat branch fitur baru (git checkout -b feature/AmazingFeature)
3. Commit perubahan (git commit -m 'Add some AmazingFeature')
4. Push ke branch (git push origin feature/AmazingFeature)
5. Buka Pull Request

📝 License

Distributed under the MIT License. See LICENSE for more information.

📞 Kontak

· Project Maintainer: [azriel]
· Email: your.email@example.com
· Project Link: https://github.com/yourusername/AXNN

🙏 Acknowledgments

· Kivy - Framework GUI
· KivyMD - Material Design
· Buildozer - Build tool for Android

---

Made with ❤️ by AXNN Team

```
