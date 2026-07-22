# Demonstrate re.match()

import re

text = "Python is an easy language."

pattern = "Python"

result = re.match(pattern, text)

if result:
    print("Match Found")
    print("Matched Text:", result.group())
else:
    print("No Match")
