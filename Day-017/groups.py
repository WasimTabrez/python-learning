# Demonstrate Capturing Groups

import re

text = "Date: 22-07-2026"

pattern = r"(\d{2})-(\d{2})-(\d{4})"

match = re.search(pattern, text)

if match:

    print("Day   :", match.group(1))

    print("Month :", match.group(2))

    print("Year  :", match.group(3))
