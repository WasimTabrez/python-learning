# Remove elements from a set using remove(), discard(), and pop()

numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)

numbers.remove(20)
print("After remove(20):", numbers)

numbers.discard(100)  # No error if element doesn't exist
print('After discard(100):', numbers)

removed = numbers.pop() # Removes a random element

print("Removed:", removed)
print("Remaining Set:", numbers)


