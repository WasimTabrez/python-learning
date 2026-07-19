# Demonstrate class variables

class Student:

    school = "ABC Public School"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name  :", self.name)
        print("School:", Student.school)
        print()


student1 = Student("Wasim")
student2 = Student("John")

student1.display()
student2.display()

print("Access using class:", Student.school)
