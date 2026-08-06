"""
Model Folder.
Hanya mengurus data folder.
Tidak boleh ada logika UI.
"""

from utils import database
from utils import helpers


def create(name, color="#2196F3", is_default=0):
    """
    Membuat folder baru.

    Args:
        name: Nama folder.
        color: Warna hex.
        is_default: 1 jika folder default.

    Returns:
        int id folder baru.
    """
    conn = database.get_connection()

    try:
        if is_default:
            conn.execute("UPDATE folders SET is_default = 0")

        cursor = conn.execute(
            """
            INSERT INTO folders (name, color, is_default)
            VALUES (?, ?, ?)
            """,
            (name, color, int(is_default)),
        )

        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def get_all():
    """
    Mengambil semua folder.

    Returns:
        list of dict folder.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            SELECT *
            FROM folders
            ORDER BY is_default DESC, name ASC
            """
        )
        return helpers.rows_to_list(cursor.fetchall())
    finally:
        conn.close()


def get_by_id(folder_id):
    """
    Mengambil satu folder berdasarkan id.

    Args:
        folder_id: int id folder.

    Returns:
        dict folder atau None.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            SELECT *
            FROM folders
            WHERE id = ?
            """,
            (folder_id,),
        )
        return helpers.row_to_dict(cursor.fetchone())
    finally:
        conn.close()


def get_default():
    """
    Mengambil folder default.

    Returns:
        dict folder default atau None.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            SELECT *
            FROM folders
            WHERE is_default = 1
            LIMIT 1
            """
        )
        return helpers.row_to_dict(cursor.fetchone())
    finally:
        conn.close()


def update(folder_id, name=None, color=None, is_default=None):
    """
    Update folder.

    Args:
        folder_id: id folder.
        name: nama baru opsional.
        color: warna baru opsional.
        is_default: status default opsional.

    Returns:
        bool True jika ada baris ter-update.
    """
    sets = []
    params = []

    if name is not None:
        sets.append("name = ?")
        params.append(name)

    if color is not None:
        sets.append("color = ?")
        params.append(color)

    if is_default is not None:
        sets.append("is_default = ?")
        params.append(int(is_default))

    if not sets:
        return False

    params.append(folder_id)

    conn = database.get_connection()

    try:
        if is_default == 1:
            conn.execute("UPDATE folders SET is_default = 0")

        query = f"""
        UPDATE folders
        SET {', '.join(sets)}
        WHERE id = ?
        """

        cursor = conn.execute(query, params)
        conn.commit()

        return cursor.rowcount > 0
    finally:
        conn.close()


def delete(folder_id):
    """
    Menghapus folder.

    Args:
        folder_id: id folder.

    Returns:
        bool True jika folder terhapus.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            DELETE FROM folders
            WHERE id = ?
            """,
            (folder_id,),
        )

        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()