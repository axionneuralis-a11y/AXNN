"""Manajemen koneksi dan inisialisasi database SQLite AXNN."""

import os
import sqlite3
from typing import Optional

# Path database di private app storage Android
DB_DIR: str = os.path.join(os.path.expanduser("~"), ".axnn")
DB_PATH: str = os.path.join(DB_DIR, "axnn.db")

DEFAULT_FOLDER_NAME: str = "Umum"
DEFAULT_FOLDER_COLOR: str = "#2196F3"


def get_db_connection() -> sqlite3.Connection:
    """Membuka koneksi SQLite dengan row_factory agar hasil berupa dict.

    Returns:
        sqlite3.Connection: Koneksi database aktif.
    """
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """Membuat semua tabel AXNN dan seed folder default.

    Dipanggil sekali saat aplikasi pertama kali dibuka (main.py).
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS folders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            color TEXT NOT NULL DEFAULT '#2196F3',
            is_default INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL DEFAULT '',
            folder_id INTEGER NOT NULL DEFAULT 1,
            reminder_at TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now','localtime')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now','localtime')),
            FOREIGN KEY (folder_id) REFERENCES folders(id)
        );

        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            is_done INTEGER NOT NULL DEFAULT 0,
            folder_id INTEGER NOT NULL DEFAULT 1,
            due_date TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now','localtime')),
            FOREIGN KEY (folder_id) REFERENCES folders(id)
        );

        CREATE TABLE IF NOT EXISTS calc_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now','localtime'))
        );

        CREATE TABLE IF NOT EXISTS code_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            language TEXT NOT NULL DEFAULT 'python',
            content TEXT NOT NULL DEFAULT '',
            is_saved INTEGER NOT NULL DEFAULT 0,
            storage_path TEXT,
            last_opened TEXT NOT NULL DEFAULT (datetime('now','localtime'))
        );

        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        """
    )

    # Seed folder default (id=1) jika belum ada
    cursor.execute(
        "INSERT OR IGNORE INTO folders (id, name, color, is_default) "
        "VALUES (1, ?, ?, 1)",
        (DEFAULT_FOLDER_NAME, DEFAULT_FOLDER_COLOR),
    )

    conn.commit()
    conn.close()
