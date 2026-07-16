def calculate_bonus():
    salary = float(input("Enter Salary: "))
    rating = int(input("Enter Rating (1-5): "))

    if rating >= 5:
        bonus = salary * 0.20
    elif rating == 4:
        bonus = salary * 0.15
    elif rating == 3:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    print(f"\nBonus = ₹{bonus:.2f}\n")
