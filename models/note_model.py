from models.base_model import BaseModel
from typing import List, Dict, Any
from utils.database import get_db_connection

class NoteModel(BaseModel):
    table_name = 'notes'

    @classmethod
    def get_recent(cls, limit: int = 3) -> List[Dict[str, Any]]:
        """F001: Ambil catatan terbaru untuk ditampilkan di Home Screen."""
        query = f"SELECT * FROM {cls.table_name} ORDER BY updated_at DESC LIMIT ?"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (limit,))
            return [dict(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    @classmethod
    def get_by_folder(cls, folder_id: int) -> List[Dict[str, Any]]:
        """F003: Filter catatan berdasarkan folder."""
        query = f"SELECT * FROM {cls.table_name} WHERE folder_id = ? ORDER BY updated_at DESC"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (folder_id,))
            return [dict(row) for row in cursor.fetchall()]
        finally:
            conn.close() 
