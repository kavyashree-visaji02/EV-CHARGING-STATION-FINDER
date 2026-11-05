
import unittest
from charger_search import find_nearest_available
from stations import stations


class TestChargerSearch(unittest.TestCase):

    def test_nearest_available(self):
        result = find_nearest_available(
            12.9700, 77.5900, stations
        )
        self.assertEqual(result["id"], "EV001")

    def test_no_available_stations(self):
        unavailable = [
            {
                "id": "EV004",
                "lat": 12.97,
                "lon": 77.59,
                "available": False
            }
        ]

        result = find_nearest_available(
            12.97, 77.59, unavailable
        )
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
