def line():

    print("=" * 80)


def title(text):

    line()

    print(text.center(80))

    line()


def display(records):

    if not records:

        print("No Records")

        return

    line()

    print(

        f"{'ID':<6}"

        f"{'NAME':<20}"

        f"{'DEPARTMENT':<18}"

        f"{'DESIGNATION':<18}"

        f"{'SALARY'}"

    )

    line()

    for employee in records:

        print(

            f"{employee[0]:<6}"

            f"{employee[1]:<20}"

            f"{employee[2]:<18}"

            f"{employee[3]:<18}"

            f"₹{employee[4]:,.2f}"

        )

    line()
