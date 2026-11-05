
# EV Charging Station Finder
# Reservation management prototype

chargers = {
    "EV001": True,
    "EV002": True,
    "EV003": False
}

def reserve_charger(charger_id):
    if charger_id not in chargers:
        return "FAILED: Charger not found"

    if not chargers[charger_id]:
        return "FAILED: Charger unavailable"

    chargers[charger_id] = False
    return "SUCCESS: Reservation confirmed"


if __name__ == "__main__":
    print("First booking:", reserve_charger("EV001"))
    print("Duplicate booking:", reserve_charger("EV001"))
    print("Unavailable charger:", reserve_charger("EV003"))
