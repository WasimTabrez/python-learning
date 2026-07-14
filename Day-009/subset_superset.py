# Check subset and superset relationships

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print("Set 1:", set1)
print("Set 2:", set2)

print("\nBy using .issubset(), .issuperset())")

print("Is Set1 subset of Set2?", set1.issubset(set2))
print("Is Set2 superset of Set1?", set2.issuperset(set1))

print("Is Set2 subset of Set1?", set2.issubset(set1))
print("Is Set1 superset of Set2?", set1.issuperset(set2))

print("\n\nBy using `<=`(issubset), `>=`(issuperset)")
print(f"Is Set1 subset of Set2? {set1 <= set2}")
print(f"Is Set2 superset of Set1? {set2 >= set1}")

print(f"Is Set2 subset of Set1? {set2 <= set1}")
print(f"Is Set1 superset of Set2? {set1 >= set2}")