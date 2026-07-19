# Demonstrate @classmethod

class Student:

    school = "ABC Public School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    def display(self):
        print(f"Name   : {self.name}")
        print(f"School : {Student.school}")
        print()


student1 = Student("Wasim")
student2 = Student("John")

student1.display()
student2.display()

Student.change_school("XYZ International School")

student1.display()
student2.display()
