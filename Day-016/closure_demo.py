# Demonstrate closures

def multiplier(number):

    def multiply(value):
        return value * number

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))
