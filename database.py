import sqlite3

def connect_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()
