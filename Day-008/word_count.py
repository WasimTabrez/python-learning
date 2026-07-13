# Count word frequency in a sentence

sentance = input("Enter a sentence: ")

words = sentance.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print()

for word, frequency in count.items():
    print(word, ":", frequency)
