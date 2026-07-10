# counts vowels in a string

def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1
    
    return count


text = input("Enter a string: ")
print("Number of vowels =",count_vowels(text))
