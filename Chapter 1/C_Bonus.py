while True: # loop
    #Menu
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    # Setting variable for user choice
    choice = input("Choose operation (1-5): ")

    # If choice not in 1-5
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please choose a number from 1 to 5.") # Invalid
        continue # Continue code again
    
    # User input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Condition based on what the user choice is
    #Formulas
    if choice == '1':
        result = num1 + num2 # Addition
    elif choice == '2':
        result = num1 - num2 # Subtraction
    elif choice == '3':
        result = num1 * num2 #MultiplicationS
    elif choice == '4':
        if num2 != 0: # If num 2 not 0
            result = num1 / num2 # Division
        else: # if 0
            result = "Error: Division by zero"
    elif choice == '5':
        if num2 != 0:
            result = num1 % num2 # Modulus
        else:
            result = "Error: Modulus by zero"

    print(f"Result: {result}") # Display/print result

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes': #if not yes
        print("Exiting the calculator.")
        break # break loop
