"""Widget editor kode dasar AXNN dengan syntax highlighting."""
import logging
from typing import List, Tuple

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

from utils.editor.highlighter import highlight_code

logger = logging.getLogger(__name__)


class CodeEditor(BoxLayout):
    """Editor kode dasar dengan highlight sederhana."""

    language = StringProperty('python')

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.text_input = TextInput(
            multiline=True,
            background_color=(0.07, 0.07, 0.07, 1),
            foreground_color=(0.97, 0.97, 0.95, 1),
            cursor_color=(0.22, 1, 0.08, 1),  # Hijau Matrix
            font_name='RobotoMono-Regular',
            font_size='14sp',
        )
        self.add_widget(self.text_input)

    def set_code(self, code: str) -> None:
        """Isi editor dengan kode."""
        self.text_input.text = code

    def get_code(self) -> str:
        """Ambil isi editor."""
        return self.text_input.text

    def apply_highlight(self) -> List[Tuple[str, str]]:
        """Render highlight (prototipe M1, belum diaplikasikan ke UI)."""
        return highlight_code(self.get_code(), self.language)
