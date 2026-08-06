import os
import logging
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# Setup Logging (Bab 2.8)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import Backend & Utils (Tim B)
from utils.database import init_db
from controllers.settings_controller import SettingsController
# from controllers.theme_controller import ThemeController  # Akan dieksekusi Tim C

class AXNNApp(App):
    title = "AXNN"  # WAJIB (Blueprint 5.1)
    
    def build(self):
        logger.info("Memulai aplikasi AXNN v1.1.0...")
        
        # 1. Inisialisasi Database SQLite
        init_db()
        
        # 2. Muat Tema Tersimpan (Koordinasi dengan Tim C)
        settings_ctrl = SettingsController()
        theme_result = settings_ctrl.get_theme()
        current_theme = theme_result['data']['theme'] if theme_result['success'] else 'light'
        logger.info(f"Tema aktif: {current_theme}")
        
        # 3. Setup ScreenManager (Akan diisi oleh Tim C)
        sm = ScreenManager()
        # sm.add_widget(HomeScreen(name='home')) -> Tim C
        # sm.add_widget(NotesScreen(name='notes')) -> Tim C
        
        logger.info("Backend siap. Menyerahkan kontrol ke UI (Tim C).")
        return sm

if __name__ == '__main__':
    # Hemat memori & cegah log file kivy tercecer di storage user
    os.environ['KIVY_NO_FILELOG'] = '1' 
    os.environ['KIVY_NO_CONSOLELOG'] = '0'
    AXNNApp().run() 
import os
import logging

os.environ['KIVY_NO_FILELOG'] = '1'  # Hemat memori

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from utils.database import init_db
from controllers.theme_controller import ThemeController
from screens.home_screen import HomeScreen
from screens.notes_screen import NotesScreen
from screens.todos_screen import TodosScreen
from screens.calculator_screen import CalculatorScreen
from screens.calendar_screen import CalendarScreen
from screens.settings_screen import SettingsScreen

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class AXNNApp(App):
    title = "AXNN"  # WAJIB (Blueprint 5.1)
    theme_ctrl = ThemeController()

    def build(self):
        logger.info("Boot AXNN v1.1.0...")
        init_db()

        # Muat tema tersimpan sebelum render UI
        self.theme_ctrl.load_saved_theme()

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(NotesScreen(name='notes'))
        sm.add_widget(TodosScreen(name='list'))
        sm.add_widget(CalculatorScreen(name='calc'))
        sm.add_widget(CalendarScreen(name='calendar'))
        sm.add_widget(SettingsScreen(name='settings'))

        logger.info("UI siap. Tema aktif: %s", self.theme_ctrl.get_current_theme())
        return sm


if __name__ == '__main__':
    os.environ['KIVY_NO_FILELOG'] = '1'
    AXNNApp().run()
