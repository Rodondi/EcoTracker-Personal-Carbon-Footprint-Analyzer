
# report.py

import sqlite3
import matplotlib.pyplot as plt
import streamlit as st

def fetch_logs():
    """Retrieve all logs from the SQLite database."""
    conn = sqlite3.connect("data/eco_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, transport_km, electricity_kwh, diet FROM logs")
    rows = cursor.fetchall()
    conn.close()
    return rows

def generate_report():
    """Generate and display a CO₂ emission trend chart using matplotlib."""
    st.header("📈 Emission Trend Report")

    # Optional refresh logic
    if st.button("🔄 Refresh Report"):
        st.rerun()

    rows = fetch_logs()

    if not rows:
        st.warning("No data found to generate a report.")
        return

    dates = []
    emissions = []

    # Process each log entry and calculate total emissions
    for date, transport_km, electricity_kwh, diet in rows:
        total_emission = transport_km * 0.21 + electricity_kwh * 0.405
        if diet == "meat-heavy":
            total_emission += 5
        elif diet == "mixed":
            total_emission += 3
        elif diet == "vegetarian":
            total_emission += 2
        elif diet == "vegan":
            total_emission += 1

        dates.append(date[:10])  # Use only the date part
        emissions.append(total_emission)

    # Generate a line chart of emissions over time
    fig, ax = plt.subplots()
    ax.plot(dates, emissions, marker='o')
    ax.set_title("Carbon Emissions Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("CO₂ Emissions (kg)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

def view_all_logs():
    """Display all user activity logs in a formatted list."""
    st.header("📝 All Logged Activities")

    if st.button("🔄 Refresh Logs"):
        st.rerun()

    rows = fetch_logs()

    if not rows:
        st.warning("No logged activities found.")
        return

    for idx, (date, transport_km, electricity_kwh, diet) in enumerate(rows, 1):
        st.text(f"{idx}. Date: {date[:10]} | Distance: {transport_km} km | Electricity: {electricity_kwh} kWh | Diet: {diet}")
