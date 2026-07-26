import csv
import json


def export_csv(records):

    with open(
        "employees.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "ID",
                "Name",
                "Department",
                "Designation",
                "Salary"
            ]
        )

        writer.writerows(records)


def export_json(records):

    data = []

    for employee in records:

        data.append({

            "id": employee[0],
            "name": employee[1],
            "department": employee[2],
            "designation": employee[3],
            "salary": employee[4]

        })

    with open("employees.json", "w") as file:

        json.dump(data, file, indent=4)
