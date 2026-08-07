"""Manajer tema resmi AXNN: Light, Dark, Green Matrix (Bible Bab 10)."""

from typing import Dict, Union


class ThemeManager:
    """Menyimpan palet 3 tema dan tema aktif."""

    THEMES: Dict[str, Dict[str, Union[str, bool]]] = {
        "light": {
            "background": "#FAFAFA",
            "text_primary": "#1A1A1A",
            "accent": "#2196F3",
            "card_bg": "#FFFFFF",
            "divider": "#E0E0E0",
            "glow": False,
        },
        "dark": {
            "background": "#121212",
            "text_primary": "#F5F5F5",
            "accent": "#64B5F6",
            "card_bg": "#1E1E1E",
            "divider": "#333333",
            "glow": False,
        },
        "matrix": {
            "background": "#000000",
            "text_primary": "#00FF41",
            "accent": "#39FF14",
            "card_bg": "#0A0A0A",
            "divider": "#003300",
            "glow": True,
        },
    }

    DEFAULT_THEME: str = "light"

    def __init__(self) -> None:
        """Set tema default ke light."""
        self.current_theme: str = self.DEFAULT_THEME

    def apply_theme(self, theme_name: str) -> bool:
        """Ganti tema aktif.

        Args:
            theme_name (str): Nama tema (light/dark/matrix).

        Returns:
            bool: True jika tema valid dan diterapkan.
        """
        if theme_name not in self.THEMES:
            return False
        self.current_theme = theme_name
        return True

    def get_style(self, key: str) -> Union[str, bool]:
        """Ambil satu nilai style dari tema aktif.

        Args:
            key (str): Kunci style (mis. 'background').

        Returns:
            Union[str, bool]: Nilai style.
        """
        return self.THEMES[self.current_theme].get(key, "#000000")
