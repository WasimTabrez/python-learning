# Count word frequency in a sentence

sentance = input("Enter a sentence: ")

words = sentance.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print()

for word, count in frequency.items():
    print(word, ":", count)
