#AREA FUNCTION
import tkinter as tk
from tkinter import ttk
import math  #provides a set of mathematical functions.

# A function used to calculate the area of a circle
def circle_area(radius_entry, result_label): # Taking  radius entry widget and a label widget as parameters
    try: # try / if no error
        radius = float(radius_entry.get()) # converting the user input for radius from the entry widget to a float.
        area = math.pi * radius**2 # formula for area stored in a variable. using the radius variable get data.
        result_label.config(text=f"Area: {area:.2f}") # displaying result
    except ValueError: # if error occur
        result_label.config(text="Invalid input. Please enter a valid number.")
        
# Same approach for the following function ---------------------------------------------------------------------

# A function used to calculate the area of a square
def square_area(side_entry, result_label):
    try:
        side = float(side_entry.get())
        area = side**2
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# A function used to calculate the area of a rectangle
def rectangle_area(length_entry, width_entry, result_label):
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = length * width
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Main program
def main():
    root = tk.Tk()
    root.title("Shape Area Calculator")

    #Setting a variable and Creating a notebook or a tab widget 
    notebook = ttk.Notebook(root)

    # Circle Tab ------------------------------------------------------------------------------------
    circle_tab = ttk.Frame(notebook) # Variable to be used as a frame in the tab
    # All items inside circle_tab >>>>>>>
    notebook.add(circle_tab, text="Circle")

    radius_label = tk.Label(circle_tab, text="Enter radius:")
    radius_entry = tk.Entry(circle_tab)
    # Button with the function as command
    # lambda is used to create an anonymous function
    calculate_circle_button = tk.Button(circle_tab, text="Calculate Area", command=lambda: circle_area(radius_entry, circle_result_label))
    circle_result_label = tk.Label(circle_tab, text="Area: ")
    
    # positioning
    radius_label.grid(row=0, column=0, padx=10, pady=10)
    radius_entry.grid(row=0, column=1, padx=10, pady=10)
    calculate_circle_button.grid(row=1, column=0, columnspan=2, pady=10)
    circle_result_label.grid(row=2, column=0, columnspan=2, pady=10)

    # Square Tab -----------------------------------------------------------------------------------------------------
    square_tab = ttk.Frame(notebook) # Different frame/ tab in the notebook
    notebook.add(square_tab, text="Square")

    side_label = tk.Label(square_tab, text="Enter side length:")
    side_entry = tk.Entry(square_tab)
    calculate_square_button = tk.Button(square_tab, text="Calculate Area", command=lambda: square_area(side_entry, square_result_label))
    square_result_label = tk.Label(square_tab, text="Area: ")

    side_label.grid(row=0, column=0, padx=10, pady=10)
    side_entry.grid(row=0, column=1, padx=10, pady=10)
    calculate_square_button.grid(row=1, column=0, columnspan=2, pady=10)
    square_result_label.grid(row=2, column=0, columnspan=2, pady=10)

    # Rectangle Tab
    rectangle_tab = ttk.Frame(notebook) # Different frame/ tab in the notebook
    notebook.add(rectangle_tab, text="Rectangle")

    length_label = tk.Label(rectangle_tab, text="Enter length:")
    length_entry = tk.Entry(rectangle_tab)
    width_label = tk.Label(rectangle_tab, text="Enter width:")
    width_entry = tk.Entry(rectangle_tab)
    calculate_rectangle_button = tk.Button(rectangle_tab, text="Calculate Area", command=lambda: rectangle_area(length_entry, width_entry, rectangle_result_label))
    rectangle_result_label = tk.Label(rectangle_tab, text="Area: ")

    length_label.grid(row=0, column=0, padx=10, pady=10)
    length_entry.grid(row=0, column=1, padx=10, pady=10)
    width_label.grid(row=1, column=0, padx=10, pady=10)
    width_entry.grid(row=1, column=1, padx=10, pady=10)
    calculate_rectangle_button.grid(row=2, column=0, columnspan=2, pady=10)
    rectangle_result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Pack and running the application
    notebook.pack(expand=1, fill="both")
    root.mainloop()

if __name__ == "__main__":
    main()
