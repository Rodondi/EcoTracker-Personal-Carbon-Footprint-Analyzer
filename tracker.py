import sqlite3
from datetime import datetime
from api import calculate_transport_emission, calculate_energy_emission

def log_activities(transport_km=None, electricity_kwh=None, diet=None):
    """
    Log activities: If values are not passed, ask for input manually (for CLI).
    """
    # If not provided (Terminal mode), ask user
    if transport_km is None:
        transport_km = float(input("How many km did you travel today by car? "))
    if electricity_kwh is None:
        electricity_kwh = float(input("How much electricity did you use (kWh)? "))
    if diet is None:
        diet = input("What kind of diet? (vegan/vegetarian/mixed/meat-heavy): ")

    transport_emission = calculate_transport_emission(transport_km)
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