# Calculate the total shopping bill using functions

def calculate_bill(price, quantity):
    return price * quantity

item = input("Enter item name: ")
price = float(input("Enter item price: "))
qunatity = int(input("Enter quantity: "))

total = calculate_bill(price, qunatity)

print("\nShopping Bill")
print("----------------")
print(f"Item      : {item}")
print(f"Price     : ₹{price:.2f}")
print(f"Quantity  : {qunatity}")
print(f"Total Bill: ₹{total:.2f}")