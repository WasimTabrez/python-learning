# Compare students enrolled in different subjects

python_students = {"Wasim", "John", "Alice", "Rahul"}
java_students = {"John", "Rahul", "David", "Rohit"}

print("Python Students:", python_students)
print("Java Students:", java_students)

print("\nStudents enrolled in both subjects")
print(python_students & java_students)
# print(python_students.intersection(java_students))

print("\nStudents enrolled only in Python")
print(python_students - java_students)
# print(python_students.difference(java_students))

print("\nStudents enrolled only in Java")
print(java_students - python_students)
# print(java_students.difference(python_students))

print("\nAll Students")
print(python_students | java_students)
# print(python_students.union(java_students))
