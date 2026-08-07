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
from typing import List, Dict
from models.base_model import BaseModel
from utils.database import get_db_connection

class TodoModel(BaseModel):
    table_name = 'todos'

    @classmethod
    def get_recent(cls, limit: int = 3) -> List[Dict]:
        """Mengambil tugas terbaru untuk Home Screen."""
        query = f"SELECT id, task, is_done FROM {cls.table_name} ORDER BY created_at DESC LIMIT ?"
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, (limit,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def toggle_status(cls, todo_id: int, current_status: int) -> bool:
        """Toggle status selesai/belum selesai."""
        new_status = 0 if current_status == 1 else 1
        query = f"UPDATE {cls.table_name} SET is_done = ? WHERE id = ?"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (new_status, todo_id))
        conn.commit()
        conn.close()
        return True
