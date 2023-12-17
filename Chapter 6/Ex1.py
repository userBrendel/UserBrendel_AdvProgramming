#BASIC MATH
import math # Module to be used for calculation terms

# Finding the ceil of a
a = 2.3
ceil_result = math.ceil(a) # math.ceil returns the smallest integer greater than or equal to a
print(f"For a = {a}, ceil(a) = {ceil_result}")

# Find the floor of a
a = 2.3
floor_result = math.floor(a) # math.floor returns the largest integer less than or equal to a
#display result
print(f"For a = {a}, floor(a) = {floor_result}")

# Finding the factorial of a
a = 5
factorial_result = math.factorial(a) # returns the factorial of a non-negative integer.
print(f"For a = {a}, factorial(a) = {factorial_result}")

# Find the value of 2^3
exponential_result = math.pow(2, 3) # returns the value of x raised to the power of y.
print(f"The value of 2^3 is: {exponential_result}")

# Find the square root of a
a = 16
sqrt_result = math.sqrt(a) # returns square root
print(f"For a = {a}, square root(a) = {sqrt_result}")
