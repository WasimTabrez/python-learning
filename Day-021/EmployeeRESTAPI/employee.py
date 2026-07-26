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

    def to_dict(self):

        return {

            "id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "salary": self.salary

        }
