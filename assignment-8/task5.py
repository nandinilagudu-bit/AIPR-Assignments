from datetime import datetime

def convert_date_format(date_str):
    if not isinstance(date_str, str):
        return "Invalid input"
    
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        return "Invalid input"


# ------------------------------
# Test Cases
# ------------------------------

test_dates = [
    "2023-10-15",
    "2000-01-01",
    "1999-12-31",
    "2024-02-29",
    "2023-07-09",
    "0010-05-05",

    "2023/10/15",
    "15-10-2023",
    "20231015",
    "2023-15-10",
    "2023-02-30",
    "abcd-ef-gh",
    "",

    None,
    12345,
    ["2023-10-15"]
]

for d in test_dates:
    print(f"{d} → {convert_date_format(d)}")
