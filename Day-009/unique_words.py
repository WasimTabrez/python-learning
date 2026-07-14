# Display unique words from a sentence

sentence = input("Enter a sentence: ").lower()

words = sentence.split()

unique_words = set(words)

print("\nUnique Words:")

for word in sorted(unique_words):
    print(word)

