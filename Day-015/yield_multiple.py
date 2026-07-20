# Demonstrate multiple yield statements

def fruits():

    yield "Apple"
    yield "Banana"
    yield "Mango"
    yield "Orange"


generator = fruits()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
