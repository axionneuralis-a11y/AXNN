"""Model folder (tabel folders)."""

from typing import Dict, List, Optional

from models.base_model import BaseModel
from utils.database import get_db_connection


class FolderModel(BaseModel):
    """Akses data folder."""

    table_name: str = "folders"

    @classmethod
    def get_by_name(cls, name: str) -> Optional[Dict]:
        """Cari folder berdasarkan nama.

        Args:
            name (str): Nama folder.

        Returns:
            Optional[Dict]: Folder jika ditemukan.
        """
        query = f"SELECT * FROM {cls.table_name} WHERE name = ?"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @classmethod
    def get_all_folders(cls) -> List[Dict]:
        """Ambil semua folder terurut.

        Returns:
            List[Dict]: Daftar folder.
        """
        query = f"SELECT * FROM {cls.table_name} ORDER BY is_default DESC, name ASC"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
