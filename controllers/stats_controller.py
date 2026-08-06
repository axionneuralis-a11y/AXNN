from models.note_model import NoteModel
from models.todo_model import TodoModel
from models.folder_model import FolderModel
from utils.database import DB_PATH
import os
import logging

logger = logging.getLogger(__name__)

class StatsController:
    def get_app_statistics(self) -> dict:
        """F013: Mengambil statistik aplikasi untuk layar Pengaturan."""
        try:
            notes_count = len(NoteModel.get_all())
            todos_count = len(TodoModel.get_all())
            folders_count = len(FolderModel.get_all())
            
            db_size_kb = 0
            if os.path.exists(DB_PATH):
                db_size_kb = os.path.getsize(DB_PATH) // 1024
                
            return {
                "success": True, 
                "data": {
                    "total_notes": notes_count,
                    "total_todos": todos_count,
                    "total_folders": folders_count,
                    "db_size_kb": db_size_kb
                }
            }
        except Exception as e:
            logger.error(f"Error stats: {e}")
            return {"success": False, "error": str(e)} 
