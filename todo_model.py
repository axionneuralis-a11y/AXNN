"""
Model Todo.
Hanya mengurus data daftar tugas.
Tidak boleh ada logika UI.
"""

from utils import database
from utils import helpers


def create(task, folder_id=None, due_date=None):
    """
    Membuat todo baru.

    Args:
        task: Isi tugas.
        folder_id: id folder opsional.
        due_date: tenggat waktu opsional.

    Returns:
        int id todo baru.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO todos (
                task,
                is_done,
                folder_id,
                due_date,
                created_at
            )
            VALUES (?, 0, ?, ?, datetime('now'))
            """,
            (task, folder_id, due_date),
        )

        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def get_all(folder_id=None, include_done=True, limit=None):
    """
    Mengambil daftar todo.

    Args:
        folder_id: Filter folder opsional.
        include_done: Jika False, todo selesai disembunyikan.
        limit: Batas jumlah data.

    Returns:
        list of dict todo.
    """
    query = """
    SELECT
        t.*,
        f.name AS folder_name
    FROM todos t
    LEFT JOIN folders f ON t.folder_id = f.id
    """

    conditions = []
    params = []

    if folder_id is not None:
        conditions.append("t.folder_id = ?")
        params.append(folder_id)

    if not include_done:
        conditions.append("t.is_done = 0")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY t.created_at DESC, t.id DESC"

    if limit is not None:
        query += " LIMIT ?"
        params.append(limit)

    conn = database.get_connection()

    try:
        cursor = conn.execute(query, params)
        return helpers.rows_to_list(cursor.fetchall())
    finally:
        conn.close()


def get_by_id(todo_id):
    """
    Mengambil satu todo berdasarkan id.

    Args:
        todo_id: int id todo.

    Returns:
        dict todo atau None.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            SELECT
                t.*,
                f.name AS folder_name
            FROM todos t
            LEFT JOIN folders f ON t.folder_id = f.id
            WHERE t.id = ?
            """,
            (todo_id,),
        )

        return helpers.row_to_dict(cursor.fetchone())
    finally:
        conn.close()


def get_latest(limit=3):
    """
    Mengambil todo terbaru untuk Home.

    Args:
        limit: jumlah todo, default 3.

    Returns:
        list of dict todo.
    """
    return get_all(limit=limit)


def update(todo_id, task=None, is_done=None, folder_id=None, due_date=None):
    """
    Update todo.

    Args:
        todo_id: id todo.
        task: isi tugas baru opsional.
        is_done: status selesai opsional.
        folder_id: folder baru opsional.
        due_date: tenggat baru opsional.

    Returns:
        bool True jika ada baris ter-update.
    """
    sets = []
    params = []

    if task is not None:
        sets.append("task = ?")
        params.append(task)

    if is_done is not None:
        sets.append("is_done = ?")
        params.append(int(is_done))

    if folder_id is not None:
        sets.append("folder_id = ?")
        params.append(folder_id)

    if due_date is not None:
        sets.append("due_date = ?")
        params.append(due_date)

    if not sets:
        return False

    params.append(todo_id)

    conn = database.get_connection()

    try:
        query = f"""
        UPDATE todos
        SET {', '.join(sets)}
        WHERE id = ?
        """

        cursor = conn.execute(query, params)
        conn.commit()

        return cursor.rowcount > 0
    finally:
        conn.close()


def set_done(todo_id, is_done=True):
    """
    Menandai todo selesai atau belum selesai.

    Args:
        todo_id: id todo.
        is_done: True jika selesai.

    Returns:
        bool True jika update sukses.
    """
    return update(todo_id, is_done=1 if is_done else 0)


def delete(todo_id):
    """
    Menghapus todo.

    Args:
        todo_id: id todo.

    Returns:
        bool True jika todo terhapus.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            DELETE FROM todos
            WHERE id = ?
            """,
            (todo_id,),
        )

        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def reassign_folder(old_folder_id, new_folder_id):
    """
    Memindahkan todo dari folder lama ke folder baru.
    Dipakai saat folder lama dihapus agar todo tidak hilang.

    Args:
        old_folder_id: id folder lama.
        new_folder_id: id folder tujuan.

    Returns:
        int jumlah todo yang dipindahkan.
    """
    conn = database.get_connection()

    try:
        cursor = conn.execute(
            """
            UPDATE todos
            SET folder_id = ?
            WHERE folder_id = ?
            """,
            (new_folder_id, old_folder_id),
        )

        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()