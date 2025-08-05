def calculator():
    print("Welcome to Simple Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        # Using int() to get whole numbers
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print("Result:", result)

        elif choice == '2':
            result = num1 - num2
            print("Result:", result)

        elif choice == '3':
            result = num1 * num2
            print("Result:", result)

        elif choice == '4':
            if num2 != 0:
                # This gives decimal if needed (e.g., 5 / 2 = 2.5)
                result = num1 / num2
                print("Result:", result)
            else:
                print("Error: Cannot divide by zero!")

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the calculator
calculator()
