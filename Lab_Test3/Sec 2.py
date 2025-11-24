SENIOR_AGE = 60

def parse_input(s: str):
    """Parse input like 'Ayesha:30 years;John:45 years;...' into dict name->age.
    This implementation avoids imports and regex by scanning characters.
    """
    entries = [e.strip() for e in s.split(';') if e.strip()]
    result = {}
    for entry in entries:
        parts = entry.split(':', 1)
        if len(parts) != 2:
            continue
        name = parts[0].strip()
        age_part = parts[1].strip()
        # extract first contiguous sequence of digits from age_part
        digits = ''
        for ch in age_part:
            if ch.isdigit():
                digits += ch
            elif digits:
                # stop after we've collected the first number
                break
        if not digits:
            continue
        age = int(digits)
        result[name] = age
    return result

def classify(age: int) -> bool:
    """Return True if senior (age >= SENIOR_AGE)."""
    return age >= SENIOR_AGE

def print_classifications(data: dict):
    # sort by age descending, tie -> name ascending
    items = sorted(data.items(), key=lambda kv: (-kv[1], kv[0]))
    for name, age in items:
        status = 'a Senior.' if classify(age) else 'not a Senior.'
        print(f"{name} is {status}")

def find_eldest_youngest(data: dict):
    if not data:
        return None, None
    items = list(data.items())
    eldest = max(items, key=lambda kv: kv[1])
    youngest = min(items, key=lambda kv: kv[1])
    return eldest, youngest

s = input("Enter Name:Age years (entries separated by ';'):\n").strip()
data = parse_input(s)
if not data:
    print("No valid entries found.")
else:
    print()
    print_classifications(data)
    eldest, youngest = find_eldest_youngest(data)
    if eldest:
        print()
        print(f"The eldest person is {eldest[0]}, aged {eldest[1]} years.")
    if youngest:
        print(f"The youngest person is {youngest[0]}, aged {youngest[1]} years.")
# Ayesha:30 years;John:45 years;Mary:67 years;Alice:30 years;Robert:62 years