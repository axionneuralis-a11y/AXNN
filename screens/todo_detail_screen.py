"""Layar detail tugas (F002)."""

from kivy.uix.screenmanager import Screen

from controllers.todo_controller import TodoController


class TodoDetailScreen(Screen):
    """Detail satu tugas."""

    def __init__(self, **kwargs):
        """Siapkan controller & state."""
        super().__init__(**kwargs)
        self.todo_ctrl = TodoController()
        self.current_todo_id = None

    def load_todo(self, todo_id: int) -> None:
        """Muat data tugas ke tampilan.

        Args:
            todo_id (int): ID tugas.
        """
        self.current_todo_id = todo_id
        result = self.todo_ctrl.get_by_id(todo_id)
        if result["success"] and result["data"]:
            self.ids.todo_task.text = result["data"]["task"] 
