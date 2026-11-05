
from distance import haversine_distance

def find_nearest_available(lat, lon, stations):
    available = [
        station for station in stations
        if station["available"]
    ]

    if not available:
        return None

    return min(
        available,
        key=lambda station: haversine_distance(
            lat, lon,
            station["lat"],
            station["lon"]
        )
    )
