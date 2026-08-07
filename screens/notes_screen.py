"""Layar daftar catatan + filter folder (F001 + F003)."""

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

from controllers.folder_controller import FolderController
from controllers.note_controller import NoteController


class NotesScreen(Screen):
    """Daftar semua catatan dengan filter folder."""

    def __init__(self, **kwargs):
        """Siapkan controller."""
        super().__init__(**kwargs)
        self.note_ctrl = NoteController()
        self.folder_ctrl = FolderController()
        self.current_folder_id = 1

    def on_enter(self, *args) -> None:
        """Muat daftar catatan."""
        Clock.schedule_once(self.refresh_list, 0.1)

    def refresh_list(self, dt=None) -> None:
        """Render daftar catatan sesuai folder aktif.

        Args:
            dt: Delta dari Clock (opsional).
        """
        container = self.ids.notes_container
        container.clear_widgets()

        result = self.note_ctrl.get_notes_by_folder(self.current_folder_id)
        if not result["success"]:
            return

        for note in result["data"]:
            item = OneLineListItem(text=note["title"])
            item.bind(on_release=lambda x, n_id=note["id"]: self.open_detail(n_id))
            container.add_widget(item)

    def open_detail(self, note_id: int) -> None:
        """Buka detail catatan.

        Args:
            note_id (int): ID catatan.
        """
        detail = self.manager.get_screen("note_detail")
        detail.load_note(note_id)
        self.manager.current = "note_detail"
