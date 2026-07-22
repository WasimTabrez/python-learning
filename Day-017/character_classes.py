# Demonstrate Character Classes

import re

text = "Python123 Java456 C++789"

print("Digits:")
print(re.findall(r"\d", text))

print("\nLetters:")
print(re.findall(r"[A-Za-z]", text))

print("\nWords:")
print(re.findall(r"\w+", text))

print("\nSpaces:")
print(re.findall(r"\s", text))
