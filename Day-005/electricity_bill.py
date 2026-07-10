# calculates electricity bill based on tiered unit rates


def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return bill


units = int(input("Enter electricity units consumed: "))
print("Electricity Bill = ₹",calculate_bill(units))
