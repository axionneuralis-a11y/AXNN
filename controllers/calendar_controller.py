"""Controller kalender: agregasi notes & todos per tanggal (F005)."""

from typing import Dict, List

from models.note_model import NoteModel
from models.todo_model import TodoModel


class CalendarController:
    """Menyediakan data indikator titik & detail tanggal."""

    def __init__(self) -> None:
        """Siapkan model notes & todos."""
        self.note_model = NoteModel
        self.todo_model = TodoModel

    def get_events_by_date(self, date_str: str) -> Dict:
        """Ambil semua notes & todos pada tanggal tertentu.

        Args:
            date_str (str): Tanggal format YYYY-MM-DD.

        Returns:
            Dict: {"success": bool, "data": {"notes": [...], "todos": [...]}}
        """
        try:
            notes: List[Dict] = self.note_model.get_by_date(date_str)
            todos: List[Dict] = self.todo_model.get_by_date(date_str)
            return {"success": True, "data": {"notes": notes, "todos": todos}}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}

    def has_events(self, date_str: str) -> bool:
        """Cek apakah ada notes/todos pada tanggal tertentu (indikator titik).

        Args:
            date_str (str): Tanggal format YYYY-MM-DD.

        Returns:
            bool: True jika ada event.
        """
        result = self.get_events_by_date(date_str)
        if not result["success"]:
            return False
        data = result["data"]
        return bool(data["notes"] or data["todos"])
