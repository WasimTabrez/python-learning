# Calculate the sum and average of list elements

numbers = []

count = int(input("How many numbers? "))

for i in range(count):
    number = int(input(f"Enter nubmer {i + 1}: "))
    # numbers.extend([number]) # Approach 1: Create a list from user input.
    # numbers.insert(i, number) # Approach 2: Create a list from user input.
    numbers.append(number) # Approach 3: Create a list from user input.

# # with Built-in Functions
# total = sum(numbers)
# average = total / len(numbers)

total = 0
average = 0

for i in numbers:
    total += i

average = total / count

print("\nNumbers :", numbers)
print("Sum  :", total)
print("Average :", average)