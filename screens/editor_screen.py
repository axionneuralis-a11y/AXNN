"""Editor Screen — layar edit kode dengan highlight (N008)."""
import logging

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from components.editor.code_editor import CodeEditor

logger = logging.getLogger(__name__)


class EditorScreen(Screen):
    """Layar editor kode AXNN."""

    language = StringProperty('python')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.editor = CodeEditor(language=self.language)
        self.add_widget(self.editor)

    def on_pre_enter(self, *args) -> None:
        logger.info("Editor dibuka dengan bahasa: %s", self.language) 
