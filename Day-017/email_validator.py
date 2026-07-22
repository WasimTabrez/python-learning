# Validate Email Address

import re

email = input("Enter Email Address: ").strip()

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")
