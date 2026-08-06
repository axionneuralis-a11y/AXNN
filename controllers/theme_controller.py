"""Controller tema — menghubungkan ThemeManager dengan SettingsModel."""
import logging
from typing import Dict, Any

from utils.theme import ThemeManager
from controllers.settings_controller import SettingsController

logger = logging.getLogger(__name__)


class ThemeController:
    """Mengelola pergantian tema dan persistensi otomatis."""

    def __init__(self) -> None:
        self.theme_manager = ThemeManager()
        self.settings_ctrl = SettingsController()

    def load_saved_theme(self) -> Dict[str, Any]:
        """Muat tema tersimpan saat aplikasi dibuka.

        Returns:
            dict: {'success': bool, 'data': {'theme': str}}
        """
        result = self.settings_ctrl.get_theme()
        if result['success']:
            theme_name = result['data']['theme']
            self.theme_manager.apply_theme(theme_name)
            return {"success": True, "data": {"theme": theme_name}}

        # Fallback default jika gagal baca
        self.theme_manager.apply_theme('light')
        return {"success": True, "data": {"theme": 'light'}}

    def switch_theme(self, theme_name: str) -> Dict[str, Any]:
        """Ganti tema + simpan otomatis ke pengaturan.

        Args:
            theme_name: Nama tema tujuan.

        Returns:
            dict: Hasil operasi sesuai standar error handling Bab 2.7.
        """
        save_result = self.settings_ctrl.set_theme(theme_name)
        if not save_result['success']:
            return save_result

        self.theme_manager.apply_theme(theme_name)
        logger.info("Tema diganti ke: %s", theme_name)
        return {"success": True, "data": {"theme": theme_name}}

    def get_current_theme(self) -> str:
        """Ambil nama tema yang sedang aktif."""
        return self.theme_manager.current_theme
