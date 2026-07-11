# Menu-driven Student Management System using lists 

students = []

def add_student():
    name = input("Enter student name: ")

    students.append(name)

    print("Student added successfully.\n")

def remove_student():
    if len(students) == 0:
        print("No students available.\n")
        return

    name = input("Enter student name to remove: ")

    if name in students:
        students.remove(name)
        print("Student removed successfully.\n")
    else:
        print("Student not found.\n")

def search_student():
    if len(students) == 0:
        print("No students available.\n")
        return
    
    name = input("Enter student name to search: ")

    if name in students:
        print(f"{name} is present.\n")
    else:
        print(f"{name} is not present.\n")

def display_students():
    if len(students) == 0:
        print("No students available.\n")
        return
    
    print("\nStudent List")
    print("------------")

    for roll, student in enumerate(students, start = 1):
        print(f"{roll}. {student}")

    print()

def count_students():
    print("Total Students:", len(students))
    print()

def menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display Students")
        print("5. Count Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            count_students()
        elif choice == '6':
            print("Thank you!")
            break
        else:
            print("Invalid Choice.\n")

menu()