# Demonstrate ^ and $ Anchors

import re

text1 = "Python Programming"

text2 = "Programming in Python"

print("Starts with Python?")

print(bool(re.search(r"^Python", text1)))

print(bool(re.search(r"^Python", text2)))

print()

print("Ends with Python?")

print(bool(re.search(r"Python$", text1)))

print(bool(re.search(r"Python$", text2)))
