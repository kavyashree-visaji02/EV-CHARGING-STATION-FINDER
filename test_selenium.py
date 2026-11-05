
import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://127.0.0.1:5000"


class TestEVChargingFlow(unittest.TestCase):

    def test_search_and_reserve(self):
        options = Options()
        options.binary_location = "/usr/bin/google-chrome"
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

        try:
            driver.get(URL)
            wait = WebDriverWait(driver, 10)

            # Step 1: Find nearest charger
            search_button = wait.until(
                EC.element_to_be_clickable((By.ID, "search-btn"))
            )
            search_button.click()

            # Step 2: Verify charger appears
            station = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "station-result")
                )
            )
            self.assertIn("Nearest Charger:", station.text)

            # Step 3: Reserve charger
            reserve_button = wait.until(
                EC.element_to_be_clickable((By.ID, "reserve-btn"))
            )
            reserve_button.click()

            # Step 4: Verify confirmation
            message = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "reservation-message")
                )
            )
            self.assertIn(
                "SUCCESS: Reservation confirmed",
                message.text
            )

            # Step 5: Save evidence screenshot
            evidence = Path("selenium_reservation_success.png")
            driver.save_screenshot(str(evidence))
            print("Screenshot saved:", evidence.resolve())

        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()
