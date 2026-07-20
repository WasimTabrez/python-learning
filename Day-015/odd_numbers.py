# Generate odd numbers

def odd_numbers(limit):

    for number in range(1, limit + 1, 2):
        yield number


for number in odd_numbers(20):
    print(number)
