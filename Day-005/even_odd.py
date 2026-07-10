# checks whether a number is even or odd

def is_even(number):
    return number % 2 == 0

number = int(input("Enter a number: "))

if is_even(number):
    print(number, "is Even")
else:
    print(number, "is Odd")