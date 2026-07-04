tasks = []

while True:

    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print("-", task)

    elif choice == 3:
        task = input("Enter task to delete: ")

        if task in tasks:
            tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")