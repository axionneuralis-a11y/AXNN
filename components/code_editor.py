"""Widget editor kode dasar (N009 target M2: bisa ketik multibaris)."""

from kivy.uix.codeinput import CodeInput
from pygments.lexers import PythonLexer


class BasicCodeEditor(CodeInput):
    """Editor teks kode sederhana dengan lexer Python default."""

    def __init__(self, **kwargs):
        """Set font mono, lexer default, dan warna dasar gelap."""
        super().__init__(**kwargs)
        self.lexer = PythonLexer()
        self.font_name = "RobotoMono-Regular"
        self.background_color = (0.07, 0.07, 0.07, 1)
        self.foreground_color = (0, 1, 0.25, 1)
