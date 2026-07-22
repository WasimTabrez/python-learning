# Demonstrate re.compile()

import re

pattern = re.compile(r"\d+")

text = "There are 25 apples and 15 oranges."

matches = pattern.findall(text)

print("Numbers Found:", matches)
