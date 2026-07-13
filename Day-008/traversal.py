# Traverse a dictionary using loops

student = {
    "name": "Wasim",
    "age": 28,
    "course": "Python"
}

print(student)

print("\nKeys")

for key in student:
    print(key)

# .keys() method
# for key in student.keys():
#     print(key)

print("\nValues")

for value in student.values():
    print(value)

print("\nItems")

for key, value in student.items():
    print(key, ":", value)
