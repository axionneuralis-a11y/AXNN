from typing import Dict
from models.todo_model import TodoModel
from controllers.base_controller import BaseController

class TodoController(BaseController):
    def __init__(self):
        super().__init__(TodoModel)

    def create_todo(self, task: str, folder_id: int = 1) -> Dict:
        """Membuat tugas baru dengan validasi."""
        if not task.strip():
            return {"success": False, "error": "Tugas tidak boleh kosong!"}
        if len(task) > 255:
            return {"success": False, "error": "Tugas maksimal 255 karakter!"}
            
        data = {"task": task.strip(), "folder_id": folder_id, "is_done": 0}
        return self.create(data)

    def toggle_todo(self, todo_id: int, current_status: int) -> Dict:
        """Menandai tugas selesai/belum."""
        try:
            self.model.toggle_status(todo_id, current_status)
            return {"success": True, "message": "Status tugas diperbarui"}
        except Exception as e:
            return {"success": False, "error": str(e)} 
