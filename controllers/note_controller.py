# controllers/note_controller.py
from controllers.base_controller import BaseController
from models.note_model import NoteModel

class NoteController(BaseController):
    def __init__(self):
        super().__init__(NoteModel)
        
    def get_recent_notes(self, limit: int = 3):
        try: return {"success": True, "data": self.model.get_recent(limit)}
        except Exception as e: return {"success": False, "error": str(e)}

# controllers/todo_controller.py
from controllers.base_controller import BaseController
from models.todo_model import TodoModel

class TodoController(BaseController):
    def __init__(self):
        super().__init__(TodoModel)
        
    def toggle_todo_status(self, todo_id: int, is_done: int):
        try:
            if self.model.toggle_done(todo_id, is_done):
                return {"success": True, "data": {"id": todo_id, "is_done": is_done}}
            return {"success": False, "error": "Gagal update status"}
        except Exception as e: return {"success": False, "error": str(e)}

# controllers/folder_controller.py
from controllers.base_controller import BaseController
from models.folder_model import FolderModel

class FolderController(BaseController):
    def __init__(self):
        super().__init__(FolderModel)
        
    def get_default_folder(self):
        try:
            result = self.model.get_default_folder()
            if result: return {"success": True, "data": result}
            return {"success": False, "error": "Folder default tidak ditemukan"}
        except Exception as e: return {"success": False, "error": str(e)} 
