# Demonstrate instance variables

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Wasim", 30)
student2 = Student("John", 25)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)
