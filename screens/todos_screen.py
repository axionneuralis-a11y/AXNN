"""Layar daftar tugas + checklist (F002 + F003)."""

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

from controllers.todo_controller import TodoController


class TodosScreen(Screen):
    """Daftar semua tugas dengan toggle selesai."""

    def __init__(self, **kwargs):
        """Siapkan controller."""
        super().__init__(**kwargs)
        self.todo_ctrl = TodoController()

    def on_enter(self, *args) -> None:
        """Muat daftar tugas."""
        Clock.schedule_once(self.refresh_list, 0.1)

    def refresh_list(self, dt=None) -> None:
        """Render daftar tugas.

        Args:
            dt: Delta dari Clock (opsional).
        """
        container = self.ids.todos_container
        container.clear_widgets()

        result = self.todo_ctrl.get_all()
        if not result["success"]:
            return

        for todo in result["data"]:
            mark = "✅" if todo["is_done"] else "⬜"
            item = OneLineListItem(text=f"{mark} {todo['task']}")
            item.bind(
                on_release=lambda x, t_id=todo["id"]: self.toggle_and_refresh(t_id)
            )
            container.add_widget(item)

    def toggle_and_refresh(self, todo_id: int) -> None:
        """Toggle status lalu render ulang.

        Args:
            todo_id (int): ID tugas.
        """
        self.todo_ctrl.toggle_todo(todo_id)
        self.refresh_list()
