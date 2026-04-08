"""
Sistema de notas persistentes con SQLite.
"""

import sqlite3
from datetime import datetime
from pathlib import Path


class NotesDB:
    def __init__(self, db_path: str = "gemmabot_notes.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    category TEXT DEFAULT 'general'
                )
            """)

    def add(self, text: str, category: str = "general") -> str:
        if not text.strip():
            return "Error: texto vacio"
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO notes (text, created_at, category) VALUES (?, ?, ?)",
                (text.strip(), now, category),
            )
        return f"Nota guardada: \"{text.strip()}\""

    def list_all(self) -> str:
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT id, text, created_at, category FROM notes ORDER BY id DESC LIMIT 20"
            ).fetchall()
        if not rows:
            return "No hay notas guardadas."
        lines = [f"=== MIS NOTAS ({len(rows)}) ===\n"]
        for row in rows:
            lines.append(f"[{row[0]}] {row[1]}\n    {row[2]} | {row[3]}")
        return "\n".join(lines)

    def delete(self, note_id: int) -> str:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
            if cursor.rowcount == 0:
                return f"No existe nota con ID {note_id}"
        return f"Nota {note_id} borrada."

    def search(self, query: str) -> str:
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT id, text, created_at FROM notes WHERE text LIKE ? ORDER BY id DESC",
                (f"%{query}%",),
            ).fetchall()
        if not rows:
            return f"No se encontraron notas con: {query}"
        lines = [f"=== RESULTADOS: {query} ({len(rows)}) ===\n"]
        for row in rows:
            lines.append(f"[{row[0]}] {row[1]}\n    {row[2]}")
        return "\n".join(lines)
