#USER INPUT

# Printing My greetings.
print("Hello There!") 

# Assigning a variables to the input. To use input to get user data. And later on to be use in printing.
username = input("What is your name? ") # Getting user name.
age = int(input("How old are you? "))# Getting user age. 
# int(input(...)) to convert the user's input into an integer type. This will later on be used for adding.

# Printing 
print("Nice to meet you,", username) # Used the variable to get user data and print it with a statement. 
                                          #Statement + variable in this case.
username_length = len(username) # Creating a new variable for the length of the input "username". 
                                #len is a function used to check a length of a string, list, array, etc...
print("Your name has", username_length, "letters.")# Printing statement with the variable "username_length".
print("You will be", age + 1, "years old next year.")# Printing statement with the variable "age." 
#The variable "age" is an integer and here we can add the input of "age" variable with 1.





