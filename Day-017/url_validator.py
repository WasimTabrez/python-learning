# Validate Website URL

import re

url = input("Enter URL: ").strip()

pattern = (
    r"^(https?://)?"
    r"(www\.)?"
    r"[A-Za-z0-9-]+"
    r"(\.[A-Za-z]{2,})+$"
)

if re.fullmatch(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")
