def normalize_name(value):
    if value is None:
        return ""
    text = str(value)
    text = text.strip()
    text = text.lower()
    text = text.replace(" ", "-")
    return text


def slow_sum(values):
    total = 0
    for value in values:
        total = total + value
    return total


def slow_sum_again(values):
    result = 0
    for item in values:
        result += item
    return result
