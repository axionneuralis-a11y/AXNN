"""Model riwayat kalkulator (tabel calc_history)."""

from models.base_model import BaseModel


class CalculatorModel(BaseModel):
    """Akses riwayat perhitungan."""

    table_name: str = "calc_history"
