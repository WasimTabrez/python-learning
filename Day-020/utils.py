# Utility Functions


def line():

    print("=" * 70)


def title(text):

    line()

    print(text.center(70))

    line()


def pause():

    input("\nPress Enter to Continue...")


def display_students(records):

    if not records:

        print("No Records Found.")

        return

    line()

    print(

        f"{'ID':<6}"

        f"{'NAME':<20}"

        f"{'AGE':<8}"

        f"{'COURSE':<20}"

        f"{'MARKS'}"

    )

    line()

    for student in records:

        print(

            f"{student[0]:<6}"

            f"{student[1]:<20}"

            f"{student[2]:<8}"

            f"{student[3]:<20}"

            f"{student[4]}"

        )

    line()


def menu():

    print()

    print("1. Add Student")

    print("2. Search Student")

    print("3. Update Student")

    print("4. Delete Student")

    print("5. Display Students")

    print("6. Export CSV")

    print("7. Export JSON")

    print("8. Reports")

    print("9. Exit")
