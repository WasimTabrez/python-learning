# Generate Fibonacci numbers

def fibonacci(limit):

    first = 0
    second = 1

    count = 0

    while count < limit:

        yield first

        first, second = second, first + second

        count += 1


generator = fibonacci(10)

for number in generator:
    print(number)
