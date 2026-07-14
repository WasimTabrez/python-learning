# Demonstrate immutable frozenset

fruits = frozenset({"Apple", "Banana", "Mango"})

print("Frozen Set:")
print(fruits)

print("\nLength:", len(fruits))

print("Is 'Apple' present?", "Apple" in fruits)

# The following statement will raise an AttributeError
# fruits.add("Orange") # AttributeError: 'frozenset' object has no attribute 'add'
