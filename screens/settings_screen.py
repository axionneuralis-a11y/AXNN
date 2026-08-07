"""Layar pengaturan: switch tema (F010 dasar M2)."""

from kivy.uix.screenmanager import Screen

from controllers.theme_controller import ThemeController


class SettingsScreen(Screen):
    """Pengaturan tema aplikasi."""

    def __init__(self, **kwargs):
        """Siapkan controller tema."""
        super().__init__(**kwargs)
        self.theme_ctrl = ThemeController()

    def set_theme(self, theme_name: str) -> None:
        """Ganti tema dan simpan.

        Args:
            theme_name (str): light/dark/matrix.
        """
        self.theme_ctrl.set_theme(theme_name)
