# Handle StopIteration exception

numbers = [10, 20]

iterator = iter(numbers)

try:
    while True:
        print(next(iterator))

except StopIteration:
    print("Iteration completed.")
