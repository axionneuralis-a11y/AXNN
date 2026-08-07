"""Bottom navigation resmi AXNN (F011).

URUTAN WAJIB (Hukum No.4): Home → Notes → List → Calc → Calendar → Settings
"""

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem


class BottomNavManager(BoxLayout):
    """Membangun bottom nav 6 menu dengan urutan terkunci."""

    NAV_ITEMS = [
        ("home", "home", "Home"),
        ("notes", "note-text-outline", "Notes"),
        ("todos", "format-list-checks", "List"),
        ("calculator", "calculator-variant", "Calc"),
        ("calendar", "calendar-month", "Calendar"),
        ("settings", "cog-outline", "Settings"),
    ]

    def __init__(self, screen_manager, **kwargs):
        """Buat bottom nav terikat ke ScreenManager.

        Args:
            screen_manager: ScreenManager utama aplikasi.
        """
        super().__init__(orientation="vertical", **kwargs)
        self.screen_manager = screen_manager

        self.bottom_nav = MDBottomNavigation()
        for name, icon, label in self.NAV_ITEMS:
            item = MDBottomNavigationItem(
                name=name, text=label, icon=icon,
                on_release=lambda x, n=name: self.switch(n),
            )
            self.bottom_nav.add_widget(item)

        self.add_widget(self.bottom_nav)

    def switch(self, screen_name: str) -> None:
        """Pindah layar sesuai nama menu.

        Args:
            screen_name (str): Nama screen tujuan.
        """
        self.screen_manager.current = screen_name
