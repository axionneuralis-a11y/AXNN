import sqlite3
import os
import logging
from typing import Optional

# Konfigurasi Logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Path database (Private App Storage di Android, fallback ke direktori home saat dev)
DB_DIR = os.getenv('AXNN_DB_DIR', os.path.join(os.path.expanduser('~'), '.axnn'))
DB_NAME = 'axnn.db'
DB_PATH = os.path.join(DB_DIR, DB_NAME)

def get_db_connection() -> sqlite3.Connection:
    """Mendapatkan koneksi ke database SQLite dengan row_factory dict."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Agar hasil query bisa diakses seperti dictionary
    conn.execute("PRAGMA foreign_keys = ON")  # Wajib aktif untuk relasi ON DELETE
    return conn

def init_db() -> None:
    """Inisialisasi database dan membuat semua tabel AXNN jika belum ada."""
    os.makedirs(DB_DIR, exist_ok=True)
    logger.info(f"[Tim B] Inisialisasi database di: {DB_PATH}")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Skema Tabel Wajib Sesuai Blueprint Bab 2.4
    tables = [
        """
        CREATE TABLE IF NOT EXISTS folders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT DEFAULT '#2196F3',
            is_default INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""",
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT DEFAULT '',
            folder_id INTEGER,
            reminder_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (folder_id) REFERENCES folders (id) ON DELETE SET NULL
        )""",
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            is_done INTEGER DEFAULT 0,
            folder_id INTEGER,
            due_date TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (folder_id) REFERENCES folders (id) ON DELETE SET NULL
        )""",
        """
        CREATE TABLE IF NOT EXISTS calc_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""",
        """
        CREATE TABLE IF NOT EXISTS code_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            language TEXT DEFAULT 'text',
            content TEXT DEFAULT '',
            is_saved INTEGER DEFAULT 0,
            storage_path TEXT,
            last_opened TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""",
        """
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )"""
    ]
    
    try:
        for table in tables:
            cursor.execute(table)
        
        # Insert default folder "Umum" jika kosong
        cursor.execute("SELECT COUNT(*) FROM folders WHERE is_default = 1")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO folders (name, color, is_default) VALUES (?, ?, ?)", 
                           ("Umum", "#2196F3", 1))
            
        # Insert default setting tema
        cursor.execute("SELECT COUNT(*) FROM settings WHERE key = 'theme'")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO settings (key, value) VALUES (?, ?)", 
                           ("theme", "light"))
                           
        conn.commit()
        logger.info("[Tim B] Database berhasil diinisialisasi & data default dibuat.")
    except sqlite3.Error as e:
        logger.error(f"Error inisialisasi database: {e}")
        conn.rollback()
    finally:
        conn.close() 
