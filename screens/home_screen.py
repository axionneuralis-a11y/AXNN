"""Home Screen — Dashboard dengan 3 catatan & 3 todo terbaru (F001/F002)."""
import logging

from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

from controllers.note_controller import NoteController
from controllers.todo_controller import TodoController

logger = logging.getLogger(__name__)


class HomeScreen(Screen):
    """Dashboard utama AXNN."""

    recent_notes = ListProperty([])
    recent_todos = ListProperty([])

    def on_pre_enter(self, *args) -> None:
        """Muat data terbaru saat screen akan tampil (via Controller)."""
        note_ctrl = NoteController()
        todo_ctrl = TodoController()

        note_res = note_ctrl.get_recent_notes(limit=3)
        if note_res['success']:
            self.recent_notes = note_res['data']

        todo_res = todo_ctrl.get_recent_todos(limit=3)
        if todo_res['success']:
            self.recent_todos = todo_res['data']

    def open_editor(self) -> None:
        """Tombol >_ — buka Editor Kode (fitur N007/N008)."""
        self.manager.current = 'editor' 
