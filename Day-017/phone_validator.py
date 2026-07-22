# Validate Indian Mobile Number

import re

phone = input("Enter Mobile Number: ").strip()

pattern = r"^[6-9]\d{9}$"

if re.fullmatch(pattern, phone):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
