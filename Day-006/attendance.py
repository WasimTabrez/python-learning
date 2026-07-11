# Store and display student attendance

students = []

count = int(input("Number of students: "))

for i in range(count):
    name = input(f"Student {i + 1}: ")
    students.append(name)

print("\nAttendance")
print("----------")

for roll, student in enumerate(students, start = 1):
    print(f"{roll}. {student}")