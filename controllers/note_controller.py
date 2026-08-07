"""Controller catatan (F001)."""

from typing import Dict

from controllers.base_controller import BaseController
from models.note_model import NoteModel

MAX_TITLE_LENGTH: int = 200
MAX_CONTENT_LENGTH: int = 10000


class NoteController(BaseController):
    """Logika bisnis CRUD catatan."""

    def __init__(self) -> None:
        """Ikatkan ke NoteModel."""
        super().__init__(NoteModel)

    def create_note(self, title: str, content: str, folder_id: int = 1) -> Dict:
        """Buat catatan baru dengan validasi.

        Args:
            title (str): Judul catatan.
            content (str): Isi catatan.
            folder_id (int): Folder tujuan.

        Returns:
            Dict: Hasil operasi.
        """
        title = title.strip()
        if not title:
            return {"success": False, "error": "Judul tidak boleh kosong"}
        if len(title) > MAX_TITLE_LENGTH:
            return {
                "success": False,
                "error": f"Judul maksimal {MAX_TITLE_LENGTH} karakter",
            }
        if len(content) > MAX_CONTENT_LENGTH:
            return {
                "success": False,
                "error": f"Isi maksimal {MAX_CONTENT_LENGTH} karakter",
            }

        data = {"title": title, "content": content, "folder_id": folder_id}
        return self.create(data)

    def get_recent_notes(self, limit: int = 3) -> Dict:
        """Ambil catatan terbaru untuk Home.

        Args:
            limit (int): Jumlah catatan.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.get_recent(limit)
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}

    def get_notes_by_folder(self, folder_id: int) -> Dict:
        """Ambil catatan per folder (F003 filter).

        Args:
            folder_id (int): ID folder.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.get_by_folder(folder_id)
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}
