# Find the difference between two sets

set1 = {"Python", "Java", "C++", "AI"}
set2 = {"Python", "AI", "Machine Learning"}

result = set1.difference(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Difference:", result)
print(f"Difference: {set1 - set2}, by using `-` operator")