"""Calculator Screen — Kalkulator dasar +-×÷ (F004)."""
import logging

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty

from controllers.calculator_controller import CalculatorController

logger = logging.getLogger(__name__)


class CalculatorScreen(Screen):
    """Layar kalkulator dengan riwayat."""

    display = StringProperty('0')
    history = ListProperty([])

    def on_pre_enter(self, *args) -> None:
        calc_ctrl = CalculatorController()
        result = calc_ctrl.get_history()
        if result['success']:
            self.history = result['data']

    def open_editor(self) -> None:
        self.manager.current = 'editor' 
