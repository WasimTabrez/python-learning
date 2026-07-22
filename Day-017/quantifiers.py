# Demonstrate Regex Quantifiers

import re

text = "Pythonnnn Python Pytho Pythonnn"

print("n+")
print(re.findall(r"Python+", text))

print("\nn*")
print(re.findall(r"Python*", text))

print("\nn?")
print(re.findall(r"Pythonn?", text))
