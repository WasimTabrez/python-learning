# calculates factorial of a number

def factorial(n):
    result = 1

    for i in range(n, 0, -1):
        result *= i

        
    return result

number = int(input("Enter number: "))
print("Factorial =",factorial(number))
