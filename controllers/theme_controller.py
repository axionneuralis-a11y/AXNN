"""Controller pengaturan tema + simpan ke tabel settings."""

from typing import Dict

from controllers.base_controller import BaseController
from models.setting_model import SettingModel
from utils.theme import ThemeManager


class ThemeController(BaseController):
    """Mengelola tema aktif dan persistensinya."""

    THEME_KEY: str = "app_theme"

    def __init__(self) -> None:
        """Siapkan ThemeManager dan model settings."""
        super().__init__(SettingModel)
        self.theme_manager = ThemeManager()

    def load_saved_theme(self) -> Dict:
        """Muat tema tersimpan dari DB, fallback ke default.

        Returns:
            Dict: Hasil operasi + nama tema aktif.
        """
        try:
            value = self.model.get_value(self.THEME_KEY)
            theme_name = value or ThemeManager.DEFAULT_THEME
            self.theme_manager.apply_theme(theme_name)
            return {"success": True, "data": self.theme_manager.current_theme}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}

    def set_theme(self, theme_name: str) -> Dict:
        """Ganti tema dan simpan ke DB.

        Args:
            theme_name (str): Nama tema baru.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            if not self.theme_manager.apply_theme(theme_name):
                return {"success": False, "error": "Tema tidak dikenal"}
            self.model.set_value(self.THEME_KEY, theme_name)
            return {"success": True, "data": theme_name}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}
