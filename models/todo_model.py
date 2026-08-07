"""Model daftar tugas (tabel todos)."""

from typing import Dict, List

from models.base_model import BaseModel
from utils.database import get_db_connection


class TodoModel(BaseModel):
    """Akses data tugas."""

    table_name: str = "todos"

    @classmethod
    def get_recent(cls, limit: int = 3) -> List[Dict]:
        """Ambil tugas terbaru untuk Home.

        Args:
            limit (int): Jumlah tugas.

        Returns:
            List[Dict]: Daftar tugas terbaru.
        """
        query = (
            f"SELECT id, task, is_done, created_at FROM {cls.table_name} "
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
        """Ambil tugas dalam folder tertentu.

        Args:
            folder_id (int): ID folder.

        Returns:
            List[Dict]: Daftar tugas dalam folder.
        """
        query = (
            f"SELECT * FROM {cls.table_name} WHERE folder_id = ? "
            "ORDER BY created_at DESC"
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (folder_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def get_by_date(cls, date_str: str) -> List[Dict]:
        """Ambil tugas dengan due_date pada tanggal tertentu (Kalender).

        Args:
            date_str (str): Tanggal format YYYY-MM-DD.

        Returns:
            List[Dict]: Daftar tugas pada tanggal itu.
        """
        query = (
            f"SELECT * FROM {cls.table_name} "
            "WHERE date(due_date) = ? ORDER BY created_at DESC"
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (date_str,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def toggle_status(cls, todo_id: int) -> bool:
        """Balik status selesai/belum selesai.

        Args:
            todo_id (int): ID tugas.

        Returns:
            bool: True jika berhasil.
        """
        query = (
            f"UPDATE {cls.table_name} SET is_done = 1 - is_done WHERE id = ?"
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (todo_id,))
        conn.commit()
        affected = cursor.rowcount > 0
        conn.close()
        return affected
