# Find the symmetric difference between two sets

set1 = {"Python", "Java", "C++"}
set2 = {"Python", "AI", "Machine Learning"}

result = set1.symmetric_difference(set2)

print("Set 1", set1)
print("Set 2", set2)
print("Symmetric Difference:", result)
print(f"Symmetric Difference: {set1 ^ set2}, by using `^` operator")
