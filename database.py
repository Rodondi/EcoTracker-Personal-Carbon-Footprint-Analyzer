import sqlite3
import os

def setup_database():
    """
    Initializes the SQLite database and creates the necessary table if it doesn't exist.
    This function ensures the data folder exists, then sets up the logs table.
    """

    # Creates data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Connects to the database (creates it if it doesn't exist)
    conn = sqlite3.connect("data/eco_tracker.db")
    cursor = conn.cursor()

    # Creates the logs table to store activity entries
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            transport_km REAL,
            electricity_kwh REAL,
            diet TEXT
        )
    """)

    # Commits changes and closes connection
    conn.commit()
    conn.close()
