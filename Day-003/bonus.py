# Employee Bonus System

name = input("Enter Name: ")
experience = float(input("Enter Experience: "))
salary = float(input("Enter annual Salary: "))
rating = float(input("Enter Rating: "))

# checked highest-first: a 4.5 rating also satisfies >=4 and >=3,
# so order determines which bonus tier wins
if rating >= 4.5:
    Bonus = 20
elif rating >= 4:
    Bonus = 15
elif rating >= 3:
    Bonus = 10
else:
    Bonus = 0
    print("No Bonus")

print()
print(f"Employee Name : {name}")
print(f"Salary : {salary}")
print(f"Bonus : {Bonus}%")
print(f"Final Salary : {salary * (1 + Bonus / 100)}")