"""Todos Screen (List) — Daftar tugas + checklist (F002)."""
import logging

from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

from controllers.todo_controller import TodoController

logger = logging.getLogger(__name__)


class TodosScreen(Screen):
    """Layar daftar semua tugas."""

    todos = ListProperty([])

    def on_pre_enter(self, *args) -> None:
        todo_ctrl = TodoController()
        result = todo_ctrl.get_all()
        if result['success']:
            self.todos = result['data']

    def toggle_todo(self, todo_id: int, is_done: int) -> None:
        """Tandai selesai/belum via Controller."""
        todo_ctrl = TodoController()
        todo_ctrl.toggle_todo_status(todo_id, is_done)

    def open_editor(self) -> None:
        self.manager.current = 'editor' 
