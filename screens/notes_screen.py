"""Notes Screen — Daftar catatan + filter folder (F001/F003)."""
import logging

from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

from controllers.note_controller import NoteController

logger = logging.getLogger(__name__)


class NotesScreen(Screen):
    """Layar daftar semua catatan."""

    notes = ListProperty([])

    def on_pre_enter(self, *args) -> None:
        note_ctrl = NoteController()
        result = note_ctrl.get_all()
        if result['success']:
            self.notes = result['data']

    def open_editor(self) -> None:
        self.manager.current = 'editor' 
