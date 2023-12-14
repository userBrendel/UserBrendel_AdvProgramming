#GREETING APP

import tkinter as tk
from tkinter import ttk

class Input: # Defining a class named Input for the functionality of the greeting application
     # self is used to access and modify the object's attributes.
     # root is used as a reference to the Tkinter root window, which is the main window of the GUI
    def __init__(self, root):# This method is to access instance variables and methods within a class
        self.root = root   # to make the tkinter root window accessible throughout the entire class
        self.root.title("Greetings!") # The title of the root window

# Widgets --------------------------------------------------------------------------------------------
        # Left Frame
        self.left_frame = tk.Frame(root, bg="lightblue", padx=20, pady=20, relief="groove", bd=5)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Centering the items inside the input frame
        self.left_frame.columnconfigure(1, weight=1)
        self.left_frame.rowconfigure(0, weight=1)  

        # Title label
        title_label = tk.Label(self.left_frame, text="Write Your Greeting", font=("Helvetica", 16, "bold"), fg="blue", bg="lightblue")
        title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        greet_label = tk.Label(self.left_frame, text="Greetings for:", bg="lightblue")
        greet_label.grid(row=1, column=0, pady=5)

        # Entry field for user's name
        self.name_entry = ttk.Entry(self.left_frame, font=("Helvetica", 12))
        self.name_entry.grid(row=1, column=1, pady=10, sticky="ew")

        # Dropdown menu for selecting color
        color_label = tk.Label(self.left_frame, text="Select Color:", bg="lightblue")
        color_label.grid(row=2, column=0, pady=5)

        self.color_var = tk.StringVar() # Variable to store data type and the input
        self.color_var.set("black")  # Default color
        color_options = ["black", "red", "green", "blue", "purple", "orange"]
        color_dropdown = ttk.Combobox(self.left_frame, textvariable=self.color_var, values=color_options, font=("Helvetica", 12))
        color_dropdown.grid(row=2, column=1, pady=5, sticky="ew")

        # Update Greeting button with reduced pady value
        update_button = ttk.Button(self.left_frame, text="Update Greeting", command=self.output) # Command used
        update_button.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")

#Display frame -------------------------------------------------------------------------------------
        # Create DisplayFrame
        self.display_frame = tk.Frame(root, bg="lightpink", padx=20, pady=20, relief="groove", bd=5)
        self.display_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Label to display personalized greeting
        self.greeting_label = tk.Label(self.display_frame, text="", font=("Helvetica", 16, "bold"), bg="white")
        self.greeting_label.pack(expand=True)

        # Configure grid weights to make frames resizable
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

# A function thats responsible for taking user's input  
   #  When the "Update Greeting" button is pressed, the output method is invoked.
    #  The method retrieves the user's name and selected color.     
    
    def output(self):         
    # Getting user's name and selected color
        user_name = self.name_entry.get()
        selected_color = self.color_var.get()

        # Changing/Updating greeting label in DisplayFrame
        greeting_text = f"Hello, {user_name}!"
        self.greeting_label.config(text=greeting_text, fg=selected_color)

# Running the program
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x260')
    app = Input(root)
    root.mainloop()





