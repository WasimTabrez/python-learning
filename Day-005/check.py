





# # electricity_bill.py
# # Calculate Electricity Bill
# def calculate_bill(units):
#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = (100 * 5) + ((units - 100) * 7)
#     else:
#         bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

#     return bill

# if __name__ == "__main__":
#     units = int(input("Enter electricity units consumed: "))
#     print("Electricity Bill = ₹",calculate_bill(units))






# # largest_number.py
# # Find Largest Element in a List
# def largest(numbers):
#     # return max(numbers)
#     largest = numbers[0]
#     for number in numbers[1:]:
#         if number > largest:
#             largest = number
    
#     return largest


# if __name__ == "__main__":
#     numbers = []

#     count = int(input("How many numbers? "))

#     for i in range(count):
#         number = int(input(f"Enter number {i + 1}: "))
#         numbers.append(number)

#     print("Largest Number =", largest(numbers))









# # count_vowels.py
# # Count Vowels
# def count_vowels(text):
#     count = 0

#     for char in text.lower():
#         if char in "aeiou":
#             count += 1
    
#     return count


# if __name__ == "__main__":
#     text = input("Enter a string: ")
#     print("Number of vowels =",count_vowels(text))



# # reverse_string.py
# # Reverse a String
# def reverse_string_manual(text):
#     result = ""
#     for ch in text:
#         result = ch + result   # prepend each character
#     # for i in range(len(text)):
#     #     result = text[i] + result   # prepend each character
#     return result

# def reverse(text):
#     return text[::-1]

# text = input("Enter a string: ")

# print("Reversed String:", reverse(text))
# print(reverse_string_manual(text))   # "olleh"

# # factorial
# def factorial(n):
#     result = 1

#     for i in range(n, 0, -1):
#         print(i)
#         result *= i

        
#     return result

# number = int(input("Enter number: "))
# print("Factorial =",factorial(number))
    






# # bonus.py
# # Calculate Employee Bonus
# def calculate_bonus(salary):
#     if salary >= 100000:
#         bonus = salary * 0.20
#     elif salary >= 500000:
#         bonus = salary * 0.10
#     else:
#         bonus = salary * 0.05
    
#     return bonus

# salary = float(input("Enter Salary: "))

# bonus = calculate_bonus(salary)

# print(f"Bonus = ₹{bonus}")



# # simple_interest.py
# # Calculate Simple Interest
# # SI = (P * R * T) / 100

# def simple_interest(principal, rate, time):
#     return principal * rate * time / 100

# principal = float(input("Enter Principal Amount: "))
# rate = float(input("Enter Interest Rate (%): "))
# time = float(input("Enter Time (Years): "))

# interest = simple_interest(principal, rate, time)

# print(f"Simple Interest = ₹{interest}")
# print("Simple Interest = ₹", interest)






# # even_odd.py
# # Check Even or Odd
# def is_even(number):
#     return number % 2 == 0

# number = int(input("Enter a number: "))

# if is_even(number):
#     print(number, "is Even")
# else:
#     print(number, "is Odd")





# maximum.py
# Find the Maximum of Three Numbers
# def maximum(a, b, c):
#     if a > b and a > c:
#         max = a
#     elif b > c:
#         max = b
#     else:
#         max = c

#     return max


# print(maximum(4, 1, 2))

# print(max(4, 1, 2))



# # add.py
# # Add Two Numbers
# def add(a, b):
#     return a + b

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Sum =", add(num1,num2))















# # shopping_bill.py
# # Calculate the total shopping bill using functions
# def calculate_bill(price, quantity):
#     return price * quantity

# item = input("Enter item name: ")
# price = float(input("Enter item price: "))
# qunatity = int(input("Enter quantity: "))

# total = calculate_bill(price, qunatity)

# print("\nShopping Bill")
# print("----------------")
# print(f"Item      : {item}")
# print(f"Price     : ₹{price:.2f}")
# print(f"Quantity  : {qunatity}")
# print(f"Total Bill: ₹{total:.2f}")




# # prime.py
# # Check whether a number is prime using a function
# def is_prime(number):
#     if number < 2:
#         return False
    
#     for i in range(2, int(number ** .5) + 1):
#         if number % i == 0:
#             return False
        
#     return True

# number = int(input("Enter a number: "))

# if is_prime(number):
#     print(number, " is a Prime Number")
# else:
#     print(number," is NOT a Prime Number")

# # factorial.py
# # Find the factorial of a number using a function
# def factorial(n):
#     result = 1

#     for i in range(n, 0, -1): # range(1, n+1):
#         result *= i

#     return result

# number = int(input("Enter a number: "))

# print("Factorial =", factorial(number))






# # area.py
# # Calculate the area of a rectangle using a function

# def rectangel_area(length, width):
#     return length * width

# length = float(input("Enter length: "))
# width = float(input("Enter width: "))

# print("Area =",rectangel_area(length,width))





# # temperature.py
# # Convert Celsius to Fahrenheit using a function

# def celsius_to_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32

# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = celsius_to_fahrenheit(celsius)
# print(f"{celsius}°C = {fahrenheit:.2f}°F")




# # employee.py
# # Display employee details using function parameters

# def employee_details(name, age, company, salary):
#     print("\nEmployee Details")
#     print("------------------")
#     print(f"Name    : {name}")
#     print(f"Age     : {age}")
#     print(f"Company : {company}")
#     print(f"Salary  : {salary}")

# name = input("Enter Name: ")
# age = int(input("Enter Age: "))
# company = input("Enter Company: ")
# salary = float(input("Enter Salary: "))

# employee_details(name, age, company, salary)







# # calculator.py
# # Perform arithmetic operations using functions

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Division by zero is not allowed"
#     return a / b

# def modulus(a, b):
#     if b == 0:
#         return "Integer modulo by zero is not allowed"
#     return a % b

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("\nResults")
# print("----------")
# print("Addition:", add(num1, num2))
# print("Subtraction:", subtract(num1, num2))
# print("Multiplication:",multiply(num1, num2))
# print("Division:",divide(num1, num2))
# print("modulus:",modulus(num1, num2))
# print("division:",divide(num1, 0))
# print("modulus:",modulus(num1, 0))




# # greet.py
# # Create and call a simple function

# def greet():
#     print("Hello, Welcome to Python Functions!")

# greet()
    


# # Global Variables
# x = 50

# def test():
#     print(x)
 
# test()


# # Local Variables
# def test():
#     x = 100
#     print(x)

# test()



# # Keyword Arguments
# def employee(name, age, company):
#     print(name)
#     print(age)
#     print(company)

# employee(
#     company = "Sasken",
#     name = "Wasim",
#     age = 30
# )



# # Default Parameters
# def greet(name = "Guest"):
#     print(f"Hello {name}")

# greet()
# greet("Wasim")

# # Return Values
# def add(a, b):
#     return a + b

# result = add(10, 20)

# print(result)



# # Multiple Parameters - positional arguments
# def employee(name, age, salary):
#     print(name)
#     print(age)
#     print(salary)

# employee("Wasim", 30, 10000)


# # Function Parameters
# def greet(name):   # name: Parameter
#     print(f"Hello {name}")

# greet("Wasim")   # "Wasim": Argument

# # Creating Functions
# def greet():
#     print("Hello Python")

# # Calling function
# greet()

# # With functions
# def greet(name):
#     print(f"Hello {name}")

# greet("Wasim")
# greet("Ken")
# greet("John")



# # Without functions:
# print("Hellow Wasim")
# print("Hello Ken")
# print("Hello John")


# import sys
# #sys.path.append("../Exercises")
# import functions_practice 
# print("Wasim checking sys.path:",sys.path)
# print("Wasim checking functions_practice.__name__:",functions_practice.__name__)