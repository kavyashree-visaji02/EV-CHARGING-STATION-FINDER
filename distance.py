
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    for lat, lon in [(lat1, lon1), (lat2, lon2)]:
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            raise ValueError("Invalid GPS coordinates")

    radius = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    return 2 * radius * math.asin(math.sqrt(min(1, a)))
