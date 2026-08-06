"""
Model Catatan.
Hanya mengurus data catatan.
Tidak boleh ada logika UI.
"""

from utils import database
from utils import helpers


def create(title, content="", folder_id=None, reminder_at=None):
    """
    Membuat catatan baru.

    Args:
        title: Judul catatan.
        content: Isi catatan.
        folder_id: id folder opsional.
        reminder_at: waktu reminder opsional.

    Returns:
        int id catatan baru.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO notes (
                title,
                content,
                folder_id,
                reminder_at,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))
            """,
            (title, content, folder_id, reminder_at),
        )

        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def get_all(folder_id=None, limit=None):
    """
    Mengambil daftar catatan.

    Args:
        folder_id: Filter folder opsional.
        limit: Batas jumlah data.

    Returns:
        list of dict catatan.
    """
    query = """
    SELECT
        n.*,
        f.name AS folder_name
    FROM notes n
    LEFT JOIN folders f ON n.folder_id = f.id
    """

    params = []

    if folder_id is not None:
        query += " WHERE n.folder_id = ?"
        params.append(folder_id)

    query += " ORDER BY n.updated_at DESC, n.id DESC"

    if limit is not None:
        query += " LIMIT ?"
        params.append(limit)

    conn = database.get_connection()

    try:
        cursor = conn.execute(query, params)
        return helpers.rows_to_list(cursor.fetchall())
    finally:
        conn.close()


def get_by_id(note_id):
    """
    Mengambil satu catatan berdasarkan id.

    Args:
        note_id: int id catatan.

    Returns:
        dict catatan atau None.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            SELECT
                n.*,
                f.name AS folder_name
            FROM notes n
            LEFT JOIN folders f ON n.folder_id = f.id
            WHERE n.id = ?
            """,
            (note_id,),
        )

        return helpers.row_to_dict(cursor.fetchone())
    finally:
        conn.close()


def get_latest(limit=3):
    """
    Mengambil catatan terbaru untuk Home.

    Args:
        limit: jumlah catatan, default 3.

    Returns:
        list of dict catatan.
    """
    return get_all(limit=limit)


def update(note_id, title=None, content=None, folder_id=None, reminder_at=None):
    """
    Update catatan.

    Args:
        note_id: id catatan.
        title: judul baru opsional.
        content: isi baru opsional.
        folder_id: folder baru opsional.
        reminder_at: reminder baru opsional.

    Returns:
        bool True jika ada baris ter-update.
    """
    sets = []
    params = []

    if title is not None:
        sets.append("title = ?")
        params.append(title)

    if content is not None:
        sets.append("content = ?")
        params.append(content)

    if folder_id is not None:
        sets.append("folder_id = ?")
        params.append(folder_id)

    if reminder_at is not None:
        sets.append("reminder_at = ?")
        params.append(reminder_at)

    if not sets:
        return False

    sets.append("updated_at = datetime('now')")
    params.append(note_id)

    conn = database.get_connection()

    try:
        query = f"""
        UPDATE notes
        SET {', '.join(sets)}
        WHERE id = ?
        """

        cursor = conn.execute(query, params)
        conn.commit()

        return cursor.rowcount > 0
    finally:
        conn.close()


def delete(note_id):
    """
    Menghapus catatan.

    Args:
        note_id: id catatan.

    Returns:
        bool True jika catatan terhapus.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            DELETE FROM notes
            WHERE id = ?
            """,
            (note_id,),
        )

        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def reassign_folder(old_folder_id, new_folder_id):
    """
    Memindahkan catatan dari folder lama ke folder baru.
    Dipakai saat folder lama dihapus agar catatan tidak hilang.

    Args:
        old_folder_id: id folder lama.
        new_folder_id: id folder tujuan.

    Returns:
        int jumlah catatan yang dipindahkan.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            UPDATE notes
            SET folder_id = ?
            WHERE folder_id = ?
            """,
            (new_folder_id, old_folder_id),
        )

        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()