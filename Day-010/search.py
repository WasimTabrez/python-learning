# Search for a substring in a string

text = input("Enter a sentence: ")

word = input("Enter word to search: ")

if word in text:
    print("Found")
    print("Index:", text.find(word))
else:
    print("Not Found")
