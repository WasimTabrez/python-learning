# Custom iterator for employee records

class EmployeeIterator:

    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.employees):
            raise StopIteration

        employee = self.employees[self.index]
        self.index += 1

        return employee


employees = [
    {"id": "EMP001", "name": "Wasim", "salary": 85000},
    {"id": "EMP002", "name": "John", "salary": 70000},
    {"id": "EMP003", "name": "Alice", "salary": 90000}
]

iterator = EmployeeIterator(employees)

for employee in iterator:
    print(employee)
