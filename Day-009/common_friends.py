# Find common friends between two users

wasim_friends = {"John", "Rahul", "Alice", "David"}
aman_friends = {"David", "Alice", "Kiran", "Rohit"}

print("Wasim's Friends:", wasim_friends)
print("Aman's Friends:", aman_friends)

common = wasim_friends.intersection(aman_friends)

print("\nCommon Friends:")
print(common)
