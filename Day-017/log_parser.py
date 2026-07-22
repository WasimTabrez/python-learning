# Extract Log Information using Regex

import re

logs = """
2026-07-22 09:30:10 INFO Server Started
2026-07-22 09:31:15 WARNING Low Memory
2026-07-22 09:32:18 ERROR Database Connection Failed
2026-07-22 09:35:22 INFO User Login Successful
2026-07-22 09:40:10 ERROR Invalid Password
"""

pattern = (
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>INFO|WARNING|ERROR)\s+"
    r"(?P<message>.+)"
)

matches = re.finditer(pattern, logs)

print("Parsed Log Entries")

print("-----------------------------")

for match in matches:

    print(f"Date    : {match.group('date')}")
    print(f"Time    : {match.group('time')}")
    print(f"Level   : {match.group('level')}")
    print(f"Message : {match.group('message')}")
    print("-" * 40)
