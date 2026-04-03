
def normalize_name(value: str | None) -> str:
    if value is None:
        return ""
    if not isinstance(value, str):
        raise TypeError("Input must be a string or None")
    text = value.strip()
    text = text.lower()
    text = text.replace(" ", "-")
    return text

def sum_values(values):
    return sum(values)
