#   CALCULATOR
import tkinter as tk
from tkinter import ttk

def result():# Defining a function that will get user data and to use as command
    try:
        # Getting user input from entry_num1, entry_num2, and value_var
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        value = value_var.get()

        # Once all info is received, this will execute
        if value == "+":  # addition
            result.set(num1 + num2)
        elif value == "-":  # subtraction
            result.set(num1 - num2)
        elif value == "*":  # multiplication
            result.set(num1 * num2)
        # The division value includes a check to prevent division by zero.
        elif value == "/":  # division
            if num2 != 0:  # it's divisible if it's not 0
                result.set(num1 / num2)
            else:
                result.set("Cannot divide by zero")  # If the value is 0
        elif value == "%":  # remainder
            result.set(num1 % num2)
        else:  # if entry is not a float value
            result.set("Invalid value")

    except ValueError: 
        result.set("Invalid input")


#Making the window and widgets
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#ebb5e8")
root.resizable(0,0)


# Title
title = tk.Label(root, text="Calculator", font=("Helvetica", 20, 'bold'), bg="#ebb5e8")
title.grid(row=0, column=2, pady=10)


# Entry for numbers || used in function
entry_num1 = ttk.Entry(root, width=20)
entry_num1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

entry_num2 = ttk.Entry(root, width=20)
entry_num2.grid(row=1, column=3, padx=10, pady=10)

# Dropdown for value selection
values = ["+", "-", "*", "/", "%"]
value_var = tk.StringVar(root)
value_var.set("+")  # Default value shown
#storing the list in the dropbox and storing the value_var to  automatically updated with the selected value.
value_menu = ttk.Combobox(root, textvariable=value_var, values=values, state="readonly", width=5)
value_menu.grid(row=1, column=2, padx=10, pady=10)

# Button to press to execute the command
button = ttk.Button(root, text="Calculate", command=result)
button.grid(row=2, column=2,  pady=10)

# Result label
result = tk.StringVar() # updating 
result_label = ttk.Label(root, width=15, textvariable=result) # displaying the result
result_label.grid(row=3, column=2,  pady=10)

root.mainloop()

