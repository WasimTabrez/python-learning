# Extract Numbers from Text

import re

text = """
Laptop Price : 75000
Mobile Price : 35000
Discount : 5000
Order ID : 987654
"""

pattern = r"\d+"

numbers = re.findall(pattern, text)

print("Numbers Found:")

for number in numbers:
    print(number)
