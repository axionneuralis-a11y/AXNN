from models.base_model import BaseModel
from typing import List, Dict, Any
from utils.database import get_db_connection
import logging

logger = logging.getLogger(__name__)

class CalculatorModel(BaseModel):
    table_name = 'calc_history'

    @classmethod
    def add_history(cls, expression: str, result: str) -> int:
        """Menyimpan riwayat perhitungan baru."""
        return cls.insert({"expression": expression, "result": result})

    @classmethod
    def clear_history(cls) -> bool:
        """Menghapus semua riwayat kalkulator (F004)."""
        query = f"DELETE FROM {cls.table_name}"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True
        except Exception as e:
            logger.error(f"Error clear history: {e}")
            return False
        finally:
            conn.close() 
from typing import List, Dict
from models.base_model import BaseModel

class CalculatorModel(BaseModel):
    table_name = 'calc_history'
