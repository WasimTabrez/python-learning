# Demonstrate special (dunder) methods

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} ({self.marks})"

    def __len__(self):
        return len(self.name)


student = Student("Wasim", 95)

print(student)
print("Length:", len(student))
