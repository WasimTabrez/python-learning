# Find common elements or intersection of two sets

set1 = {"Python", "Java", "C++", "AI"}
set2 = {"Python", "AI", "Machine Learning"}

result = set1.intersection(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection:", result)
print(f"Intersection: {set1 & set2}, by using `&` operator")