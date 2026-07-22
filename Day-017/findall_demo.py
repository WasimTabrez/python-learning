# Demonstrate re.findall()

import re

text = "Python Java Python C++ Python"

pattern = "Python"

result = re.findall(pattern, text)

print("Occurrences:", result)
print("Count:", len(result))
