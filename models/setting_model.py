"""Model key-value untuk pengaturan aplikasi."""

from typing import Optional

from models.base_model import BaseModel
from utils.database import get_db_connection


class SettingModel(BaseModel):
    """Akses tabel settings (key, value)."""

    table_name: str = "settings"

    @classmethod
    def get_value(cls, key: str) -> Optional[str]:
        """Ambil nilai pengaturan berdasarkan key.

        Args:
            key (str): Kunci pengaturan.

        Returns:
            Optional[str]: Nilai jika ada, selain itu None.
        """
        query = f"SELECT value FROM {cls.table_name} WHERE key = ?"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (key,))
        row = cursor.fetchone()
        conn.close()
        return row["value"] if row else None

    @classmethod
    def set_value(cls, key: str, value: str) -> None:
        """Simpan/ubah nilai pengaturan (upsert).

        Args:
            key (str): Kunci pengaturan.
            value (str): Nilai baru.
        """
        query = (
            f"INSERT INTO {cls.table_name} (key, value) VALUES (?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value"
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (key, value))
        conn.commit()
        conn.close()
