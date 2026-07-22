# Split text using regex

import re

text = "Python,Java;C++:Go|Rust"

pattern = r"[,;:|]"

result = re.split(pattern, text)

print(result)
