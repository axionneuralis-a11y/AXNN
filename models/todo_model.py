from models.base_model import BaseModel
from typing import List, Dict, Any
from utils.database import get_db_connection

class TodoModel(BaseModel):
    table_name = 'todos'

    @classmethod
    def get_recent(cls, limit: int = 3) -> List[Dict[str, Any]]:
        """F002: Ambil todo terbaru untuk Home Screen."""
        query = f"SELECT * FROM {cls.table_name} ORDER BY updated_at DESC LIMIT ?"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (limit,))
            return [dict(row) for row in cursor.fetchall()]
        finally:
            conn.close()
            
    @classmethod
    def toggle_done(cls, todo_id: int, is_done: int) -> bool:
        """F002: Tandai todo selesai atau belum."""
        return cls.update(todo_id, {"is_done": is_done}) 
