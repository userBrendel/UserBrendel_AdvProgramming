#LOOPING WITH WHILE LOOP . || USER CAN LOOP AS MUCH AS THEY WANT 
#USER SHOULD ENTER 'Y' TO KEEP LOOPING
#THE NUMBER OF TIMES THE LOOP IS EXECUTED WILL PRINT WHEN USER INPUTS.


# A count variable to track the number of times the loop is executed
count = 0  

# Using "while True" to loop.  
while True:  
    # Converting input to uppercase for case-insensitivity || in case the user puts an uncapitalized Q.
    user_input = input("Enter (Y) to continue looping || (Q) to quit: ").upper()

    # Incrementing the count variable value whenever the loop||input is executed.
    count += 1  
    
    # User input can be Y/Q/invalid   
    if user_input == 'Y':
        print(f"The loop was executed {count} times.\n")

    # Ending the loop    
    elif user_input == 'Q':
        print(f"You quit.\nThe loop was executed {count} times.")
        break  # Break the loop if the user enters 'Q'
    
    elif user_input != 'Y' and user_input != 'Q':  #When user input is not equal to 'Y' nor 'Q'
        print(f"\nThe loop was executed {count} times.\nInvalid input. Please try again.")
        break # Break the loop if the user input is not Y/Q




    
    
