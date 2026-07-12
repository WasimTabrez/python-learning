# Return multiple values from a function

def divide(a, b):
    quotient = a // b
    remainder = a % b

    return quotient, remainder

q, r = divide(17, 5)

print("Quotient :", q)
print("Remainder:", r)
