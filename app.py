
from flask import Flask, render_template_string, request
from charger_search import find_nearest_available
from stations import stations
import reservation

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>EV Charging Station Finder</title>
</head>
<body>
    <h1>EV Charging Station Finder</h1>
    <p>Find and reserve your nearest available charger.</p>

    <form method="POST" action="/search">
        <button id="search-btn" type="submit">
            Find Nearest Charger
        </button>
    </form>

    {% if station %}
        <h2 id="station-result">
            Nearest Charger: {{ station["id"] }}
        </h2>
        <form method="POST" action="/reserve">
            <input type="hidden" name="charger_id"
                   value="{{ station['id'] }}">
            <button id="reserve-btn" type="submit">
                Reserve Charger
            </button>
        </form>
    {% endif %}

    {% if message %}
        <p id="reservation-message">{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

@app.route("/search", methods=["POST"])
def search():
    station = find_nearest_available(
        12.9716, 77.5946, stations
    )
    return render_template_string(PAGE, station=station)

@app.route("/reserve", methods=["POST"])
def reserve():
    charger_id = request.form.get("charger_id", "")
    message = reservation.reserve_charger(charger_id)
    return render_template_string(PAGE, message=message)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
