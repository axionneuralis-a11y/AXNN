"""Controller dasar yang diwarisi semua controller lain (Blueprint 5.6)."""

from typing import Dict, List, Optional

from models.base_model import BaseModel


class BaseController:
    """Base controller dengan CRUD umum + error handling terpusat."""

    def __init__(self, model: BaseModel):
        """Inisialisasi dengan model terkait.

        Args:
            model (BaseModel): Model yang dikelola controller ini.
        """
        self.model = model

    def create(self, data: Dict) -> Dict:
        """Buat entri baru.

        Args:
            data (Dict): Data yang akan disimpan.

        Returns:
            Dict: {"success": bool, "data"/"error": ...}
        """
        try:
            result = self.model.insert(data)
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001 - error dikirim ke View
            return {"success": False, "error": str(exc)}

    def get_all(self, limit: Optional[int] = None) -> Dict:
        """Ambil semua entri.

        Args:
            limit (Optional[int]): Batas jumlah data.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.get_all(limit)
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}

    def get_by_id(self, record_id: int) -> Dict:
        """Ambil satu entri berdasarkan ID.

        Args:
            record_id (int): ID entri.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.get_by_id(record_id)
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}

    def update(self, record_id: int, data: Dict) -> Dict:
        """Update satu entri.

        Args:
            record_id (int): ID entri.
            data (Dict): Data baru.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.update(record_id, data)
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}

    def delete(self, record_id: int) -> Dict:
        """Hapus satu entri.

        Args:
            record_id (int): ID entri.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.delete(record_id)
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}
