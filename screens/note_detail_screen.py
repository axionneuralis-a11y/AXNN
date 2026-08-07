"""Layar detail catatan (F001 + F012 fullscreen dasar)."""

from kivy.uix.screenmanager import Screen

from controllers.note_controller import NoteController


class NoteDetailScreen(Screen):
    """Detail satu catatan."""

    def __init__(self, **kwargs):
        """Siapkan controller & state."""
        super().__init__(**kwargs)
        self.note_ctrl = NoteController()
        self.current_note_id = None

    def load_note(self, note_id: int) -> None:
        """Muat data catatan ke tampilan.

        Args:
            note_id (int): ID catatan.
        """
        self.current_note_id = note_id
        result = self.note_ctrl.get_by_id(note_id)
        if result["success"] and result["data"]:
            note = result["data"]
            self.ids.note_title.text = note["title"]
            self.ids.note_content.text = note["content"] 
