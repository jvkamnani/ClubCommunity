from flask import Flask, render_template, abort
from dotenv import load_dotenv
import requests
import os

# Load .env config
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

HEADERS = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}"
}

app = Flask(__name__)

# ----------------------
# Utility Functions
# ----------------------

def get_all_clubs():
    url = f"{SUPABASE_URL}/rest/v1/clubs?select=*,sports(*)"
    res = requests.get(url, headers=HEADERS)
    return res.json()

def get_club_details(club_id, sport_name):
    detail_table_map = {
        "football": "football_club_details",
        "running": "running_club_details",
        "badminton": "badminton_club_details",
        "cycling": "cycling_club_details"
    }
    table = detail_table_map.get(sport_name.lower())
    if not table:
        return {}
    url = f"{SUPABASE_URL}/rest/v1/{table}?club_id=eq.{club_id}&select=*"
    res = requests.get(url, headers=HEADERS)
    return res.json()[0] if res.json() else {}

def get_events_for_club(club_id):
    url = f"{SUPABASE_URL}/rest/v1/events?club_id=eq.{club_id}&select=*"
    res = requests.get(url, headers=HEADERS)
    return res.json()

def get_clubs_by_sport(slug):
    # Step 1: Get the sport ID from name
    sport_res = requests.get(
        f"{SUPABASE_URL}/rest/v1/sports?name=eq.{slug.capitalize()}",
        headers=HEADERS
    )
    sport_data = sport_res.json()
    if not sport_data:
        return []

    sport_id = sport_data[0]["id"]

    # Step 2: Get clubs with that sport_id
    clubs_res = requests.get(
        f"{SUPABASE_URL}/rest/v1/clubs?sport_id=eq.{sport_id}&select=*,sports(*)",
        headers=HEADERS
    )
    return clubs_res.json()

# ----------------------
# Routes
# ----------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sports")
def sports():
    sports_list = [
        {"name": "Running", "slug": "running", "image": "img.icons8.png"},
        {"name": "Cycling", "slug": "cycling", "image": "icons8-cycling-50.png"},
        {"name": "Football", "slug": "football", "image": "icons8-football-50.png"},
        {"name": "Badminton", "slug": "badminton", "image": "icons8-badminton-50.png"},
    ]
    return render_template("sports.html", sports=sports_list)

@app.route("/sports/<slug>")
def sport_detail(slug):
    clubs = get_clubs_by_sport(slug)
    if not clubs:
        abort(404)
    return render_template("sports_details.html", clubs=clubs, sport_name=slug.capitalize())

@app.route("/clubs/<int:club_id>")
def view_club(club_id):
    # Fetch main club info
    club_url = f"{SUPABASE_URL}/rest/v1/clubs?id=eq.{club_id}&select=*,sports(*)"
    club_res = requests.get(club_url, headers=HEADERS)
    if not club_res.json():
        abort(404)

    club = club_res.json()[0]
    sport = club["sports"]["name"]

    # Fetch extra info + events
    details = get_club_details(club_id, sport)
    events = get_events_for_club(club_id)

    return render_template("club_details.html", club=club, details=details, events=events)

# ----------------------

if __name__ == "__main__":
    app.run(debug=True)
