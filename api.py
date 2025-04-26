import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("CARBON_INTERFACE_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

BASE_URL = "https://www.carboninterface.com/api/v1"

def fetch_vehicle_makes():
    """Fetch available vehicle makes."""
    try:
        response = requests.get(f"{BASE_URL}/vehicle_makes", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching vehicle makes:", e)
        return []

def fetch_vehicle_models(make_id):
    """Fetch available vehicle models for a given make."""
    try:
        response = requests.get(f"{BASE_URL}/vehicle_makes/{make_id}/vehicle_models", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching vehicle models:", e)
        return []

def calculate_transport_emission(km, model_id=None):
    """Estimate CO₂ emissions for transport."""
    if model_id is None:
        return round(km * 0.21, 2)  # fallback estimate if no model selected

    try:
        payload = {
            "type": "vehicle",
            "distance_unit": "km",
            "distance_value": km,
            "vehicle_model_id": model_id
        }
        response = requests.post(f"{BASE_URL}/estimates", headers=HEADERS, json=payload)
        response.raise_for_status()
        carbon_kg = response.json()["data"]["attributes"]["carbon_kg"]
        return round(carbon_kg, 2)
    except Exception as e:
        print("API Error (transport):", e)
        return round(km * 0.21, 2)  # fallback estimate

def calculate_energy_emission(kwh):
    """Estimate CO₂ emissions from electricity usage."""
    return round(kwh * 0.405, 2)
