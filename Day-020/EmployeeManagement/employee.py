# Employee Class

class Employee:

    def __init__(
        self,
        employee_id,
        name,
        department,
        designation,
        salary
    ):

        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary

    def to_tuple(self):

        return (
            self.employee_id,
            self.name,
            self.department,
            self.designation,
            self.salary
        )

    def __str__(self):

        return (
            f"ID          : {self.employee_id}\n"
            f"Name        : {self.name}\n"
            f"Department  : {self.department}\n"
            f"Designation : {self.designation}\n"
            f"Salary      : ₹{self.salary:,.2f}"
        )
