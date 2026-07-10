# finds the largest element in a list

def largest(numbers):
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    
    return largest


numbers = []

count = int(input("How many numbers? "))

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Largest Number =", largest(numbers))
