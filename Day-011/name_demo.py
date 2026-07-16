# Demonstrate the `__name__` variable

print("__name__=", __name__)

def display():
    print("Display Function")

if __name__ == "__main__":
    print("This file is executed directly.")
    display()
else:
    print("This file is imported.")
