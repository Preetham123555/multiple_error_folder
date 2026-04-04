import json

def load_records(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            records = [json.loads(line.strip()) for line in handle if line.strip()]
        return records
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading records: {e}")
        return []

def save_record(path, record):
    try:
        with open(path, "a", encoding="utf-8") as handle:
            json.dump(record, handle)
            handle.write("\n")
    except Exception as e:
        print(f"Error saving record: {e}")