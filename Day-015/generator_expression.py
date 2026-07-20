# Demonstrate generator expressions

squares = (number ** 2 for number in range(1, 6))

for value in squares:
    print(value)
