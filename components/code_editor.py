# components/code_editor.py
from kivy.uix.codeinput import CodeInput
from pygments.lexers import PythonLexer

class BasicCodeEditor(CodeInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lexer = PythonLexer()  # Default sementara
        self.font_name = 'RobotoMono-Regular'
        self.background_color = (0.07, 0.07, 0.07, 1) # Dark mode base
