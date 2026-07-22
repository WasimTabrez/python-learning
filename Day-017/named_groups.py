# Demonstrate Named Groups

import re

text = "Name: Wasim Age: 40"

pattern = r"Name:\s(?P<name>[A-Za-z]+)\sAge:\s(?P<age>\d+)"

match = re.search(pattern, text)

if match:

    print("Name :", match.group("name"))

    print("Age  :", match.group("age"))
