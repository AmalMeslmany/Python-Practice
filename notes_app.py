while True:

    print("\n===== NOTES APP =====")
    print("1. Add Note")
    print("2. Exit")

    choice = input("Choose: ")

    if choice == "1":

        note = input("Enter your note: ")

        file = open("notes.txt", "a")

        file.write(note + "\n")

        file.close()

        print("Note Added Successfully!")

    elif choice == "2":

        print("Goodbye!")
        break

    else:

        print("Invalid Choice!")