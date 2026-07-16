def calculate_tax():
    income = float(input("Enter Annual Income: "))

    if income <= 700000:
        tax = 0
    elif income <= 1200000:
        tax = income * 0.10
    else:
        tax = income * 0.20

    print(f"\nEstimated Tax = ₹{tax:.2f}\n")
