# Analyze text statistics

from collections import Counter

text = input("Enter a paragraph:\n\n")

characters = len(text)
words = text.split()
word_count = len(words)
sentences = text.count(".") + text.count("!") + text.count("?")

vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
digits = 0
special = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    if ch.islower():
        lowercase += 1
    if ch.isdigit():
        digits += 1
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif not ch.isspace():
        special += 1

longest = max(words, key = len) if words else ""
shortest = min(words, key = len) if words else ""

frequency = Counter(word.lower().strip(".,!?") for word in words)

most_word = ""
most_count = 0

if frequency:
    most_word, most_count = frequency.most_common(1)[0]

print("\n========== Analysis ==========\n")

print("Total Characters      :", characters)
print("Total Words           :", word_count)
print("Total Sentences       :", sentences)
print("Total Vowels          :", vowels)
print("Total Consonants      :", consonants)
print("Uppercase Letters     :", uppercase)
print("Lowercase Letters     :", lowercase)
print("Digits                :", digits)
print("Special Characters    :", special)
print("Longest Word          :", longest)
print("Shortest Word         :", shortest)
print("Most Frequent Word    :", most_word)
print("Frequency             :", most_count)
