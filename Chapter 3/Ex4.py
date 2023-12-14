#DRAW SHAPE
import tkinter as tk

# Function to draw shape automatically 
def auto_canvas():
    # Getting the selected shape
    selected_shape = auto_shape_var.get()

    # Clearing previous drawing on the automatic canvas
    auto_canvas_widget.delete("all") #will be used to delete the shape widget when another shape is picked

    # Drawing the selected shape on the automatic canvas with defined coordinates
    if selected_shape == "Oval":
        auto_canvas_widget.create_oval(50, 50, 150, 150, outline="black", fill="black")
    elif selected_shape == "Rectangle":
        auto_canvas_widget.create_rectangle(50, 50, 150, 150, outline="black", fill="black")
    elif selected_shape == "Square":
        auto_canvas_widget.create_rectangle(50, 50, 150, 150, outline="black")
    elif selected_shape == "Triangle":
        auto_canvas_widget.create_polygon(50, 150, 100, 50, 150, 150, outline="black", fill="black" )

# Function that lets the user draw the shape with coordinates
def manual_canvas():
    # Getting the selected shape for manual canvas
    selected_shape = manual_shape_var.get()

    # Getting coordinate values from the user
    coordinates = entry_coordinates.get()
    coordinates = coordinates.split(',') # the coordinates should be split with comma. Indication of separation

    # Converting coordinates to integers
    coordinates = [int(coord.strip()) for coord in coordinates]

    # Clearing previous drawing on the manual canvas
    manual_canvas_widget.delete("all")

    # Drawing the selected shape on the manual canvas
    if selected_shape == "Oval":
        manual_canvas_widget.create_oval(coordinates, outline="black")
    elif selected_shape == "Rectangle":
        manual_canvas_widget.create_rectangle(coordinates, outline="black")
    #side_length = abs(coordinates[2] - coordinates[0]) calculates the absolute difference between the x-coordinates,
    # ensuring that the side length is always a positive value. 
    elif selected_shape == "Square":
        side_length = abs(coordinates[2] - coordinates[0])
        manual_canvas_widget.create_rectangle(coordinates, outline="black")
    elif selected_shape == "Triangle":
        manual_canvas_widget.create_polygon(coordinates, outline="black")

# Create the main window
root = tk.Tk()
root.title("Shape Drawer")

# First canvas -----------------------------------------------------------------------------------------
# Automatic canvas for displaying the shape
auto_canvas_widget = tk.Canvas(root, width=200, height=200, bg="white")
auto_canvas_widget.pack()

# Create a label and dropdown for selecting the shape (Automatic Canvas)
label_auto_shape = tk.Label(root, text="Auto Canvas: Select a shape")
label_auto_shape.pack()

# Variable for dropdown
auto_shapes = ["Oval", "Rectangle", "Square", "Triangle"]
auto_shape_var = tk.StringVar()
auto_shape_var.set(auto_shapes[0])  # Default shape is Oval

# Creating the dropdown
dropdown_auto_shape = tk.OptionMenu(root, auto_shape_var, *auto_shapes)
dropdown_auto_shape.pack()

# Button to update automatic canvas
button_auto_draw = tk.Button(root, text="Update Auto Canvas", command=auto_canvas)
button_auto_draw.pack()

# Second canvas ---------------------------------------------------------------------------------
# Manual canvas for drawing shapes with coordinates
manual_canvas_widget = tk.Canvas(root, width=200, height=200, bg="white")
manual_canvas_widget.pack()

# Create a label and dropdown for selecting the shape (Manual Canvas)
label_manual_shape = tk.Label(root, text="Manual Canvas: Select a shape")
label_manual_shape.pack()

manual_shapes = ["Oval", "Rectangle", "Square", "Triangle"]
manual_shape_var = tk.StringVar()
manual_shape_var.set(manual_shapes[0])  # Default shape is Oval

dropdown_manual_shape = tk.OptionMenu(root, manual_shape_var, *manual_shapes)
dropdown_manual_shape.pack()

# Create a label and entry for entering coordinate values
label_coordinates = tk.Label(root, text="Enter coordinates (comma-separated):")
label_coordinates.pack()

entry_coordinates = tk.Entry(root)
entry_coordinates.pack()

# Button to draw the shape on the manual canvas
button_manual_draw = tk.Button(root, text="Draw Manual Shape", command=manual_canvas)
button_manual_draw.pack()

#Run tk
root.mainloop()



