# Export and Import Student Data

import csv
import json


def export_csv(filename, students):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Name",
            "Age",
            "Course",
            "Marks"
        ])

        writer.writerows(students)

    print("CSV Export Successful.")


def export_json(filename, students):

    data = []

    for student in students:

        data.append({

            "id": student[0],
            "name": student[1],
            "age": student[2],
            "course": student[3],
            "marks": student[4]

        })

    with open(filename, "w") as file:

        json.dump(data, file, indent=4)

    print("JSON Export Successful.")


def import_json(filename):

    with open(filename, "r") as file:

        data = json.load(file)

    return data
