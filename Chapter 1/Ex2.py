#CALCULATOR

# Asking the user to input two numbers. 
# Setting a variable to an input to be used later on with the formulas.
num1 = int(input("Enter your first number: ")) # Asking user for a first number || int to convert to integers || and to be used in the formula. 
num2 = int(input("Enter your second number: ")) # Asking user for a second number.


# New variable to be used later on in printing.
# Formulating the number that was given by the user. 
add = num1 + num2
minus = num1 - num2
multiply = num1 * num2

# There will be an error if the second number of the user is 0 because it is undefined that' s why i use this approach
# If not 0 the variable "quotient" and "remainder" is formulated when printed.
if num2 != 0:
    quotient = num1 / num2
    remainder = num1 % num2

# If not 0 then else
# Will show the string "Undefined" when variable is printed.
else:
    quotient = "Undefined" 
    remainder = "Undefined"

#Printing
print("Sum:", add)
print("Difference:", minus)
print("Product:", multiply)
print("Quotient:", quotient)
print("Remainder:", remainder)

