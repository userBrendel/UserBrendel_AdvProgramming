#LARGEST NUMBER 

# Asking the user for 3 different number || using float as user might input a decimal value.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Comparing the numbers to find the largest
# All possible largest number scenario
if num1 >= num2 and num1 >= num3: # num1 is largest
    largest = num1
elif num2 >= num1 and num2 >= num3: # num2 is largest
    largest = num2
else: # num3 is largest
    largest = num3

# Output the largest number || printing statement and largest variable outcome.
print("The largest number is:", largest)