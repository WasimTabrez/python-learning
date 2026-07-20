# Generate student records

def students():

    records = [
        {"roll": 101, "name": "Wasim", "marks": 95},
        {"roll": 102, "name": "John", "marks": 82},
        {"roll": 103, "name": "Alice", "marks": 91},
        {"roll": 104, "name": "David", "marks": 76}
    ]

    for student in records:
        yield student


for student in students():

    print(
        student["roll"],
        student["name"],
        student["marks"]
    )
