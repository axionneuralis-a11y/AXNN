"""
Konstanta resmi AXNN.
Dimiliki oleh Tim B.
Jangan mengubah nilai inti tanpa koordinasi Tim A.
"""

APP_NAME = "AXNN"

DB_FILENAME = "axnn.db"

DEFAULT_FOLDER_NAME = "Default"
DEFAULT_FOLDER_COLOR = "#2196F3"

MAX_NOTE_TITLE_LENGTH = 200
MAX_TODO_TASK_LENGTH = 500
MAX_FOLDER_NAME_LENGTH = 100

# Disiapkan untuk kebutuhan izin Android Tim B + Tim E.
# Eksekusi izin runtime tetap mengikuti milestone dan koordinasi Tim E.
ANDROID_PERMISSIONS_REQUIRED = [
    "WRITE_INTERNAL_STORAGE",
    "READ_INTERNAL_STORAGE",
    "WRITE_EXTERNAL_STORAGE",
    "READ_EXTERNAL_STORAGE",
    "NOTIFICATIONS",
    "VIBRATE",
    "POST_NOTIFICATIONS",
]