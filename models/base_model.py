import sqlite3
from typing import List, Dict, Optional, Any
from utils.database import get_db_connection
import logging

logger = logging.getLogger(__name__)

class BaseModel:
    """Model dasar yang diwarisi semua model lain (Pola MVC Ketat)."""
    
    table_name: str = ""
    
    @classmethod
    def insert(cls, data: Dict[str, Any]) -> int:
        """Insert data baru ke database (Aman dari SQL Injection)."""
        if not cls.table_name:
            raise ValueError("table_name belum didefinisikan pada model")
            
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {cls.table_name} ({columns}) VALUES ({placeholders})"
        
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, list(data.values()))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Database error pada insert {cls.table_name}: {e}")
            raise
        finally:
            conn.close()
            
    @classmethod
    def get_all(cls, limit: Optional[int] = None, order_by: str = "created_at DESC") -> List[Dict[str, Any]]:
        """Ambil semua data dari tabel."""
        query = f"SELECT * FROM {cls.table_name} ORDER BY {order_by}"
        if limit:
            query += f" LIMIT {limit}"
            
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            return [dict(row) for row in cursor.fetchall()]
        finally:
            conn.close()
            
    @classmethod
    def get_by_id(cls, record_id: int) -> Optional[Dict[str, Any]]:
        """Ambil 1 data berdasarkan ID."""
        query = f"SELECT * FROM {cls.table_name} WHERE id = ?"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (record_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
        finally:
            conn.close()
            
    @classmethod
    def update(cls, record_id: int, data: Dict[str, Any]) -> bool:
        """Update data berdasarkan ID + otomatis update timestamp."""
        if not data: return False
            
        set_clause = ', '.join([f"{k} = ?" for k in data.keys()])
        query = f"UPDATE {cls.table_name} SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
        values = list(data.values()) + [record_id]
        
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Database error pada update {cls.table_name}: {e}")
            return False
        finally:
            conn.close()
            
    @classmethod
    def delete(cls, record_id: int) -> bool:
        """Hapus data berdasarkan ID."""
        query = f"DELETE FROM {cls.table_name} WHERE id = ?"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (record_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Database error pada delete {cls.table_name}: {e}")
            return False
        finally:
            conn.close()
