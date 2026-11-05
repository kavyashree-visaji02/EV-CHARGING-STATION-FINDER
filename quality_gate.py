
import subprocess
import sys

MIN_COVERAGE = 80

print("EV CHARGING STATION FINDER - QUALITY GATE")
print("-" * 45)

result = subprocess.run([
    sys.executable, "-m", "pytest",
    "test_reservation.py",
    "test_search.py",
    "test_integration.py",
    "--cov=reservation",
    "--cov=charger_search",
    "--cov=distance",
    f"--cov-fail-under={MIN_COVERAGE}",
    "--cov-report=term-missing",
])

if result.returncode == 0:
    print("\nQUALITY GATE: PASSED")
    print("Tests passed and coverage meets the threshold.")
else:
    print("\nQUALITY GATE: FAILED")
    print("Tests failed or coverage is below the threshold.")

sys.exit(result.returncode)
