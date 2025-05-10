
# streamlit_app.py

import streamlit as st
from tracker import log_activities
from report import generate_report, view_all_logs
from api import fetch_vehicle_makes, fetch_vehicle_models

# Configure the Streamlit app layout and title
st.set_page_config(page_title="EcoTracker", page_icon="🌱")
st.title("🌱 EcoTracker: Personal Carbon Footprint Analyzer")

# Sidebar menu options
menu = ["Log Activities", "View Emission Report", "View All Logs", "Get Eco Tip"]
choice = st.sidebar.selectbox("Select Action", menu)

# If the user chooses to log activities
if choice == "Log Activities":
    st.header("🚗 Log Today's Activities")

    # Input fields for transport, electricity, and diet
    transport_km = st.number_input("How many km did you travel today?", min_value=0.0, step=0.1)
    electricity_kwh = st.number_input("How much electricity did you use (kWh)?", min_value=0.0, step=0.1)
    diet = st.selectbox("What kind of diet?", ["vegan", "vegetarian", "mixed", "meat-heavy"])

    # Fetch and display vehicle makes from the API
    makes = fetch_vehicle_makes()
    selected_model_id = None

    if makes:
        # Extract make names for dropdown
        make_names = [make["data"]["attributes"]["name"] for make in makes]
        selected_make = st.selectbox("Select Vehicle Make:", make_names)

        # Get the selected make ID for fetching models
        selected_make_id = makes[make_names.index(selected_make)]["data"]["id"]

        # Fetch and display models for selected make
        models = fetch_vehicle_models(selected_make_id)
        if models:
            model_options = [f"{model['data']['attributes']['name']} ({model['data']['attributes']['year']})" for model in models]
            selected_model_text = st.selectbox("Select Vehicle Model:", model_options)
            selected_model = models[model_options.index(selected_model_text)]
            selected_model_id = selected_model["data"]["id"]

    # Log activity button
    if st.button("Log Activity"):
        log_activities(transport_km, electricity_kwh, diet, selected_model_id)
        st.success("✅ Activity logged successfully!")

# If the user chooses to view the emission report
elif choice == "View Emission Report":
    generate_report()

# If the user chooses to view all activity logs
elif choice == "View All Logs":
    view_all_logs()

# If the user chooses to get an eco tip
elif choice == "Get Eco Tip":
    from utils import get_random_tip
    st.info(get_random_tip())
