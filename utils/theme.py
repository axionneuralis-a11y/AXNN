"""Manajemen tema aplikasi AXNN.

Palet warna WAJIB mengikuti Bab 10 Design System.
DILARANG menambah warna di luar palet resmi tanpa persetujuan Azriel.
"""
import logging
from typing import Dict, Union

from kivy.utils import get_color_from_hex
from kivy.graphics import Color

logger = logging.getLogger(__name__)


class ThemeManager:
    """Pengelola 3 tema resmi AXNN: light, dark, matrix."""

    THEMES: Dict[str, Dict[str, Union[str, bool]]] = {
        'light': {
            'background': '#FAFAFA',
            'text_primary': '#1A1A1A',
            'accent': '#2196F3',
            'card_bg': '#FFFFFF',
            'divider': '#E0E0E0',
            'glow': False,
        },
        'dark': {
            'background': '#121212',
            'text_primary': '#F5F5F5',
            'accent': '#64B5F6',
            'card_bg': '#1E1E1E',
            'divider': '#333333',
            'glow': False,
        },
        'matrix': {
            'background': '#000000',
            'text_primary': '#00FF41',
            'accent': '#39FF14',
            'card_bg': '#0A0A0A',
            'divider': '#003300',
            'glow': True,
        },
    }

    VALID_THEMES = ('light', 'dark', 'matrix')

    def __init__(self) -> None:
        self.current_theme: str = 'light'

    def apply_theme(self, theme_name: str) -> bool:
        """Terapkan tema ke seluruh aplikasi.

        Args:
            theme_name: Nama tema ('light', 'dark', 'matrix').

        Returns:
            bool: True jika tema valid dan diterapkan.
        """
        if theme_name not in self.VALID_THEMES:
            logger.warning("Tema '%s' tidak valid, fallback ke light", theme_name)
            theme_name = 'light'

        self.current_theme = theme_name
        logger.info("Tema diterapkan: %s", theme_name)
        return True

    def get_style(self, key: str) -> Union[str, bool]:
        """Ambil nilai style berdasarkan tema aktif.

        Args:
            key: Kunci style (background, text_primary, accent, dll).

        Returns:
            Nilai style sesuai tema aktif.
        """
        return self.THEMES[self.current_theme].get(key, '#000000')

    def get_color(self, key: str) -> Color:
        """Ambil warna Kivy dari kunci style.

        Args:
            key: Kunci style berupa hex color.

        Returns:
            Color: Objek warna Kivy siap pakai.
        """
        hex_value = str(self.get_style(key))
        return get_color_from_hex(hex_value)

    def is_glow(self) -> bool:
        """Cek apakah tema aktif memiliki efek glow (Matrix)."""
        return bool(self.get_style('glow')) 
