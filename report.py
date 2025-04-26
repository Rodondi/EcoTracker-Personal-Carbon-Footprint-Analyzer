import sqlite3
import matplotlib.pyplot as plt
import streamlit as st

def fetch_logs():
    """Fetch all logged activities from the database."""
    conn = sqlite3.connect("data/eco_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, transport_km, electricity_kwh, diet FROM logs")
    rows = cursor.fetchall()
    conn.close()
    return rows

def generate_report():
    """Display a line chart of CO₂ emissions over time."""
    st.header("📈 Emission Trend Report")

    rows = fetch_logs()

    if not rows:
        st.warning("No data available to generate a report.")
        return

    dates = []
    emissions = []

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

        dates.append(date[:10])  # Only the YYYY-MM-DD part
        emissions.append(total_emission)

    fig, ax = plt.subplots()
    ax.plot(dates, emissions, marker='o')
    ax.set_title("Carbon Emissions Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("CO₂ Emissions (kg)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

def view_all_logs():
    """Display a list of all logged activities."""
    st.header("📝 All Logged Activities")

    rows = fetch_logs()

    if not rows:
        st.warning("No logged activities found.")
        return

    for idx, (date, transport_km, electricity_kwh, diet) in enumerate(rows, start=1):
        st.text(f"{idx}. Date: {date[:10]} | Distance: {transport_km} km | Electricity: {electricity_kwh} kWh | Diet: {diet}")
