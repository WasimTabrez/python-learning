# Remove elements using `remove()` and `pop()`

cities = ["Delhi", "Mumbai", "Chennai", "Bangalore"]

print("Original List:", cities)

cities.remove("Mumbai")
print("\nAfter remove():", cities)

removed = cities.pop()

print("Removed:", removed)
print("After pop():", cities)