# Login Validation

USERNAME = "admin"
PASSWORD = "1234"

attempts = 3

while attempts:

    username = input("Username: ")
    password = input("Password: ")

    try:

        if username != USERNAME:
            raise Exception("Invalid Username.")

        if password != PASSWORD:
            raise Exception("Invalid Password.")

        print("Login Successful.")
        break

    except Exception as error:
        attempts -= 1

        print(error)

        if attempts:
            print("Attempts Remaining:", attempts)
        else:
            print("Account Locked.")
