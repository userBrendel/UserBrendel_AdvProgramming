#ARITHMETIC OPERATIONS

import tkinter as tk
from tkinter import ttk

# Class AO to handle the arithmetic operations
class AO:
    def __init__(self):
        #  the result default
        self.result = 0

    def calculate(self, operation, num1, num2): #store info
        # calculation condition based on  the selected operation
        if operation == "Addition":
            self.result = num1 + num2
        elif operation == "Subtraction":
            self.result = num1 - num2
        elif operation == "Multiplication":
            self.result = num1 * num2
        elif operation == "Division":
            # Handle division by zero
            if num2 != 0:
                self.result = num1 / num2
            else:
                return "Error: Division by zero"
        # Return the result message
        return f"Result: {self.result}"


class widget:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Operations")
        self.root.geometry("400x300")
        self.root.configure(bg='#e0f7fa')  

        # Custom font for consistent styling
        font = ("Arial", 12)

        # an instance of AO to perform calculations
        self.arithmetic_operations = AO()

        # Label for operation selection 
        self.operation_label = ttk.Label(root, text="Select Operation:", font=font, background="#e0f7fa")
        self.operation_label.pack()

        # Using Combobox for operation selection
        self.operation_var = tk.StringVar()
        self.operation_combobox = ttk.Combobox(root, textvariable=self.operation_var,
                                               values=["Addition", "Subtraction", "Multiplication", "Division"],
                                               font=font)
        self.operation_combobox.pack()

        # Labels and entry widgets for operands -------------------------------------------------------
        #num 1
        self.num1_label = ttk.Label(root, text="Operand 1:", font=font, background="#e0f7fa")
        self.num1_label.pack()
        self.num1_entry = ttk.Entry(root, font=font)
        self.num1_entry.pack()
        
        #num 2
        self.num2_label = ttk.Label(root, text="Operand 2:", font=font, background="#e0f7fa")
        self.num2_label.pack()
        self.num2_entry = ttk.Entry(root, font=font)
        self.num2_entry.pack()

        # button with command
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.perform_calculation, style='TButton')
        self.calculate_button.pack()

        # Output label to display the result
        self.output_label = ttk.Label(root, text="", font=font, wraplength=300, background="#e0f7fa")
        self.output_label.pack()

        # Style for the button
        style = ttk.Style()
        style.configure('TButton', font=font, foreground='#000000', background='#00796b')  # Set button style

    def perform_calculation(self):
        # Getting operation from user input
        operation = self.operation_var.get()
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())

        #  calculation using AO class
        result_message = self.arithmetic_operations.calculate(operation, num1, num2)

        # putting the result on the output label
        self.output_label.config(text=result_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = widget(root)
    root.mainloop()
