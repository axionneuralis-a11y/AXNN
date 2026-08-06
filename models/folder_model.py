from models.base_model import BaseModel
from typing import Dict, Any, Optional
from utils.database import get_db_connection

class FolderModel(BaseModel):
    table_name = 'folders'

    @classmethod
    def get_default_folder(cls) -> Optional[Dict[str, Any]]:
        """F003: Dapatkan folder default sistem."""
        query = f"SELECT * FROM {cls.table_name} WHERE is_default = 1 LIMIT 1"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            return dict(row) if row else None
        finally:
            conn.close() 
