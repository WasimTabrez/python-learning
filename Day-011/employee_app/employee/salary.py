def calculate_salary():
    basic = float(input("Enter Basic Salary: "))

    hra = basic * 0.20
    da = basic * 0.10

    gross = basic + hra + da

    print("\nSalary Details")
    print("----------------")
    print(f"Basic Salary : ₹{basic:.2f}")
    print(f"HRA          : ₹{hra:.2f}")
    print(f"DA           : ₹{da:.2f}")
    print(f"Gross Salary : ₹{gross:.2f}\n")
