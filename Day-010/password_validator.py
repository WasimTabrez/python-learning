# Validate password strength

password = input("Enter password: ")

if len(password) < 8:
    print("Weak password")
elif not any(ch.isupper() for ch in password):
    print("Must contain an uppercase letter")
elif not any(ch.islower() for ch in password):
    print("Must contain a lowercase letter")
elif not any(ch.isdigit() for ch in password):
    print("Must contain a digit")
else:
    print("Strong Password")
