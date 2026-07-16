# Generate random numbers and random choices

import random

print("Random Integer:", random.randint(1, 100))
print("Random Float:", random.random())

colors = ["Red", "Blue", "Green", "Black"]

print("Random Choice:", random.choice(colors))

random.shuffle(colors)

print("Shuffled List:", colors)