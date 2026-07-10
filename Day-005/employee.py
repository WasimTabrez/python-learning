# Display employee details using function parameters

def employee_details(name, age, company, salary):
    print("\nEmployee Details")
    print("------------------")
    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"Company : {company}")
    print(f"Salary  : {salary}")

name = input("Enter Name: ")
age = int(input("Enter Age: "))
company = input("Enter Company: ")
salary = float(input("Enter Salary: "))

employee_details(name, age, company, salary)