import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CARBON_INTERFACE_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

BASE_URL = "https://www.carboninterface.com/api/v1"

def fetch_vehicle_makes():
    """Fetch all vehicle makes."""
    response = requests.get(f"{BASE_URL}/vehicle_makes", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def fetch_vehicle_models(make_id):
    """Fetch all models for a specific vehicle make."""
    response = requests.get(f"{BASE_URL}/vehicle_makes/{make_id}/vehicle_models", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def select_vehicle_model():
    """Let user select a vehicle model and return its model ID."""
    makes = fetch_vehicle_makes()
    
    print("\nAvailable Vehicle Makes:")
    for idx, make in enumerate(makes[:5]):  # Show only first 5 makes
        name = make['data']['attributes']['name']
        print(f"{idx + 1}. {name}")

    choice = int(input("Select a make (1-5): ")) - 1
    selected_make_id = makes[choice]['data']['id']

    models = fetch_vehicle_models(selected_make_id)
    
    print(f"\nAvailable Models:")
    for idx, model in enumerate(models[:5]):  # Show only first 5 models
        model_name = model['data']['attributes']['name']
        model_year = model['data']['attributes']['year']
        print(f"{idx + 1}. {model_name} ({model_year})")

    model_choice = int(input("Select a model (1-5): ")) - 1
    selected_model_id = models[model_choice]['data']['id']

    return selected_model_id

def calculate_transport_emission(km):
    """Use selected model to calculate transport CO₂ emissions."""
    try:
        model_id = select_vehicle_model()
        if model_id is None:
            print("Using fallback estimate.")
            return round(km * 0.21, 2)
        
        data = {
            "type": "vehicle",
            "distance_unit": "km",
            "distance_value": km,
            "vehicle_model_id": model_id
        }
        response = requests.post(f"{BASE_URL}/estimates", headers=HEADERS, json=data)
        response.raise_for_status()
        carbon_kg = response.json()["data"]["attributes"]["carbon_kg"]
        return round(carbon_kg, 2)
    except Exception as e:
        print("API Error (transport):", e)
        return round(km * 0.21, 2)

def calculate_energy_emission(kwh):
    """Simple fallback energy emission calculator."""
    return round(kwh * 0.405, 2)
