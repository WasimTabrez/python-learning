# reverses a string

def reverse_string(s):
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str


text = input("Enter a string: ")
print(f"Reversed: {reverse_string(text)}")
