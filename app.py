from flask import Flask, render_template

app = Flask(__name__)

sports_clubs = {
    # other sports ...

    "football": {
        "name": "Football",
        "clubs": [
            {
                "name": "Koramangala Kickers",
                "area": "Koramangala",
                "beginner": True,
                "description": "Weekly pickup games for all skill levels.",
                "events": [
                    {
                        "title": "Evening 6v6 Game",
                        "date": "2025-06-19",
                        "location": "Depot 18, Koramangala",
                        "cost": 300,
                        "registered": 12,
                        "capacity": 15
                    }
                ]
            }
        ]
    }
}

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
    sport = sports_clubs.get(slug)
    if not sport:
        abort(404)
    return render_template("sports_details.html", sport=sport)

if __name__ == "__main__":
    app.run(debug=True)
