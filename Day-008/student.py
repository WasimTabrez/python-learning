# Store and display student information

student = {}

student["name"] = input("Enter Name: ")
student["age"] = int(input("Enter Age: "))
student["course"] = input("Enter Course: ")

print()

for key, value in student.items():
    print(key, ":", value)