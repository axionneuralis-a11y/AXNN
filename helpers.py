"""
Helper umum untuk Tim B.
Hanya berisi fungsi murni, tidak boleh mengandung logika UI.
"""

import re
from datetime import datetime


def ok(data=None, message="OK"):
    """
    Response sukses standar untuk Controller.

    Args:
        data: Data yang dikembalikan ke View.
        message: Pesan sukses.

    Returns:
        dict response sukses.
    """
    return {
        "success": True,
        "message": message,
        "data": data,
    }


def fail(message="Terjadi kesalahan."):
    """
    Response gagal standar untuk Controller.

    Args:
        message: Pesan error yang aman ditampilkan ke user.

    Returns:
        dict response gagal.
    """
    return {
        "success": False,
        "message": message,
        "data": None,
    }


def row_to_dict(row):
    """
    Ubah satu baris sqlite3.Row menjadi dict.

    Args:
        row: sqlite3.Row atau None.

    Returns:
        dict atau None.
    """
    if row is None:
        return None
    return dict(row)


def rows_to_list(rows):
    """
    Ubah daftar sqlite3.Row menjadi list of dict.

    Args:
        rows: Iterable sqlite3.Row.

    Returns:
        list of dict.
    """
    return [dict(row) for row in rows]


def now_sqlite():
    """
    Mengembalikan timestamp format SQLite.

    Returns:
        str timestamp.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def is_valid_hex_color(value):
    """
    Validasi warna hex 6 digit.

    Args:
        value: String warna, contoh '#2196F3'.

    Returns:
        bool True jika valid.
    """
    if not value:
        return False
    return bool(re.fullmatch(r"#[0-9A-Fa-f]{6}", value))