import streamlit as st
from tracker import log_activities
from report import generate_report, view_all_logs
from api import fetch_vehicle_makes, fetch_vehicle_models
from utils import get_random_tip

# Streamlit page setup
st.set_page_config(page_title="EcoTracker", page_icon="🌱")

st.title("🌱 EcoTracker: Personal Carbon Footprint Analyzer")

# Sidebar menu
menu = ["Log Activities", "View Emission Report", "View All Logs", "Get Eco Tip"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Log Activities":
    st.header("🚗 Log Today's Activities")

    transport_km = st.number_input(
        "How many km did you travel today?", min_value=0.0, step=0.1
    )
    electricity_kwh = st.number_input(
        "How much electricity did you use (kWh)?", min_value=0.0, step=0.1
    )
    diet = st.selectbox(
        "What kind of diet?", ["vegan", "vegetarian", "mixed", "meat-heavy"]
    )

    makes = fetch_vehicle_makes()
    selected_model_id = None

    if makes:
        make_names = [make["data"]["attributes"]["name"] for make in makes]
        selected_make = st.selectbox("Select Vehicle Make", make_names)
        selected_make_id = makes[make_names.index(selected_make)]["data"]["id"]

        models = fetch_vehicle_models(selected_make_id)
        if models:
            model_options = [
                f"{model['data']['attributes']['name']} ({model['data']['attributes']['year']})"
                for model in models
            ]
            selected_model_text = st.selectbox("Select Vehicle Model", model_options)
            selected_model = models[model_options.index(selected_model_text)]
            selected_model_id = selected_model["data"]["id"]

    if st.button("Log Activity"):
        log_activities(transport_km, electricity_kwh, diet, selected_model_id)
        st.success("✅ Activity logged successfully!")

elif choice == "View Emission Report":
    generate_report()

elif choice == "View All Logs":
    view_all_logs()

elif choice == "Get Eco Tip":
    st.header("🌿 Eco Tip of the Day")
    st.info(get_random_tip())
