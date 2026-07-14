# Remove duplicate elements from a list using a set

numbers = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original List:")
print(numbers,"\nWith sorted:",sorted(numbers))

unique_numbers = list(set(numbers))

print("\nAfter Removing Duplicates:")
print(unique_numbers,"\nWith sorted:",sorted(unique_numbers))
