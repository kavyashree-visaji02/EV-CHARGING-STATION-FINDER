
import unittest
import reservation


class TestReservation(unittest.TestCase):

    def setUp(self):
        reservation.chargers = {
            "EV001": True,
            "EV002": False
        }

    def test_successful_reservation(self):
        result = reservation.reserve_charger("EV001")
        self.assertEqual(
            result,
            "SUCCESS: Reservation confirmed"
        )

    def test_duplicate_reservation(self):
        reservation.reserve_charger("EV001")
        result = reservation.reserve_charger("EV001")
        self.assertEqual(
            result,
            "FAILED: Charger unavailable"
        )

    def test_unavailable_charger(self):
        result = reservation.reserve_charger("EV002")
        self.assertEqual(
            result,
            "FAILED: Charger unavailable"
        )

    def test_unknown_charger(self):
        result = reservation.reserve_charger("EV999")
        self.assertEqual(
            result,
            "FAILED: Charger not found"
        )


if __name__ == "__main__":
    unittest.main()
