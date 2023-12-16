# AREA OF A SQUARE / CIRCLE / TRIANGLE CALCULATOR


# Importing the math module
# To have access to mathematical functions provided by this math module.
import math

#FORMULA ON FUNCTIONS 
# Functions to be used later on. 
# Function to calculate the area of a square
def square_area(side): 
    # formula of area of a square
    return side**2 # returning the outcome of the formula

# Function to calculate the area of a circle
def circle_area(radius):
    # Using math.pi to get the  π/radius and calculate the area of a circle
    return math.pi * radius**2

# Function to calculate the area of a triangle
def triangle_area(base, height):
    # Calculating the area of a triangle using the formula: 0.5 * base * height
    return 0.5 * base * height

# Main program function
def main():
    # Asking the user to choose a shape
    shape = input("What shape do you want to calculate?\n(s)quare\n(c)ircle\n(t)riangle\n").lower()
    # If user choose 's'
    if shape == 's':
        # Square calculation
        side = float(input("Enter the side length of the square: ")) # Side is needed to calculate the area of a square
        area = square_area(side) # Function is used. The function made earlier will be executed. 
        #This will now calculate the area of the square with the given 'side'.
        print(f"The area of the square is: {area}") # Printing variable outcome

# SAME APPROACH   
    # If user choose 'c'
    elif shape == 'c':
        # Circle calculation
        radius = float(input("Enter the radius of the circle: ")) # Radius is need to calculate the area of a circle
        area = circle_area(radius)
        print(f"The area of the circle is: {area}")
    
    # If user choose 't'
    elif shape == 't':
        # Triangle calculation
        # base and height need to calculate the area of a triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height) 
        print(f"The area of the triangle is: {area}")

    else:
        print("Invalid choice. Enter s, c, or t only.")

# Calling the main function to start the program
if __name__ == "__main__":
    main()



