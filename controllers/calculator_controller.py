"""Controller kalkulator dasar + riwayat (F004)."""

import re
from typing import Dict

from controllers.base_controller import BaseController
from models.calculator_model import CalculatorModel

ALLOWED_PATTERN: str = r"^[0-9+\-*/.() ]+$"
SAFE_GLOBALS: Dict = {"__builtins__": {}}


class CalculatorController(BaseController):
    """Logika operasi dasar +-×÷ dengan riwayat."""

    def __init__(self) -> None:
        """Ikatkan ke CalculatorModel."""
        super().__init__(CalculatorModel)

    def calculate(self, expression: str) -> Dict:
        """Hitung ekspresi dasar dengan aman.

        Args:
            expression (str): Ekspresi, mis. "2+3", "10÷2".

        Returns:
            Dict: Hasil operasi + nilai.
        """
        sanitized = expression.replace("×", "*").replace("÷", "/").strip()
        if not sanitized:
            return {"success": False, "error": "Ekspresi kosong"}
        if not re.match(ALLOWED_PATTERN, sanitized):
            return {"success": False, "error": "Input tidak valid"}

        try:
            result = eval(sanitized, SAFE_GLOBALS, {})  # noqa: S307 - sudah disanitasi
            result_str = str(result)
            self.create({"expression": expression, "result": result_str})
            return {"success": True, "data": result_str}
        except ZeroDivisionError:
            return {"success": False, "error": "Tidak bisa dibagi nol"}
        except Exception:  # noqa: BLE001
            return {"success": False, "error": "Format perhitungan salah"}

    def get_history(self, limit: int = 20) -> Dict:
        """Ambil riwayat perhitungan.

        Args:
            limit (int): Jumlah riwayat.

        Returns:
            Dict: Hasil operasi.
        """
        return self.get_all(limit) 
