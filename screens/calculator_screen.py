"""Layar kalkulator dasar + riwayat (F004)."""

from kivy.uix.screenmanager import Screen

from controllers.calculator_controller import CalculatorController


class CalculatorScreen(Screen):
    """Kalkulator +-×÷ dengan riwayat."""

    def __init__(self, **kwargs):
        """Siapkan controller & buffer input."""
        super().__init__(**kwargs)
        self.calc_ctrl = CalculatorController()
        self.current_input = ""

    def press_key(self, key: str) -> None:
        """Tambahkan karakter ke display.

        Args:
            key (str): Karakter tombol.
        """
        self.current_input += key
        self.ids.calc_display.text = self.current_input

    def clear(self) -> None:
        """Reset display."""
        self.current_input = ""
        self.ids.calc_display.text = "0"

    def calculate(self) -> None:
        """Hitung ekspresi saat ini."""
        if not self.current_input:
            return

        result = self.calc_ctrl.calculate(self.current_input)
        if result["success"]:
            self.ids.calc_display.text = result["data"]
            self.current_input = result["data"]
        else:
            self.ids.calc_display.text = "Error"
            self.current_input = ""
