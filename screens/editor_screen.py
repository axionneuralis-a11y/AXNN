"""Layar editor dasar (target M2: buka & bisa ketik)."""

from kivy.uix.screenmanager import Screen


class EditorScreen(Screen):
    """Screen editor kode sederhana."""

    def clear_editor(self) -> None:
        """Kosongkan area editor."""
        self.ids.code_input.text = ""
