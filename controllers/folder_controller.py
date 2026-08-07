"""Controller manajemen folder (F003)."""

import re
from typing import Dict

from controllers.base_controller import BaseController
from models.folder_model import FolderModel

FOLDER_NAME_PATTERN: str = r"^[\w\s\-]+$"  # huruf, angka, spasi, underscore, strip


class FolderController(BaseController):
    """Logika bisnis folder + filter."""

    def __init__(self) -> None:
        """Ikatkan ke FolderModel."""
        super().__init__(FolderModel)

    def create_folder(self, name: str, color: str = "#2196F3") -> Dict:
        """Buat folder baru dengan validasi nama unik & format.

        Args:
            name (str): Nama folder.
            color (str): Warna folder (hex).

        Returns:
            Dict: Hasil operasi.
        """
        name = name.strip()
        if not name:
            return {"success": False, "error": "Nama folder tidak boleh kosong"}
        if not re.match(FOLDER_NAME_PATTERN, name):
            return {
                "success": False,
                "error": "Nama hanya boleh huruf, angka, spasi, underscore",
            }
        if self.model.get_by_name(name):
            return {"success": False, "error": "Nama folder sudah dipakai"}

        data = {"name": name, "color": color, "is_default": 0}
        return self.create(data)

    def delete_folder(self, folder_id: int) -> Dict:
        """Hapus folder; folder default tidak boleh dihapus.

        Args:
            folder_id (int): ID folder.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            folder = self.model.get_by_id(folder_id)
            if not folder:
                return {"success": False, "error": "Folder tidak ditemukan"}
            if folder.get("is_default") == 1:
                return {"success": False, "error": "Folder default tidak bisa dihapus"}
            return self.delete(folder_id)
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)}

    def get_folders(self) -> Dict:
        """Ambil semua folder untuk dropdown filter.

        Returns:
            Dict: Hasil operasi.
        """
        try:
            result = self.model.get_all_folders()
            return {"success": True, "data": result}
        except Exception as exc:  # noqa: BLE001
            return {"success": False, "error": str(exc)} 
