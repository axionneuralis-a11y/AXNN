from utils.database import get_db_connection
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class NotificationModel:
    """Model khusus untuk mengambil data reminder dari notes & todos (F006)."""
    
    @classmethod
    def get_upcoming_reminders(cls) -> List[Dict[str, Any]]:
        """Mengambil catatan & tugas yang memiliki reminder aktif."""
        query = """
            SELECT 'note' as type, id, title as name, reminder_at as time FROM notes WHERE reminder_at IS NOT NULL
            UNION ALL
            SELECT 'todo' as type, id, task as name, due_date as time FROM todos WHERE due_date IS NOT NULL
            ORDER BY time ASC
        """
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Error get reminders: {e}")
            return []
        finally:
            conn.close() 
