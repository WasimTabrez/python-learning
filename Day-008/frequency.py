# Count character frequency in a string

text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print()

for ch, count in frequency.items():
    print(ch, ":", count)