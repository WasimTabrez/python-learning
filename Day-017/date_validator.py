# Validate Date (DD-MM-YYYY)

import re

date = input("Enter Date (DD-MM-YYYY): ").strip()

pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"

if re.fullmatch(pattern, date):
    print("Valid Date Format")
else:
    print("Invalid Date Format")
