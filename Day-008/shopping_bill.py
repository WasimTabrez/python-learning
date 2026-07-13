# Calculate the total shopping bill

items = {
    "Rice": 500,
    "Oil": 250,
    "Sugar": 100,
    "Milk": 60
}

total = 0

print("Shopping Bill")
print("-------------")

for item, price in items.items():
    print(item, ":", price)
    total += price

print("-------------")
print("Total :", total)