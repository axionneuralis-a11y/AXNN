"""
Model Riwayat Kalkulator.
Disiapkan untuk F004.
Logika kalkulator penuh dilanjutkan pada tahap migrasi fitur lama.
"""

from utils import database
from utils import helpers


def add(expression, result):
    """
    Menyimpan riwayat perhitungan.

    Args:
        expression: Rumus perhitungan.
        result: Hasil perhitungan.

    Returns:
        int id riwayat baru.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO calc_history (expression, result, created_at)
            VALUES (?, ?, datetime('now'))
            """,
            (expression, result),
        )

        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def get_history(limit=50):
    """
    Mengambil riwayat kalkulator terbaru.

    Args:
        limit: jumlah riwayat.

    Returns:
        list of dict riwayat.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            SELECT *
            FROM calc_history
            ORDER BY created_at DESC, id DESC
            LIMIT ?
            """,
            (limit,),
        )

        return helpers.rows_to_list(cursor.fetchall())
    finally:
        conn.close()


def clear():
    """
    Menghapus semua riwayat kalkulator.

    Returns:
        int jumlah baris yang dihapus.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute("DELETE FROM calc_history")
        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()