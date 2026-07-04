contacts = {}

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")

        contacts[name] = phone

        print("Contact Added.")

    elif choice == "2":

        if len(contacts) == 0:
            print("No Contacts.")

        else:

            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":

        name = input("Enter Name: ")

        if name in contacts:
            print("Phone:", contacts[name])

        else:
            print("Contact Not Found.")

    elif choice == "4":

        name = input("Enter Name: ")

        if name in contacts:
            del contacts[name]
            print("Deleted Successfully.")

        else:
            print("Contact Not Found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")