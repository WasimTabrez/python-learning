# Salary Tax Calculator

salary = float(input("Enter annual salary: "))

if salary <= 300000:
    tax = 0
elif salary <= 700000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.10
else:
    tax = salary * 0.20

print("Estimated tax:", tax)