# Traverse tuples

students = ("John", "Alice", "Bob", "Wasim")

print("Using for loop")
print("--------------")

for student in students:
    print(student)

print("\nUsing enumerate()")
print("-----------------")

for roll, student in enumerate(students, start = 1):
    print(f"{roll}. {student}")

print("\nUsing while loop")
print("----------------")

index = 0

while index < len(students):
    print(students[index])
    index += 1
