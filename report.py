import sqlite3
import matplotlib.pyplot as plt
import streamlit as st  # ✅ Add this for Streamlit support

def generate_report():
    """Generate a line chart showing CO2 emissions over time."""
    conn = sqlite3.connect("data/eco_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, transport_km, electricity_kwh, diet FROM logs")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        st.warning("No data found to generate a report.")
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

        dates.append(date[:10])  # Only take YYYY-MM-DD
        emissions.append(total_emission)

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(dates, emissions, marker='o')
    ax.set_title("Carbon Emissions Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("CO₂ Emissions (kg)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Streamlit way to show the figure
    st.pyplot(fig)


def view_all_logs():
    """Fetch and display all logged activities nicely."""
    conn = sqlite3.connect("data/eco_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, transport_km, electricity_kwh, diet FROM logs")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        st.warning("No logged activities found.")
        return

    # Create a nicer dataframe-like table
    st.subheader("📝 All Logged Activities")
    for idx, (date, transport_km, electricity_kwh, diet) in enumerate(rows, 1):
        st.text(f"{idx}. Date: {date[:10]} | Distance: {transport_km} km | Electricity: {electricity_kwh} kWh | Diet: {diet}")