# Create a simple generator using yield

def numbers():

    yield 10
    yield 20
    yield 30


generator = numbers()

for number in generator:
    print(number)
