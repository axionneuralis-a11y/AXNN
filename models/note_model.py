"""Model catatan (tabel notes)."""

from typing import Dict, List

from models.base_model import BaseModel
from utils.database import get_db_connection


class NoteModel(BaseModel):
    """Akses data catatan."""

    table_name: str = "notes"

    @classmethod
    def get_recent(cls, limit: int = 3) -> List[Dict]:
        """Ambil catatan terbaru untuk Home.

        Args:
            limit (int): Jumlah catatan (default 3 sesuai F001).

        Returns:
            List[Dict]: Daftar catatan terbaru.
        """
        query = (
            f"SELECT id, title, content, created_at FROM {cls.table_name} "
            "ORDER BY created_at DESC LIMIT ?"
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (limit,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def get_by_folder(cls, folder_id: int) -> List[Dict]:
        """Ambil catatan dalam folder tertentu.

        Args:
            folder_id (int): ID folder.

        Returns:
            List[Dict]: Daftar catatan dalam folder.
        """
        query = (
            f"SELECT * FROM {cls.table_name} WHERE folder_id = ? "
            "ORDER BY updated_at DESC"
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (folder_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def get_by_date(cls, date_str: str) -> List[Dict]:
        """Ambil catatan yang dibuat pada tanggal tertentu (untuk Kalender).

        Args:
            date_str (str): Tanggal format YYYY-MM-DD.

        Returns:
            List[Dict]: Daftar catatan pada tanggal itu.
        """
        query = (
            f"SELECT * FROM {cls.table_name} "
            "WHERE date(created_at) = ? ORDER BY created_at DESC"
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (date_str,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
