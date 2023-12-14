#SHAPES
import tkinter as tk
from tkinter import ttk
import math

class Shape:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Area Calculator")
        self.root.geometry("400x300")

        self.sides = [] # to store the side values of the geometric shape.

        # Entry widgets for side values
        self.entry_labels = []
        self.entry_widgets = []
        self.create_entry_widgets()  # for entry widgets with its specific shape

        # Button to calculate area
        self.calculate_button = ttk.Button(self.root, text="Calculate Area", command=self.calculate_area)
        self.calculate_button.pack()

        # Output label
        self.output_label = ttk.Label(self.root, text="", font=("Arial", 10), wraplength=300)
        self.output_label.pack()

    def create_entry_widgets(self):
        pass  # To be implemented in subclasses
    
    def input_sides(self):
    # to clear the existing list of sides
     self.sides = []

    # Iterate over the entry widgets associated with the shape
     for entry_widget in self.entry_widgets:
        # Get the user-entered value from the entry widget
        side_value = entry_widget.get()

        try:
            # to convert the user input to a float
            side_value = float(side_value)

            # If successful, add the converted value to the list of sides
            self.sides.append(side_value)

        except ValueError:
            # incase the conversion to float fails (due to non-numeric input), handle the exception
            self.output_label.config(text="Invalid input. Please enter numerical values.")
            return False  # Return False if input validation failed

     # Return True if input validation was successful
     return True


    def calculate_area(self):
    #  if input validation was successful using the input_sides 
     if self.input_sides():
        # area calculation
        area_result = self.area()
        # Update the output label with the calculated area
        self.output_label.config(text=f"The area of the shape is: {area_result:.2f}")


    def area(self):
        pass  # To be implemented in subclasses

class Circle(Shape):
    def create_entry_widgets(self):
        # Entry widgets for circle (radius)
        radius_label = ttk.Label(self.root, text="Radius:", font=("Arial", 12))
        radius_label.pack()
        radius_entry = ttk.Entry(self.root, font=("Arial", 12), style='TEntry.Background.TEntry')
        radius_entry.pack()

        self.entry_labels.append(radius_label)
        self.entry_widgets.append(radius_entry)

    def area(self):
        # Area calculation for a circle
        return math.pi * self.sides[0] ** 2

class Rectangle(Shape):
    def create_entry_widgets(self):
        # Entry widgets for rectangle (length and width)
        length_label = ttk.Label(self.root, text="Length:", font=("Arial", 12))
        length_label.pack()
        length_entry = ttk.Entry(self.root, font=("Arial", 12), style='TEntry.Background.TEntry')
        length_entry.pack()

        width_label = ttk.Label(self.root, text="Width:", font=("Arial", 12))
        width_label.pack()
        width_entry = ttk.Entry(self.root, font=("Arial", 12), style='TEntry.Background.TEntry')
        width_entry.pack()

        self.entry_labels.extend([length_label, width_label])
        self.entry_widgets.extend([length_entry, width_entry])

    def area(self):
        # Area calculation for a rectangle
        return self.sides[0] * self.sides[1]

class Triangle(Shape):
    def create_entry_widgets(self):
        # Entry widgets for triangle (side1, side2, side3)
        side1_label = ttk.Label(self.root, text="Side 1:", font=("Arial", 12))
        side1_label.pack()
        side1_entry = ttk.Entry(self.root, font=("Arial", 12), style='TEntry.Background.TEntry')
        side1_entry.pack()

        side2_label = ttk.Label(self.root, text="Side 2:", font=("Arial", 12))
        side2_label.pack()
        side2_entry = ttk.Entry(self.root, font=("Arial", 12), style='TEntry.Background.TEntry')
        side2_entry.pack()

        side3_label = ttk.Label(self.root, text="Side 3:", font=("Arial", 12))
        side3_label.pack()
        side3_entry = ttk.Entry(self.root, font=("Arial", 12), style='TEntry.Background.TEntry')
        side3_entry.pack()

        self.entry_labels.extend([side1_label, side2_label, side3_label])
        self.entry_widgets.extend([side1_entry, side2_entry, side3_entry])

    def area(self):
        # Area calculation for a triangle using Heron's formula
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

#running everything
if __name__ == "__main__":
    root = tk.Tk()
    circle_app = Circle(root)
    rectangle_app = Rectangle(root)
    triangle_app = Triangle(root)
    root.mainloop()
