# Raise Exception Demo

salary = float(input("Enter Salary: "))

if salary < 0:
    raise ValueError("Salary cannot be negative.")

print("Salary =", salary)
