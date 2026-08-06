"""Bottom Navigation AXNN dengan 6 menu (URUTAN WAJIB — Hukum No.4)."""
import logging

from kivymd.uix.bottomnavigation import MDBottomNavigationBar, MDBottomNavigationItem
from kivy.uix.screenmanager import ScreenManager

logger = logging.getLogger(__name__)

# URUTAN WAJIB — DILARANG MENGUBAH (Hukum Proyek No.4)
NAV_ORDER = [
    ('home', 'Home', 'home'),
    ('notes', 'Notes', 'note'),
    ('list', 'List', 'format-list-checks'),
    ('calc', 'Calc', 'calculator'),
    ('calendar', 'Calendar', 'calendar-month'),
    ('settings', 'Settings', 'cog'),
]


class AXNNBottomNav(MDBottomNavigationBar):
    """Bottom nav utama AXNN, terhubung dengan ScreenManager."""

    def __init__(self, screen_manager: ScreenManager, **kwargs) -> None:
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self._build_items()

    def _build_items(self) -> None:
        """Bangun 6 item navigasi sesuai urutan wajib."""
        for name, label, icon in NAV_ORDER:
            item = MDBottomNavigationItem(
                name=name,
                text=label,
                icon=icon,
                on_tab_press=lambda x, n=name: self._on_tab_select(n),
            )
            self.add_widget(item)

    def _on_tab_select(self, screen_name: str) -> None:
        """Pindah screen saat tab ditekan.

        Args:
            screen_name: Nama target screen di ScreenManager.
        """
        self.screen_manager.current = screen_name
        self.screen_manager.transition.direction = 'left'
        logger.info("Navigasi ke: %s", screen_name) 
