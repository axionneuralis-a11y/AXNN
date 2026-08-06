"""Settings Screen — Tema, statistik, feedback (F010/F013/F014)."""
import logging

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from controllers.theme_controller import ThemeController
from controllers.stats_controller import StatsController

logger = logging.getLogger(__name__)


class SettingsScreen(Screen):
    """Layar pengaturan aplikasi."""

    current_theme = StringProperty('light')

    def on_pre_enter(self, *args) -> None:
        theme_ctrl = ThemeController()
        self.current_theme = theme_ctrl.get_current_theme()

    def change_theme(self, theme_name: str) -> None:
        """Ganti tema via Controller (tersimpan otomatis)."""
        theme_ctrl = ThemeController()
        result = theme_ctrl.switch_theme(theme_name)
        if result['success']:
            self.current_theme = theme_name

    def open_editor(self) -> None:
        self.manager.current = 'editor' 
