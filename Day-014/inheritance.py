# Demonstrate single inheritance

class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):

    def study(self):
        print(f"{self.name} is studying.")


student = Student("Wasim")

student.display()
student.study()
