import random

# List of eco-friendly tips
ECO_TIPS = [
    "Use public transportation, bike, or walk whenever possible.",
    "Turn off lights and electronics when not in use to save energy.",
    "Eat more plant-based meals to lower your carbon footprint.",
    "Reduce, reuse, and recycle to minimize waste.",
    "Use energy-efficient appliances and LED light bulbs.",
    "Bring your own reusable bags when shopping.",
    "Buy local and seasonal produce to cut transport emissions.",
    "Carpool to work or school to reduce vehicle emissions.",
    "Avoid single-use plastics like straws and cups.",
    "Support renewable energy initiatives in your community.",
    "Collect rainwater for gardening instead of using tap water.",
    "Compost your food scraps to reduce landfill waste.",
    "Use a programmable thermostat to save on heating and cooling.",
    "Choose eco-friendly cleaning products.",
    "Plant trees or support reforestation projects."
]

def get_random_tip():
    """Return a randomly selected eco tip."""
    return random.choice(ECO_TIPS)
