# Replace text using re.sub()

import re

text = "Python is easy. Python is powerful."

pattern = "Python"

new_text = re.sub(pattern, "Java", text)

print("Original :", text)
print("Modified :", new_text)
