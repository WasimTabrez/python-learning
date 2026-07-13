# Remove elements using `pop()`, `del`, and `popitem()`

student = {
    "name": "Wasim",
    "age": 28,
    "course": "Python"
}

print(student)
student.pop("course")
print(student)

student["city"] = "Bangalore"

print(student)
del student["city"]
print(student)

student.popitem()
print(student)
