# Employee Management using OOP

class Employee:

    company = "ABC Technologies"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def increment(self, amount):
        self.salary += amount

    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)
        print("Company     :", Employee.company)
        print()


employee1 = Employee("EMP001", "Wasim", 85000)
employee2 = Employee("EMP002", "John", 70000)

employee1.increment(5000)

employee1.display()
employee2.display()
