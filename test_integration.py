
import unittest
import reservation
from charger_search import find_nearest_available
from stations import stations


class TestIntegration(unittest.TestCase):

    def setUp(self):
        # Reset the reservation stub before each test.
        reservation.chargers = {
            "EV001": True,
            "EV002": True,
            "EV003": False
        }

    def test_search_then_reserve_successfully(self):
        # Integration test 1: Search and reserve a charger.
        nearest = find_nearest_available(
            12.9716, 77.5946, stations
        )

        self.assertIsNotNone(nearest)

        charger_id = nearest["id"]
        result = reservation.reserve_charger(charger_id)

        self.assertIn("SUCCESS", result)
        self.assertFalse(reservation.chargers[charger_id])

    def test_duplicate_reservation_is_rejected(self):
        # Integration test 2: Search and attempt
        # to reserve the same charger twice.
        nearest = find_nearest_available(
            12.9716, 77.5946, stations
        )

        self.assertIsNotNone(nearest)

        charger_id = nearest["id"]

        first = reservation.reserve_charger(charger_id)
        second = reservation.reserve_charger(charger_id)

        self.assertIn("SUCCESS", first)
        self.assertIn("FAILED", second)


if __name__ == "__main__":
    unittest.main()
