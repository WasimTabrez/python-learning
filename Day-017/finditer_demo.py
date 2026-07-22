# Demonstrate re.finditer()

import re

text = "Python Java Python C++ Python"

pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(f"Found '{match.group()}' at index {match.start()} to {match.end()}")
