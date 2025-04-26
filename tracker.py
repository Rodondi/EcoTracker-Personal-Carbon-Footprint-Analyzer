import sqlite3
from datetime import datetime
from api import calculate_transport_emission, calculate_energy_emission

def log_activities(transport_km, electricity_kwh, diet, vehicle_model_id=None):
    """Log a user's daily activities into the database."""
    transport_emission = calculate_transport_emission(transport_km, vehicle_model_id)
    electricity_emission = calculate_energy_emission(electricity_kwh)

    conn = sqlite3.connect("data/eco_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO logs (date, transport_km, electricity_kwh, diet)
        VALUES (?, ?, ?, ?)
    """, (datetime.now().isoformat(), transport_km, electricity_kwh, diet))

    conn.commit()
    conn.close()

    print(f"Transport CO₂: {transport_emission} kg, Electricity CO₂: {electricity_emission} kg")
    print("Data logged successfully!")
