# Demonstrate re.search()

import re

text = "I love learning Python programming."

pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Match Found")
    print("Matched Text :", result.group())
    print("Start Index  :", result.start())
    print("End Index    :", result.end())
else:
    print("No Match")
