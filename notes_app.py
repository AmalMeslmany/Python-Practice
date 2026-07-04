while True:

    print("\n===== NOTES APP =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        note = input("Enter your note: ")

        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()

        print("Note Added Successfully!")

    elif choice == "2":
        file = open("notes.txt", "r")
        notes = file.read()
        file.close()

        print("\n===== YOUR NOTES =====")
        print(notes)

    elif choice == "3":

         file = open("notes.txt", "w")
         file.close()

         print("All Notes Deleted!")

    elif choice == "4":

         print("Goodbye!")
         break

else:
        print("Invalid Choice!")