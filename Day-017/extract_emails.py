# Extract Email Addresses

import re

text = """
Employees

Wasim : wasim@gmail.com
John  : john123@yahoo.com
Alice : alice.johnson@company.co.in
Support : support@test.org
"""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print("Email Addresses")

print("----------------")

for email in emails:
    print(email)
