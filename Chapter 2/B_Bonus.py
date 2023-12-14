from datetime import datetime # to  provide classes for working with dates and times

# Function to calculate age based on the given birthdate
def calculate_age(birthdate):
    # Getting the current date and time now and setting is variable as today
    today = datetime.now()

    # Converting the user-provided birthdate string to a datetime object
    birthdate = datetime.strptime(birthdate, "%m/%d/%Y") # format

    # Calculating  age by comparing years and adjusting for the birthdate month and day
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return age

# Main function 
def main():
    # Getting the user's date of birth as input
    user_input = input("Enter your date of birth (MM/DD/YYYY): ")

    try:
        # calculate and display the age
        age = calculate_age(user_input) # the used of function
        print(f"Your age is {age} years.")
    except ValueError:
        # Handle the case where the user provides an invalid date format
        print("Invalid date format. Please enter the date in MM/DD/YYYY format.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()

