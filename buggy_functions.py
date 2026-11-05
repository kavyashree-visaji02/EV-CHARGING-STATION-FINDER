
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # BUG: Degrees are used instead of radians.
    radius = 6371
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (math.sin(dlat / 2) ** 2
         + math.cos(lat1) * math.cos(lat2)
         * math.sin(dlon / 2) ** 2)
    return 2 * radius * math.asin(math.sqrt(a))


def find_nearest_charger(stations):
    # BUG: Selects the farthest station.
    available = [s for s in stations if s["available"]]
    return max(available, key=lambda s: s["distance"])


def reserve_charger(charger_id, chargers):
    # BUG: Allows duplicate reservations.
    if charger_id not in chargers:
        return "FAILED: Unknown charger"
    if chargers[charger_id]:
        return "SUCCESS: Reservation confirmed"
    return "FAILED: Charger unavailable"
