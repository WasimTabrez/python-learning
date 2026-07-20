# Compare generators and lists

import sys

numbers_list = [number for number in range(1000)]

numbers_generator = (number for number in range(1000))

print("List Size      :", sys.getsizeof(numbers_list), "bytes")
print("Generator Size :", sys.getsizeof(numbers_generator), "bytes")
