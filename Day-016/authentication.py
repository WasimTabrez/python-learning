# Simulate user authentication

logged_in = False


def login_required(function):

    def wrapper(*args, **kwargs):

        if not logged_in:
            print("Access Denied. Please login first.\n")
            return

        return function(*args, **kwargs)

    return wrapper


@login_required
def view_account():

    print("Account Details")
    print("Balance : ₹50,000")


view_account()

logged_in = True

view_account()
