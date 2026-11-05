
def predict_risk(complexity, changes, defects):
    score = 0

    if complexity >= 8:
        score += 3
    elif complexity >= 5:
        score += 2
    else:
        score += 1

    if changes >= 5:
        score += 3
    elif changes >= 3:
        score += 2
    else:
        score += 1

    if defects >= 3:
        score += 3
    elif defects >= 1:
        score += 2
    else:
        score += 1

    if score >= 8:
        return "HIGH"
    elif score >= 5:
        return "MEDIUM"
    return "LOW"


modules = [
    ("Reservation", 9, 6, 4),
    ("Charger Search", 7, 4, 2),
    ("Distance Calculation", 3, 1, 0),
    ("Web Application", 6, 3, 1),
    ("Station Data", 2, 1, 0),
]

print("EV CHARGING STATION FINDER - MODULE RISK REPORT")
print("-" * 60)

for name, complexity, changes, defects in modules:
    risk = predict_risk(complexity, changes, defects)
    print(f"{name:22} | Risk: {risk}")
