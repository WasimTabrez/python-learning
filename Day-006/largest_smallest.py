# Find the largest and smallest elements in a list

numbers = []

count = int(input("How many numbers? "))

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# # With Built-in Functions
# print("\nLargest :", max(numbers))
# print("Smallest :", min(numbers))

largest = numbers[0]
smallest = numbers[0]

# Start from the second element because the first element is already used to initialize largest and smallest.
for number in numbers[1:]:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("\nLargest :", largest)
print("Smallest :", smallest)

