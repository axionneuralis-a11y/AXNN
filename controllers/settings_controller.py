from models.setting_model import SettingModel
from utils.constants import VALID_THEMES, DEFAULT_THEME

class SettingsController:
    def __init__(self):
        self.model = SettingModel()
        
    def get_theme(self) -> dict:
        try:
            theme = self.model.get_value('theme', DEFAULT_THEME)
            return {"success": True, "data": {"theme": theme}}
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def set_theme(self, theme_name: str) -> dict:
        if theme_name not in VALID_THEMES:
            return {"success": False, "error": "Tema tidak valid"}
        try:
            self.model.set_value('theme', theme_name)
            return {"success": True, "data": {"theme": theme_name}}
        except Exception as e:
            return {"success": False, "error": str(e)} 
