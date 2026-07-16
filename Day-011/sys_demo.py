# Demonstrate sys module

import sys

print("Python Version:")
print(sys.version)

print("\nPlatform:")
print(sys.platform)

print("\nPython Executable:")
print(sys.executable)

print("\nCommand-line Arguments:")

for index, arg in enumerate(sys.argv):
    print(f"{index}: {arg}")


# command "python3 sys_demo.py Hello Python 123"