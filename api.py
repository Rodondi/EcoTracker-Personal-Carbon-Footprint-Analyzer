# api.py

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("CARBON_INTERFACE_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

BASE_URL = "https://www.carboninterface.com/api/v1"

def fetch_vehicle_makes():
    """Fetch all vehicle makes."""
    try:
        response = requests.get(f"{BASE_URL}/vehicle_makes", headers=HEADERS)
        response.raise_for_status()
        return response.json()  # Return full list
    except Exception as e:
        print("Error fetching vehicle makes:", e)
        return []

def fetch_vehicle_models(make_id):
    """Fetch all models for a specific vehicle make."""
    try:
        response = requests.get(f"{BASE_URL}/vehicle_makes/{make_id}/vehicle_models", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching vehicle models:", e)
        return []

def calculate_transport_emission(km, model_id=None):
    """Calculate CO₂ emissions for a distance and optional vehicle model."""
    if model_id is None:
        return round(km * 0.21, 2)  # fallback

    try:
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
        return round(km * 0.21, 2)  # fallback

def calculate_energy_emission(kwh):
    """Simple fallback energy emission calculator."""
    return round(kwh * 0.405, 2)