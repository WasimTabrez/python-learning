# Check whether a string is a palindrome

text = input("Enter text: ")

if text.lower() == text[::-1].lower():
    print("Palindrome")
else:
    print("Not Palindrome")
