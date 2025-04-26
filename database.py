import os
import sqlite3

def setup_database():
    """Create the database and logs table if they don't exist."""
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect("data/eco_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            transport_km REAL,
            electricity_kwh REAL,
            diet TEXT
        )
    """)

    conn.commit()
    conn.close()
