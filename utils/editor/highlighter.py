"""Syntax highlighter menggunakan Pygments untuk editor AXNN."""
import logging
from typing import List, Tuple

from pygments import highlight
from pygments.lexers import get_lexer_by_name, PythonLexer
from pygments.token import Token
from pygments.formatter import Formatter

logger = logging.getLogger(__name__)


class KivySegmentFormatter(Formatter):
    """Formatter Pygments custom yang menghasilkan segmen (teks, warna) untuk Kivy."""

    # Peta warna token -> hex (tema default gelap, bisa di-override ThemeManager)
    TOKEN_COLORS = {
        Token.Keyword: '#FF79C6',
        Token.Keyword.Namespace: '#FF79C6',
        Token.Name.Function: '#50FA7B',
        Token.Name.Class: '#8BE9FD',
        Token.String: '#F1FA8C',
        Token.Number: '#BD93F9',
        Token.Comment: '#6272A4',
        Token.Operator: '#FF9F43',
        Token.Punctuation: '#F8F8F2',
        Token.Name.Builtin: '#8BE9FD',
    }

    DEFAULT_COLOR = '#F8F8F2'

    def __init__(self, **options):
        super().__init__(**options)
        self.segments: List[Tuple[str, str]] = []

    def format(self, tokensource, outfile):
        self.segments = []
        for token_type, value in tokensource:
            color = self.TOKEN_COLORS.get(token_type, self.DEFAULT_COLOR)
            self.segments.append((value, color))
        return self.segments


def highlight_code(code: str, language: str = 'python') -> List[Tuple[str, str]]:
    """Highlight kode menjadi list segmen (teks, warna_hex).

    Args:
        code: Kode sumber.
        language: Bahasa pemrograman (default: python).

    Returns:
        List[(teks, warna_hex)]
    """
    try:
        lexer = get_lexer_by_name(language)
    except Exception:
        lexer = PythonLexer()

    formatter = KivySegmentFormatter()
    return highlight(code, lexer, formatter)
