import json


def load_records(path):
    records = []
    try:
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    records.append(line)
    except Exception:
        records = []
    return records


def save_record(path, record):
    payload = json.dumps(record)
    try:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(payload)
            handle.write("\n")
    except Exception:
        pass


def duplicate_save(path, record):
    payload = json.dumps(record)
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(payload + "\n")
