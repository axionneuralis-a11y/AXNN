"""
Database AXNN.
Milik Tim B.

Aturan:
- File ini hanya mengurus koneksi dan struktur database.
- Tidak boleh ada logika UI.
- Tidak boleh ada logika bisnis kompleks.
- Semua tabel wajib dibuat idempotent dengan IF NOT EXISTS.
"""

import os
import sqlite3

from utils.constants import (
    DB_FILENAME,
    DEFAULT_FOLDER_NAME,
    DEFAULT_FOLDER_COLOR,
)


SQL_SCHEMA = """
CREATE TABLE IF NOT EXISTS folders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(100) NOT NULL UNIQUE,
    color TEXT(7) NOT NULL DEFAULT '#2196F3',
    is_default INTEGER NOT NULL DEFAULT 0 CHECK (is_default IN (0, 1))
);

CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT(200) NOT NULL,
    content TEXT NOT NULL DEFAULT '',
    folder_id INTEGER,
    reminder_at DATETIME,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (folder_id) REFERENCES folders(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT(500) NOT NULL,
    is_done INTEGER NOT NULL DEFAULT 0 CHECK (is_done IN (0, 1)),
    folder_id INTEGER,
    due_date DATETIME,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (folder_id) REFERENCES folders(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS calc_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expression TEXT NOT NULL,
    result TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS code_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT(255) NOT NULL,
    language TEXT(50),
    content TEXT NOT NULL DEFAULT '',
    is_saved INTEGER NOT NULL DEFAULT 0 CHECK (is_saved IN (0, 1)),
    storage_path TEXT,
    last_opened DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT
);

CREATE INDEX IF NOT EXISTS idx_notes_folder_id ON notes(folder_id);
CREATE INDEX IF NOT EXISTS idx_notes_updated_at ON notes(updated_at);
CREATE INDEX IF NOT EXISTS idx_todos_folder_id ON todos(folder_id);
CREATE INDEX IF NOT EXISTS idx_todos_created_at ON todos(created_at);
CREATE INDEX IF NOT EXISTS idx_code_files_filename ON code_files(filename);
CREATE INDEX IF NOT EXISTS idx_code_files_is_saved ON code_files(is_saved);
"""


def get_db_path():
    """
    Mendapatkan path database AXNN.

    Returns:
        str path database.
    """
    custom_path = os.environ.get("AXNN_DB_PATH")
    if custom_path:
        return custom_path

    base_dir = os.path.join(os.path.expanduser("~"), ".axnn")
    return os.path.join(base_dir, DB_FILENAME)


def get_connection(db_path=None):
    """
    Membuat koneksi SQLite dengan foreign key aktif.

    Args:
        db_path: Path database opsional. Jika None pakai path default.

    Returns:
        sqlite3.Connection
    """
    path = db_path or get_db_path()
    folder = os.path.dirname(path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn


def _seed_default_folder(conn):
    """
    Memastikan folder default selalu ada.

    Args:
        conn: sqlite3.Connection aktif.
    """
    cursor = conn.execute(
        """
        SELECT id
        FROM folders
        WHERE is_default = 1
        LIMIT 1
        """
    )

    if cursor.fetchone() is None:
        try:
            conn.execute(
                """
                INSERT INTO folders (name, color, is_default)
                VALUES (?, ?, 1)
                """,
                (DEFAULT_FOLDER_NAME, DEFAULT_FOLDER_COLOR),
            )
        except sqlite3.IntegrityError:
            # Jika folder bernama Default sudah ada tetapi belum ditandai default.
            conn.execute(
                """
                UPDATE folders
                SET is_default = 1
                WHERE name = ?
                """,
                (DEFAULT_FOLDER_NAME,),
            )

        # Jika tetap belum ada default, ambil folder pertama sebagai default.
        cursor = conn.execute(
            """
            SELECT COUNT(*) AS total
            FROM folders
            WHERE is_default = 1
            """
        )
        row = cursor.fetchone()

        if row and row["total"] == 0:
            conn.execute(
                """
                UPDATE folders
                SET is_default = 1
                WHERE id = (
                    SELECT MIN(id) FROM folders
                )
                """
            )


def init_db(db_path=None):
    """
    Inisialisasi database AXNN.
    Dipanggil pertama kali saat aplikasi dibuka.

    Args:
        db_path: Path database opsional.

    Returns:
        True jika sukses.

    Raises:
        sqlite3.Error jika gagal.
    """
    conn = get_connection(db_path)

    try:
        conn.executescript(SQL_SCHEMA)
        _seed_default_folder(conn)
        conn.commit()
        return True
    except sqlite3.Error:
        conn.rollback()
        raise
    finally:
        conn.close()