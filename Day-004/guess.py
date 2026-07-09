# Guess the Number

secret = 7

while True:
    guess = int(input("Guess: "))

    if guess == secret:
        print("Correct")
        break

    print("Try Again")
