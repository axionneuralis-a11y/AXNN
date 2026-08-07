"""Titik masuk aplikasi AXNN v1.1.0 (M2 build)."""

import os

os.environ["KIVY_NO_FILELOG"] = "1"

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from utils.database import init_db
from controllers.theme_controller import ThemeController

from screens.home_screen import HomeScreen
from screens.notes_screen import NotesScreen
from screens.todos_screen import TodosScreen
from screens.calculator_screen import CalculatorScreen
from screens.calendar_screen import CalendarScreen
from screens.settings_screen import SettingsScreen
from screens.note_detail_screen import NoteDetailScreen
from screens.todo_detail_screen import TodoDetailScreen
from screens.editor_screen import EditorScreen

KV_FILES = [
    "kv_files/home_screen.kv",
    "kv_files/notes_screen.kv",
    "kv_files/todos_screen.kv",
    "kv_files/calculator_screen.kv",
    "kv_files/calendar_screen.kv",
    "kv_files/settings_screen.kv",
    "kv_files/note_detail_screen.kv",
    "kv_files/todo_detail_screen.kv",
    "kv_files/editor_screen.kv",
]


class AXNNApp(App):
    """Aplikasi utama AXNN."""

    title = "AXNN"

    def __init__(self, **kwargs):
        """Siapkan controller tema."""
        super().__init__(**kwargs)
        self.theme_ctrl = ThemeController()

    def build(self):
        """Bangun UI: init DB, tema, semua screen."""
        init_db()
        self.theme_ctrl.load_saved_theme()

        for kv in KV_FILES:
            Builder.load_file(kv)

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(NotesScreen(name="notes"))
        sm.add_widget(TodosScreen(name="todos"))
        sm.add_widget(CalculatorScreen(name="calculator"))
        sm.add_widget(CalendarScreen(name="calendar"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.add_widget(NoteDetailScreen(name="note_detail"))
        sm.add_widget(TodoDetailScreen(name="todo_detail"))
        sm.add_widget(EditorScreen(name="editor"))
        return sm

    def go_to_editor(self) -> None:
        """Navigasi ke editor (tombol >_)."""
        self.root.current = "editor"

    def go_back(self) -> None:
        """Kembali ke layar sebelumnya."""
        self.root.current = "home"

    def show_add_note(self) -> None:
        """Placeholder dialog tambah catatan (diperluas di M3)."""

    def show_add_todo(self) -> None:
        """Placeholder dialog tambah tugas (diperluas di M3)."""

    def save_editor(self) -> None:
        """Placeholder save editor (diperluas di M6)."""


if __name__ == "__main__":
    AXNNApp().run()
