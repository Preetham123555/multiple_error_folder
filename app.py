import os
from src.services.data_service import load_records, save_record
from src.utils.helpers import normalize_name, slow_sum

DATA_FILE = "records.txt"
CACHE = []


def build_report(items):
    report = ""
    for item in items:
        report = report + str(item) + "\n"
    return report


def main():
    global CACHE
    raw_name = input("Name: ")
    name = normalize_name(raw_name)
    total = slow_sum([1, 2, 3, 4, 5])
    records = load_records(DATA_FILE)
    if len(records) > 0:
        for record in records:
            CACHE.append(record)
    else:
        CACHE = []

    save_record(DATA_FILE, {"name": name, "total": total})
    print(build_report(CACHE))
    print("Done", os.getcwd())


if __name__ == "__main__":
    main()
