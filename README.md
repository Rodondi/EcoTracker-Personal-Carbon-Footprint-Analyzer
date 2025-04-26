
# 🌱 EcoTracker: Personal Carbon Footprint Analyzer

---

## 📋 Project Overview

**EcoTracker** is a lightweight personal carbon footprint analyzer that helps individuals understand, track, and reduce their daily environmental impact.  
By logging simple activities like transportation, electricity usage, and diet choices, users receive real-time feedback on their CO₂ emissions and practical eco-friendly tips.

✅ **Problem It Solves:**
- Lack of awareness about daily carbon emissions
- No simple tool to track activities related to transport, energy, and diet
- Motivates greener lifestyle changes with actionable tips

✅ **Key Features:**
- 🌍 Log daily activities (km traveled, kWh used, diet type)
- 📈 View emission trends and reports over time
- 📋 See all logged eco-activities nicely printed
- 🌿 Get a random eco-friendly tip every day
- 🧩 Connected to Carbon Interface API for real vehicle emission estimates
- 🛜 Works offline with local database (SQLite)
- 💻 Streamlit web app interface for easy and beautiful use

---

## 🚀 How to Run EcoTracker

You can run EcoTracker **locally** on any computer that has Python installed.  
Here’s how:

---

### ⚙️ 1. Clone the Project

```bash
git clone https://github.com/Rodondi/EcoTracker-Personal-Carbon-Footprint-Analyzer.git
cd EcoTracker-Personal-Carbon-Footprint-Analyzer
```

---

### ⚙️ 2. Set Up Python Environment

It’s recommended to use a virtual environment:

```bash
# Create a virtual environment
python -m venv eco-env

# Activate the virtual environment
# On Windows:
eco-env\Scripts\activate

# On Mac/Linux:
source eco-env/bin/activate
```

---

### ⚙️ 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

### ⚙️ 4. Setup .env File (API Key)

Create a `.env` file in the root folder with your Carbon Interface API Key:

```
CARBON_INTERFACE_API_KEY=your_api_key_here
```
*(Sign up at [carboninterface.com](https://www.carboninterface.com/) to get your free API key.)*

---

### ⚙️ 5. Run the App

Launch the Streamlit web application:

```bash
streamlit run streamlit_app.py
```

✅ A browser window will open automatically at `http://localhost:8501` where you can start using EcoTracker!

---

## 📦 Project Structure

| File/Folder | Purpose |
|:---|:---|
| `main.py` | CLI version (optional, legacy) |
| `streamlit_app.py` | Main Streamlit Web App |
| `tracker.py` | Handles activity logging |
| `report.py` | Generates reports and views logs |
| `utils.py` | Provides eco-friendly tips |
| `database.py` | Sets up the SQLite database |
| `requirements.txt` | List of all Python packages needed |
| `.env` | Stores your API key securely |
| `data/eco_tracker.db` | SQLite database to store user logs |

---

## 🧠 Technologies Used

- Python
- Streamlit
- SQLite (local database)
- Requests (API calls)
- dotenv (for environment variables)
- Matplotlib (for plotting reports)

---

## 🌟 Final Notes

- EcoTracker works both **online (with API)** and **offline (using fallback estimates)**.
- User data is **stored locally**, ensuring **privacy**.
- The app is designed to be **lightweight**, **fast**, and **motivational** for eco-conscious living.

---
  
# 🚀 Let's Track for a Greener Tomorrow! 🌍🌱
