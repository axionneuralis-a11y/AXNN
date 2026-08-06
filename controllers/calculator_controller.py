from controllers.base_controller import BaseController
from models.calculator_model import CalculatorModel
from utils.helpers import validate_calc_expression

class CalculatorController(BaseController):
    def __init__(self):
        super().__init__(CalculatorModel)
        
    def calculate_and_save(self, expression: str, result: str) -> dict:
        """F004: Menghitung dan menyimpan ke riwayat."""
        if not validate_calc_expression(expression):
            return {"success": False, "error": "Karakter tidak valid! Hanya angka dan +-×÷."}
            
        try:
            self.model.add_history(expression, result)
            return {"success": True, "data": {"expression": expression, "result": result}}
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def clear_history(self) -> dict:
        try:
            if self.model.clear_history():
                return {"success": True, "message": "Riwayat dihapus"}
            return {"success": False, "error": "Gagal menghapus riwayat"}
        except Exception as e:
            return {"success": False, "error": str(e)} 
