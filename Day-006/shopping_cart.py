# Store purchased items in a shopping cart

cart = []

count = int(input("How many items? "))

for i in range(count):
    item = input(f"Enter item {i + 1}: ")
    cart.append(item)

print("\nShopping Cart")
print("-------------")

for item in cart:
    print(item)