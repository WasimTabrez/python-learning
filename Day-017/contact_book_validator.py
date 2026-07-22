# Contact Book Validator using Regular Expressions

import re

contacts = {}


def validate_name(name):
    pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
    return re.fullmatch(pattern, name)


def validate_mobile(mobile):
    pattern = r"^[6-9]\d{9}$"
    return re.fullmatch(pattern, mobile)


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(pattern, email)


def add_contact():

    name = input("Enter Name: ").strip()

    if not validate_name(name):
        print("Invalid Name.\n")
        return

    mobile = input("Enter Mobile Number: ").strip()

    if not validate_mobile(mobile):
        print("Invalid Mobile Number.\n")
        return

    if mobile in contacts:
        print("Mobile Number already exists.\n")
        return

    email = input("Enter Email Address: ").strip()

    if not validate_email(email):
        print("Invalid Email Address.\n")
        return

    contacts[mobile] = {
        "name": name,
        "email": email
    }

    print("Contact Added Successfully.\n")


def search_contact():

    mobile = input("Enter Mobile Number: ").strip()

    if mobile in contacts:

        print("\nContact Found")

        print("------------------------")

        print("Name   :", contacts[mobile]["name"])
        print("Mobile :", mobile)
        print("Email  :", contacts[mobile]["email"])
        print()

    else:
        print("Contact Not Found.\n")


def delete_contact():

    mobile = input("Enter Mobile Number: ").strip()

    if mobile in contacts:
        del contacts[mobile]
        print("Contact Deleted Successfully.\n")
    else:
        print("Contact Not Found.\n")


def display_contacts():

    if not contacts:
        print("No Contacts Available.\n")
        return

    print("\n========= Contact List =========")

    for mobile, details in sorted(contacts.items()):

        print(f"Name   : {details['name']}")
        print(f"Mobile : {mobile}")
        print(f"Email  : {details['email']}")
        print("-" * 35)

    print()


def menu():

    while True:

        print("====== Contact Book Validator ======")

        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter Choice: ")

        match choice:

            case "1":
                add_contact()

            case "2":
                search_contact()

            case "3":
                delete_contact()

            case "4":
                display_contacts()

            case "5":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice.\n")


menu()
