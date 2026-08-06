from models.base_model import BaseModel
from typing import Any
from utils.database import get_db_connection
import logging

logger = logging.getLogger(__name__)

class SettingModel(BaseModel):
    table_name = 'settings'
    
    # Override metode standar karena Primary Key-nya adalah 'key', bukan 'id'
    @classmethod
    def set_value(cls, key: str, value: Any) -> bool:
        """Menyimpan atau memperbarui pengaturan (Upsert SQLite)."""
        query = """
            INSERT INTO settings (key, value) VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value = excluded.value
        """
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (key, str(value)))
            conn.commit()
            return True
        except Exception as e:
            logger.error(f"Error setting value: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def get_value(cls, key: str, default: Any = None) -> Any:
        """Mengambil nilai pengaturan berdasarkan key."""
        query = "SELECT value FROM settings WHERE key = ?"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (key,))
            row = cursor.fetchone()
            return row['value'] if row else default
        finally:
            conn.close() 
