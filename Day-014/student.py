# Student Management using OOP

class Student:

    school = "ABC Public School"

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        else:
            return "D"

    def display(self):
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Grade   :", self.grade())
        print("School  :", Student.school)
        print()


student1 = Student(101, "Wasim", 95)
student2 = Student(102, "Alice", 81)
student3 = Student(103, "John", 58)

student1.display()
student2.display()
student3.display()
