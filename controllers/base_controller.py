from typing import Dict, Any
from models.base_model import BaseModel
import logging

logger = logging.getLogger(__name__)

class BaseController:
    """Controller dasar yang diwarisi semua controller lain."""
    
    def __init__(self, model_class: type[BaseModel]):
        self.model = model_class
        
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            record_id = self.model.insert(data)
            return {"success": True, "data": {"id": record_id}}
        except Exception as e:
            logger.error(f"Error create: {e}")
            return {"success": False, "error": str(e)}
            
    def get_all(self) -> Dict[str, Any]:
        try:
            return {"success": True, "data": self.model.get_all()}
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def get_by_id(self, record_id: int) -> Dict[str, Any]:
        try:
            result = self.model.get_by_id(record_id)
            if result: return {"success": True, "data": result}
            return {"success": False, "error": "Data tidak ditemukan"}
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def update(self, record_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            if self.model.update(record_id, data):
                return {"success": True, "data": {"id": record_id}}
            return {"success": False, "error": "Gagal update data"}
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def delete(self, record_id: int) -> Dict[str, Any]:
        try:
            if self.model.delete(record_id):
                return {"success": True, "data": {"id": record_id}}
            return {"success": False, "error": "Gagal hapus data"}
        except Exception as e:
            return {"success": False, "error": str(e)}
