"""Controller daftar tugas (F002)."""

from typing import Dict

from controllers.base_controller import BaseController
from models.todo_model import TodoModel

MAX_TASK_LENGTH: int = 255


class TodoController(BaseController):
    """Logika bisnis CRUD tugas."""

    def __init__(self) -> None:
        """Ikatkan ke TodoModel."""
        super().__init__(TodoModel)

    def create_todo(self, task: str, folder_id: int = 1) -> Dict:
        """Buat tugas baru dengan validasi.

        Args:
            task (str): Isi tugas.
            folder_id (int): Folder tujuan.

        Returns:
            Dict: Hasil operasi.
        """
        task = task.strip()
        if not task:
            return {"success": False, "error": "Tugas tidak boleh kosong"}
        if len(task) > MAX_TASK_LENGTH:
            return {
                "success": False,
                "error": f"Tugas maksimal {MAX_TASK_LENGTH} karakter",
            }

        data = {"task": task, "folder_id": folder_id, "is_done": 0}
        return self.create(data)

    def toggle_todo(self, todo_id: int) -> Dict:
        """Tandai selesai/belum selesai.

        Args:
            todo_id (int): ID tugas.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.toggle_status(todo_id)
            return {"success": result, "data": todo_id}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}

    def get_recent_todos(self, limit: int = 3) -> Dict:
        """Ambil tugas terbaru untuk Home.

        Args:
            limit (int): Jumlah tugas.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.get_recent(limit)
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}
