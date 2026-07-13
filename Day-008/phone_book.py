# Menu-driven Phone Book Application

contacts = {}

def add_contact():
    name = input("Enter Name: ")

    if name in contacts:
        print("Contact already exists.\n")
        return
    
    phone = input("Enter Phone Number: ")

    contacts[name] = phone

    print("Contact added successfully.\n")

def search_contact():
    if not contacts:
        print("No contacts available.\n")
        return
    
    name = input("Enter Name: ")

    if name in contacts:
        print(f"{name} : {contacts[name]}\n")
    else:
        print("Contact not found.\n")

def update_contact():
    if not len(contacts):
        print("No contacts available.\n")
        return
    
    name = input("Enter Name: ")

    if name in contacts:
        phone = input("Enter New Phone Nubmer: ")

        contacts[name] = phone

        print("Contact updated successfully.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    if len(contacts) == 0:
        print("No contacts available.\n")
        return
    
    name = input("Enter Name: ")

    if name in contacts:
        del contacts[name]
    
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")
    
def display_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    
    print("\nContact List")
    print("------------")

    for index, (name, phone) in enumerate(contacts.items(), start = 1):
        print(f"{index}. {name} : {phone}")
    print()

def menu():
    while True:
        print("======= Phone Book ========")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_contact()
            case "2":
                search_contact()
            case "3":
                update_contact()
            case "4":
                delete_contact()
            case "5":
                display_contacts()
            case "6":
                print("Thank you!")
                break
            case _:
                print("Invalid Choice.\n")

menu()
    