# Demonstrate commonly used dictionary methods

student = {
    "name": "Wasim",
    "age": 28,
    "course": "Python"
}

print(student.keys())

print(student.values())

print(student.items())

student.update({"city": "Bangalore"})
print(student)

student.setdefault("country", "India")
print(student)

copy_student = student.copy()
print(copy_student)

student.clear()
print(student)
print(copy_student)