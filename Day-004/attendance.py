# Student Attendance System

n = int(input("How many students? "))

students = []    # holds the name of the student

for _ in range(n):
    name = input("Enter student name: ")
    status = input(f"Is {name} Present or Absent? ")
    students.append((name, status))

print("\nAttendance Report")
for name, status in students:
    print(f"{name}\t{status}")
