#TRIANGLE CHECKER

#Triangle has 3 sides
#Asking user for data
#Float values into a decimal point || User may put values that have a decimal point.
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))



# Checking if the user data creates a valid triangle ||  triangle inequality theorem.
# If the sum of the lengths of any two sides of a triangle is greater than the length of the remaining side, 
# then it is a valid triangle.

# Using if-elif-else statement for different conditions.

# CHECKING IF THE GIVEN DATA IS A TRIANGLE
if side1 + side2 > side3  and side1 + side3 > side2 and side2 + side3 > side1:
    print("It's a valid triangle.") #Will print if it meets the if condition ^

# Classifying the type of triangle.
    if side1 == side2 == side3:
        print("It's an Equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("It's an Isosceles triangle.")
    else:
        print("It's a Scalene triangle.")

else:
    print("Not a triangle.")