while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    choice = input("Choose operation (1-5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please choose a number from 1 to 5.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif choice == '5':
        if num2 != 0:
            result = num1 % num2
        else:
            result = "Error: Modulus by zero"

    print(f"Result: {result}")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        print("Exiting the calculator.")
        break
