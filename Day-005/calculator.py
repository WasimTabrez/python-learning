# basic calculator using separate functions per operation

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b



x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == "+":
    print(add(x, y))
elif op == "-":
    print(subtract(x, y))
elif op == "*":
    print(multiply(x, y))
elif op == "/":
    print(divide(x, y))
else:
    print("Invalid operation")
