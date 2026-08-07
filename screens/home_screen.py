"""Layar Home / Dashboard (F001 + F002: 3 terbaru)."""

from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

from controllers.note_controller import NoteController
from controllers.todo_controller import TodoController


class HomeScreen(Screen):
    """Dashboard: 3 catatan & 3 tugas terbaru."""

    def __init__(self, **kwargs):
        """Siapkan controller."""
        super().__init__(**kwargs)
        self.note_ctrl = NoteController()
        self.todo_ctrl = TodoController()

    def on_enter(self, *args) -> None:
        """Muat data saat layar tampil."""
        Clock.schedule_once(self.load_dashboard_data, 0.1)

    def load_dashboard_data(self, dt: float) -> None:
        """Ambil & render data dashboard.

        Args:
            dt (float): Delta dari Clock.
        """
        notes_res = self.note_ctrl.get_recent_notes(3)
        if notes_res["success"]:
            self.render_notes(notes_res["data"])

        todos_res = self.todo_ctrl.get_recent_todos(3)
        if todos_res["success"]:
            self.render_todos(todos_res["data"])

    def render_notes(self, notes: list) -> None:
        """Render kartu catatan terbaru.

        Args:
            notes (list): Daftar catatan.
        """
        container = self.ids.recent_notes_container
        container.clear_widgets()
        for note in notes:
            card = self._build_card(note["title"], note["created_at"])
            container.add_widget(card)

    def render_todos(self, todos: list) -> None:
        """Render kartu tugas terbaru.

        Args:
            todos (list): Daftar tugas.
        """
        container = self.ids.recent_todos_container
        container.clear_widgets()
        for todo in todos:
            mark = "✅" if todo["is_done"] else "⬜"
            card = self._build_card(f"{mark} {todo['task']}", todo["created_at"])
            container.add_widget(card)

    def _build_card(self, title: str, subtitle: str) -> MDCard:
        """Buat kartu sederhana.

        Args:
            title (str): Judul.
            subtitle (str): Subjudul.

        Returns:
            MDCard: Kartu siap tampil.
        """
        card = MDCard(
            orientation="vertical", size_hint_y=None, height=dp(72),
            padding=dp(12), radius=[12],
        )
        card.add_widget(MDLabel(text=title, font_style="Subtitle1", bold=True))
        card.add_widget(MDLabel(text=subtitle, font_style="Caption"))
        return card
