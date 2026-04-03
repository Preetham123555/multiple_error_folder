
import os
from src.services.data_service import load_records, save_record
from src.utils.helpers import normalize_name, sum_values

DATA_FILE = "records.txt"

class Cache:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_report(self):
        return "
".join(map(str, self.items))

def main():
    cache = Cache()
    raw_name = input("Name: ")
    name = normalize_name(raw_name)
    total = sum_values([1, 2, 3, 4, 5])
    records = load_records(DATA_FILE)
    if records:
        cache.items = records
    else:
        cache.items = []

    save_record(DATA_FILE, {"name": name, "total": total})
    print(cache.get_report())
    print("Done", os.getcwd())

if __name__ == "__main__":
    main()
