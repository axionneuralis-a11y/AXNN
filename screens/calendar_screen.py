"""Calendar Screen — Kalender bulanan + indikator titik (F005)."""
import logging

from kivy.uix.screenmanager import Screen

logger = logging.getLogger(__name__)


class CalendarScreen(Screen):
    """Layar kalender bulanan dengan indikator catatan/todo."""

    def open_editor(self) -> None:
        self.manager.current = 'editor' 
