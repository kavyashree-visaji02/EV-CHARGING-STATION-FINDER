
import timeit
import statistics

# Manual version: straightforward reservation logic
def manual_reserve(chargers, charger_id):
    if charger_id not in chargers:
        return "FAILED: Charger not found"

    if not chargers[charger_id]:
        return "FAILED: Charger unavailable"

    chargers[charger_id] = False
    return "SUCCESS: Reservation confirmed"


# AI-generated comparison version
def ai_reserve(chargers, charger_id):
    if charger_id not in chargers:
        return "FAILED: Charger not found"

    if chargers[charger_id] is False:
        return "FAILED: Charger unavailable"

    chargers[charger_id] = False
    return "SUCCESS: Reservation confirmed"


def benchmark(func, iterations=100000, repeats=5):
    def task():
        chargers = {"EV001": True, "EV002": True, "EV003": False}
        func(chargers, "EV001")

    samples = timeit.repeat(task, number=iterations, repeat=repeats)
    return statistics.median(samples) / iterations * 1_000_000


def main():
    manual_time = benchmark(manual_reserve)
    ai_time = benchmark(ai_reserve)

    print("EV CHARGING STATION FINDER - L5.4")
    print("--------------------------------")
    print(f"Manual version: {manual_time:.4f} microseconds per call")
    print(f"AI version:     {ai_time:.4f} microseconds per call")

    print("\nREADABILITY COMPARISON")
    print("Manual: Explicit availability check")
    print("AI:     Direct comparison with False")
    print("Both versions use simple conditional logic")

    print("\nFUNCTIONAL VERIFICATION")
    for func in (manual_reserve, ai_reserve):
        chargers = {"EV001": True, "EV002": True, "EV003": False}
        results = [
            func(chargers, "EV001"),
            func(chargers, "EV001"),
            func(chargers, "EV003"),
            func(chargers, "UNKNOWN"),
        ]
        print(f"{func.__name__}: {results}")


if __name__ == "__main__":
    main()
