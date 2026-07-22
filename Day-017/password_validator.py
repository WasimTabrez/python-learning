# Validate Password Strength

import re

password = input("Enter Password: ")

pattern = (
    r"^(?=.*[a-z])"
    r"(?=.*[A-Z])"
    r"(?=.*\d)"
    r"(?=.*[@$!%*?&])"
    r"[A-Za-z\d@$!%*?&]{8,}$"
)

if re.fullmatch(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
