# Menu-driven Course Enrollment System using set

students = set()

def enroll_student():
    name = input("Enter Students: ").strip()

    if not name:
        print("Student name cannot be empty.\n")
        return

    if name in students:
        print(f"{name} is already enrolled.\n")
    else:
        students.add(name)
        print(f"{name} enrolled successfully.\n")

def remove_student():
    if not students:
        print("No students enrolled.\n")
        return

    name = input("Enter Student Name: ").strip()

    if name in students:
        students.remove(name)
        print(f"{name} removed successfully.\n")
    else:
        print(f"{name} not found.\n")


def display_students():
    if not students:
        print("No students enrolled.\n")
        return
    
    print("\nEnrolled Students")
    print("------------------")

    for roll, student in enumerate(sorted(students), start = 1):
        print(f"{roll}. {student}")
    
    print()

def check_student():
    if not students:
        print("No students enrolled.\n")
        return
    
    name = input("Enter Student Name: ").strip()

    if name in students:
        print(f"{name} is enrolled.\n")
    else:
        print(f"{name} is not enrolled.\n")

def count_students():
    if not students:
        print("No students enrolled.\n")
        return
    print(f"Total Students: {len(students)}\n")


def menu():
    while True:
        print("\n======= Course Enrollment System ========")
        print("1. Enroll Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Check Student")
        print("5. Count Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                enroll_student()
            case "2":
                remove_student()
            case "3":
                display_students()
            case "4":
                check_student()
            case "5":
                count_students()
            case "6":
                print("Thank you!")
                break
            case _:
                print("Invalid Choice.\n")

menu()
