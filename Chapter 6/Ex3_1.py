#CALCULATOR
import operator 
# module to perform operations like addition, subtraction, 
#multiplication, etc., using functions instead of the actual operators.

# X and y to be given by user
# Function to perform addition
def add(x, y):
    return operator.add(x, y)

# Function to perform subtraction
def subtract(x, y):
    return operator.sub(x, y)

# Function to perform multiplication
def multiply(x, y):
    return operator.mul(x, y)

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return operator.truediv(x, y)

# Function to find modulus
def modulus(x, y):
    return operator.mod(x, y)

# Function to find the greater of two numbers
def greater(x, y):
    return max(x, y)

# Function to display the calculator menu
def menu():
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Check greater number")
        print("Q. Quit")

        # Get user's choice
        choice = input("Enter your choice (1-6 or Q to quit): ")

        # Check if the user wants to quit
        if choice.upper() == 'Q':
            break

        # Check if the choice is a valid number between 1 and 6
        if choice.isdigit() and 1 <= int(choice) <= 6:
            # asking x and y value from user
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
             
            # condition based on what option the user choose
            if choice == '1':
                result = add(x, y) # using function
            elif choice == '2':
                result = subtract(x, y)
            elif choice == '3':
                result = multiply(x, y)
            elif choice == '4':
                result = divide(x, y)
            elif choice == '5':
                result = modulus(x, y)
            elif choice == '6':
                result = greater(x, y)

            # Display the result
            print(f"Result: {result}")

        else: # if invalid input
            print(" Try again. Please enter a valid choice.")


if __name__ == "__main__":
   menu()

