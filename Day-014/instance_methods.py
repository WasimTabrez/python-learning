# Demonstrate instance methods

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Marks:", self.marks)
        print()


student1 = Student("Wasim", 95)
student2 = Student("Alice", 88)

student1.display()
student2.display()
