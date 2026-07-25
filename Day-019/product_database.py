# Product Inventory Database

import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")

connection.commit()


def add_product():

    product_id = int(input("Product ID: "))
    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    cursor.execute(
        "INSERT INTO products VALUES (?, ?, ?, ?)",
        (product_id, name, price, quantity)
    )

    connection.commit()

    print("Product Added Successfully.")


def display_products():

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    if products:

        print("\nInventory\n")

        for product in products:
            print(product)

    else:
        print("Inventory Empty")


while True:

    print("\n====== Product Inventory ======")
    print("1.Add Product")
    print("2.Display Products")
    print("3.Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        display_products()

    elif choice == "3":
        connection.close()
        break

    else:
        print("Invalid Choice")
