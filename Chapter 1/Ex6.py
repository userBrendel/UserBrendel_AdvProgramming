#FIZZBUZZ
#PROGRAM THAT PRINTS 1-100
#MULTIPLE OF 3 = FIZZ
#MULTIPLE OF 5 = BUZZ
#MULTIPLE OF 3 AND 5 = FIZZBUZZ

# Loop through numbers from 1 to 100 || Range gives a sequence of number, in a given range.
# num has a range of (1,101). 
# Range function start with 0 so here instead of 100, i used 101.
for num in range(1, 101): 
    
    # if the number is divisible by both 3 and 5
    # '%' returns the remainder of num and 3 and 5
    # if remainder of the num divided by 3 and 5 is 0 therefore its divisible by 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz") #prints if divisible by 3 and 5

    #SAME APPROACH
    elif num % 3 == 0:
        print("Fizz") #prints if divisible by 3
    
    # if the number is divisible by 5
    elif num % 5 == 0:
        print("Buzz") #prints if divisible by 5
    
    
    # If the number is not divisible by 3 or 5
    else:
        print(num) # prints the number if not in the if-else condition.