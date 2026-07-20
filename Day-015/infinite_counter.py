# Infinite generator example

def counter():

    number = 1

    while True:
        yield number
        number += 1


generator = counter()

for _ in range(10):
    print(next(generator))
