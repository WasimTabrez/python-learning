# Search Word in File

# filename = input("Enter File Name: ")
# word = input("Enter Word to Search: ")

# try:
#     with open(filename, "r") as file:

#         text = file.read()

#         if word.lower() in text.lower():
#             print("Word found.")
#         else:
#             print("Word not found.")

# except FileNotFoundError:
#     print("File not found.")

# shows how many times the word appears and on which lines

filename = input("Enter File Name: ")
word = input("Enter Word to Search: ").lower()

try:
    with open(filename, "r") as file:

        found = False
        count = 0

        for line_no, line in enumerate(file, start=1):

            occurrences = line.lower().count(word)

            if occurrences:
                found = True
                count += occurrences
                print(f"Line {line_no}: {line.strip()}")

        if found:
            print(f"\n'{word}' found {count} time(s).")
        else:
            print("Word not found.")

except FileNotFoundError:
    print("File not found.")
