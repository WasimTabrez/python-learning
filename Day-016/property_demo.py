# Demonstrate @property


class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value < 0:
            print("Salary cannot be negative.")
        else:
            self._salary = value

    @salary.deleter
    def salary(self):
        print("Salary deleted.")
        del self._salary


employee = Employee(50000)

print(employee.salary)

employee.salary = 65000

print(employee.salary)

del employee.salary
