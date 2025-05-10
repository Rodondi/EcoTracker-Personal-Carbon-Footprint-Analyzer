from api import calculate_transport_emission, calculate_energy_emission
import sqlite3
from datetime import datetime

def log_activities(transport_km, electricity_kwh, diet, vehicle_model_id=None):
    """Logs a user's activity to the SQLite database."""

    # Calculating emissions for transport and electricity
    transport_emission = calculate_transport_emission(transport_km, vehicle_model_id)
    electricity_emission = calculate_energy_emission(electricity_kwh)

    # Connecting to the local SQLite database and inserting activity data
    conn = sqlite3.connect("data/eco_tracker.db")
    cursor = conn.cursor()

    # Storing activity with timestamp
    cursor.execute("""
        INSERT INTO logs (date, transport_km, electricity_kwh, diet)
        VALUES (?, ?, ?, ?)
    """, (datetime.now().isoformat(), transport_km, electricity_kwh, diet))

    # Committing changes and closing connection
    conn.commit()
    conn.close()

    # Printing summary to the terminal (for debugging or CLI use)
    print(f"Transport CO₂: {transport_emission} kg, Electricity CO₂: {electricity_emission} kg")
    print("Data logged successfully!")
