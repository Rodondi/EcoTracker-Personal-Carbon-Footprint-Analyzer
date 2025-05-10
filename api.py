
# api.py

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("CARBON_INTERFACE_API_KEY")

# Headers for API authentication
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Base URL for Carbon Interface API
BASE_URL = "https://www.carboninterface.com/api/v1"

def fetch_vehicle_makes():
    """Fetch a list of available vehicle makes from the Carbon Interface API."""
    try:
        response = requests.get(f"{BASE_URL}/vehicle_makes", headers=HEADERS)
        response.raise_for_status()
        return response.json()  # List of vehicle makes
    except Exception as e:
        print("Error fetching vehicle makes:", e)
        return []

def fetch_vehicle_models(make_id):
    """Fetch vehicle models for a given make ID."""
    try:
        response = requests.get(f"{BASE_URL}/vehicle_makes/{make_id}/vehicle_models", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching vehicle models:", e)
        return []

def calculate_transport_emission(km, model_id=None):
    """
    Calculate transport CO₂ emissions.
    Uses a real vehicle model ID if provided, otherwise falls back to a generic estimate.
    """
    if model_id is None:
        return round(km * 0.21, 2)  # fallback for generic vehicle

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
    """Estimate CO₂ emissions from electricity usage. Uses a constant emission factor."""
    return round(kwh * 0.405, 2)
