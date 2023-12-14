#PRODUCT OF LIST ITEM


# Function calculating the product (values multiplied) of the list values.
def calculate_product(user_list):
    product = 1  # Starting point for the multiplication.   
    # Multiplying each element in the list
    # To iterate over each number in the user_list
    for num in user_list:
        product *= num     # This multiplies it with the current value of the product variable.       
        #if user enters 2 3 4
        # 2*3=6  6*4= 24  
    # Returning the calculated product
    return product

# Main program || Function
def main():
    # Getting the user's input to create a list of numbers.
    numbers = input("Enter a list of numbers with spaces: ").split() # Works only if user enters space in between the numbers.
    # Converting the input string to a list of integers using split().
    # The split() method separates the input string into individual items based on spaces.
    # Converting input to integers
    numbers = [int(num) for num in numbers]
    # Calling the function and getting the result
    result = calculate_product(numbers)

    # Printing the result
    print(f"The product of the numbers in the list is: {result}")

#start program
if __name__ == "__main__":
    main()
