"""Fungsi bantuan (helpers) untuk sanitasi dan formatting."""
import re
import logging
from datetime import datetime
from utils.constants import MAX_NOTE_TITLE_LENGTH

logger = logging.getLogger(__name__)

def sanitize_filename(filename: str) -> str:
    """
    Membersihkan nama file dari karakter ilegal (Bab 17 Security).
    Mencegah path traversal dan error filesystem Android.
    """
    # Hapus karakter \/:*?"<>|
    sanitized = re.sub(r'[\\/*?:"<>|]', "", filename)
    return sanitized.strip()

def validate_note_title(title: str) -> tuple[bool, str]:
    """Validasi judul catatan sesuai aturan Bible."""
    if not title or not title.strip():
        return False, "Judul tidak boleh kosong."
    if len(title) > MAX_NOTE_TITLE_LENGTH:
        return False, f"Judul maksimal {MAX_NOTE_TITLE_LENGTH} karakter."
    return True, ""

def validate_calc_expression(expression: str) -> bool:
    """Validasi input kalkulator agar hanya berisi angka dan operator dasar (Anti-Inject)."""
    return bool(re.match(r'^[\d\+\-\*\/\.\(\)\s]+$', expression))

def format_datetime(dt_string: str) -> str:
    """Format timestamp SQLite (YYYY-MM-DD HH:MM:SS) menjadi string ramah user."""
    try:
        dt = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%d %b %Y, %H:%M")
    except (ValueError, TypeError):
        return str(dt_string) 
