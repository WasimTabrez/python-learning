# Countdown generator

def countdown(start):

    while start > 0:
        yield start
        start -= 1

    yield "Lift Off!"


for value in countdown(5):
    print(value)
