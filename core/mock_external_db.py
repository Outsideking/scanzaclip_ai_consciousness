# core/mock_external_db.py
import sqlite3
import os
import time
from typing import Dict, List, Any

DB_PATH = os.path.join(os.path.dirname(__file__), "mock_behaviors.db")

class MockExternalDB:
    """
    ตัวอย่าง DB แบบ SQLite ที่เก็บ historical behaviors.
    ใช้ง่าย สามารถใช้จริงหรือเป็นตัวอย่างขยายไปเป็น MongoDB/SQL server ได้
    """
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._ensure_db()

    def _ensure_db(self):
        need_seed = not os.path.exists(self.db_path)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS behaviors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                action TEXT,
                emotion TEXT,
                timestamp REAL,
                meta TEXT
            )
        """)
        self.conn.commit()
        if need_seed:
            self._seed_example()

    def _seed_example(self):
        now = time.time()
        rows = [
            ("user_001","say_goodnight","neutral", now - 3600*24, "{}"),
            ("user_001","observe","curious", now - 3600*2, "{}"),
            ("user_002","cheer_up_user","sad", now - 3600*5, "{}"),
            ("user_003","display_sad_expression","sad", now - 3600*36, "{}"),
        ]
        cur = self.conn.cursor()
        cur.executemany("INSERT INTO behaviors (user_id,action,emotion,timestamp,meta) VALUES (?,?,?,?,?)", rows)
        self.conn.commit()

    def insert_behavior(self, user_id: str, action: str, emotion: str, timestamp: float = None, meta: str = "{}"):
        if timestamp is None:
            timestamp = time.time()
        cur = self.conn.cursor()
        cur.execute("INSERT INTO behaviors (user_id,action,emotion,timestamp,meta) VALUES (?,?,?,?,?)", (user_id, action, emotion, timestamp, meta))
        self.conn.commit()

    def query_behaviors(self) -> Dict[str, List[Dict[str,Any]]]:
        """
        คืนค่า dict: { user_id: [ {action,emotion,timestamp,meta}, ... ] }
        """
        cur = self.conn.cursor()
        cur.execute("SELECT user_id, action, emotion, timestamp, meta FROM behaviors ORDER BY timestamp DESC")
        rows = cur.fetchall()
        out = {}
        for user_id, action, emotion, timestamp, meta in rows:
            out.setdefault(user_id, []).append({
                "user_id": user_id,
                "action": action,
                "emotion": emotion,
                "timestamp": timestamp,
                "meta": meta
            })
        return out
