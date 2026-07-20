# Generate even numbers

def even_numbers(limit):

    for number in range(2, limit + 1, 2):
        yield number


for number in even_numbers(20):
    print(number)
