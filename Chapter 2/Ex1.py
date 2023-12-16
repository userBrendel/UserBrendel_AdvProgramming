# WELCOME TO GUI || Graphical User Interface
# GUI is a visual way for users to interact with a computer or software,
# using graphical elements like buttons, icons, and windows

# Tkinter is a Python library for creating graphical user interfaces (GUIs).
import tkinter as tk # Importing tkinter. 
# Can also use 'from tkinter import*' to import more.


root = tk.Tk() # Creating a window
root.title("Welcome to GUI") # Title of the window
root.geometry("800x800")  # Setting the default window size
root.resizable(0, 0)  # Disabling resizing the window. Other approach can be ((false,false))
root.configure(bg="#83c1d4")  # Adding background color to the window

# Creating a Label to add text
# Variable 'text' is a Label and is a part of root
# text to put the text, font to design the text, bg for background color
text = tk.Label(root, text="Welcome to Graphical user interface(GUI)!", font=("Helvetica", 19, "bold"), 
                bg="#eca1ed")

# Placing the label 'text' in the window 
# .pack helps to add positioning before the label is added to the root
text.pack(pady=50) # With a padding of 50. 


root.mainloop() # Running the window
