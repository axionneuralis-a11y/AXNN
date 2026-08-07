"""Model dasar yang diwarisi semua model lain (Blueprint 5.7)."""

import sqlite3
from typing import Dict, List, Optional

from utils.database import get_db_connection


class BaseModel:
    """Base CRUD generik untuk semua entitas AXNN."""

    table_name: str = ""  # WAJIB di-override oleh subclass

    @classmethod
    def insert(cls, data: Dict) -> int:
        """Insert satu baris baru.

        Args:
            data (Dict): Kolom -> nilai.

        Returns:
            int: ID baris baru.
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {cls.table_name} ({columns}) VALUES ({placeholders})"

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, list(data.values()))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @classmethod
    def get_all(cls, limit: Optional[int] = None) -> List[Dict]:
        """Ambil semua data terurut dari yang terbaru.

        Args:
            limit (Optional[int]): Batas jumlah baris.

        Returns:
            List[Dict]: Daftar baris.
        """
        query = f"SELECT * FROM {cls.table_name} ORDER BY id DESC"
        if limit is not None:
            query += " LIMIT ?"

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (limit,) if limit is not None else ())
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def get_by_id(cls, record_id: int) -> Optional[Dict]:
        """Ambil satu baris berdasarkan ID.

        Args:
            record_id (int): ID yang dicari.

        Returns:
            Optional[Dict]: Baris jika ditemukan, selain itu None.
        """
        query = f"SELECT * FROM {cls.table_name} WHERE id = ?"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (record_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @classmethod
    def update(cls, record_id: int, data: Dict) -> bool:
        """Update satu baris berdasarkan ID.

        Args:
            record_id (int): ID yang di-update.
            data (Dict): Kolom -> nilai baru.

        Returns:
            bool: True jika ada baris yang terdampak.
        """
        set_clause = ", ".join([f"{key} = ?" for key in data])
        query = f"UPDATE {cls.table_name} SET {set_clause} WHERE id = ?"

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, list(data.values()) + [record_id])
        conn.commit()
        affected = cursor.rowcount > 0
        conn.close()
        return affected

    @classmethod
    def delete(cls, record_id: int) -> bool:
        """Hapus satu baris berdasarkan ID.

        Args:
            record_id (int): ID yang dihapus.

        Returns:
            bool: True jika ada baris yang terhapus.
        """
        query = f"DELETE FROM {cls.table_name} WHERE id = ?"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (record_id,))
        conn.commit()
        affected = cursor.rowcount > 0
        conn.close()
        return affected
