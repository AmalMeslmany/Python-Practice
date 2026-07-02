print("===== Python Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

choice = int(input("Choose an option: "))

if choice == 5:
    print("Goodbye!")
    exit()

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if choice == 1:
    result = first + second
    print("Result =", result)

elif choice == 2:
    result = first - second
    print("Result =", result)

elif choice == 3:
    result = first * second
    print("Result =", result)

elif choice == 4:
    if second == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = first / second
        print("Result =", result)

else:
    print("Invalid choice!")