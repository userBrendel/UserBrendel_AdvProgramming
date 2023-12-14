#PRINTING EVEN NUMBER THAT RANGE FROM 1-100

# Creating a loop range from 1-100
#For loop is used to iterate all items till its finish.
for num in range(1, 101):
    # Check if the number in num is not even 
    if num % 2 != 0: 
        # If the num is divided to 2 and the remainder is not equal to 0.
        # Then skip and continue with the next iteration.
        continue
    
    # Print the rest of num || even numbers
    print(num)
