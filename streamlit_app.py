import streamlit as st
from tracker import log_activities
from report import generate_report, view_all_logs
from utils import get_random_tip
from database import setup_database

# Setup database on app start
setup_database()

# Streamlit app UI
st.set_page_config(page_title="EcoTracker", page_icon="🌱")

st.title("🌱 EcoTracker: Personal Carbon Footprint Analyzer")

menu = ["Log Activities", "View Emission Report", "View All Logs", "Get Eco Tip"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Log Activities":
    st.header("Log Today's Activities")
    transport_km = st.number_input("How many km did you travel today?", min_value=0.0, step=0.1)
    electricity_kwh = st.number_input("How much electricity did you use (kWh)?", min_value=0.0, step=0.1)
    diet = st.selectbox("What kind of diet?", ["vegan", "vegetarian", "mixed", "meat-heavy"])
    
    if st.button("Log Activity"):
        log_activities(transport_km, electricity_kwh, diet)
        st.success("✅ Activity logged successfully!")

elif choice == "View Emission Report":
    st.header("📈 Emission Report")
    generate_report()

elif choice == "View All Logs":
    st.header("📋 All Logged Activities")
    view_all_logs()

elif choice == "Get Eco Tip":
    st.header("🌿 Eco Tip of the Day")
    st.info(get_random_tip())