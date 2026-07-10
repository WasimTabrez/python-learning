# finds the maximum of three numbers

def max_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest



x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
print(f"Maximum: {max_of_three(x, y, z)}")
