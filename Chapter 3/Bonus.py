
def menu(): # Function with the burger menu
    print("Burger Shack Menu:")
    print("1. Beef Burger")
    print("2. Chicken Burger")
    print("3. Vegetarian Burger")

def burger(): # Function to store the types of burger
    burger_types = ["Beef Burger", "Chicken Burger", "Vegetarian Burger"] # storing in a list
    while True:
        try:
            # if valid selection 1-3
            choice = int(input("Choose a burger type (1-3): "))
            if 1 <= choice <= 3: # if 1-3
                return burger_types[choice - 1] # display burger type
            # For errors
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def toppings(): # Function to store the types of toppings
    toppings = ["Cheese", "Peanut Butter", "Avocado"]  # List of available toppings
    print("\nChoose toppings:")    # Displays a message to choose toppings
    # Display the available toppings with corresponding numbers
    print(", ".join([f"{i + 1}. {topping}" for i, topping in enumerate(toppings)]))   
    user_input = input("Enter topping numbers (1,2 separate with comma if choosing more than one item): ") # input that ask the user to enter topping numbers, separated by commas
    selected_toppings = [toppings[int(index) - 1] for index in user_input.split(",") if 1 <= int(index) <= len(toppings)]  # Extract selected toppings based on user input
    return selected_toppings



def condiments():
    condiments = ["Ketchup", "Mayonnaise", "BBQ Sauce"]
    print("\nChoose condiments:")
    print(", ".join([f"{i + 1}. {condiment}" for i, condiment in enumerate(condiments)]))
    user_input = input("Enter condiment numbers (e.g., 1,2): ")
    selected_condiments = [condiments[int(index) - 1] for index in user_input.split(",")]
    return selected_condiments

def sides():
    sides = ["Fries", "Drink"]
    print("\nChoose sides (separate with commas):")
    print(", ".join([f"{i + 1}. {side}" for i, side in enumerate(sides)]))
    user_input = input("Enter side numbers (e.g., 1,2): ")
    selected_sides = [sides[int(index) - 1] for index in user_input.split(",")]
    return selected_sides


def total(order_items):
    # Assigning price
    prices = {"Beef Burger": 5.99, "Chicken Burger": 4.99, "Vegetarian Burger": 3.99,
              "Cheese": 0.50, "Peanut Butter": 0.75, "Avocado": 1.00,
              "Ketchup": 0.25, "Mayonnaise": 0.30, "BBQ Sauce": 0.50,
              "Fries": 2.50, "Drink": 1.50}

    total = sum(prices[item] for item in order_items) # Calculating total on what the users item choose
    return total

def payment(total):
    while True:
        try:
            amount_paid = float(input(f"\nEnter amount paid (${total:.2f}): ")) # user input money
            if amount_paid >= total: # if input grater than total
                change = amount_paid - total
                print(f"Thank you for your payment! Your change is ${change:.2f}") # print
                break
            else:
                print("Insufficient payment. Please enter a sufficient amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main(): # Main program
    print("Welcome to Burger Shack!")
    menu() # display menu
    
    # Calls function to get the user's choices for burger type, toppings, condiments, and sides.
    burger_type = burger()
    chosen_toppings = toppings()
    chosen_condiments = condiments()
    chosen_sides = sides()
    
    #combines the user's choices into a single list 
    order_items = [burger_type] + chosen_toppings + chosen_condiments + chosen_sides
    total_price = total(order_items) # calculating every item in the list
    
    print("\n---------Your Order------------")
    # to print the user's order item by item
    for item in order_items:
        print(f"- {item}")

    print(f"\nTotal Price: ${total_price:.2f}")

    payment(total_price)# using function to process the payment for the order.

if __name__ == "__main__": # runs main
    main()
