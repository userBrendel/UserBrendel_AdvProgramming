#USER INFORMATION

import tkinter as tk
from tkinter import messagebox

class Bio:
    def __init__(self, root):
        self.root = root
        
        # Creating labels and entry widgets for user input/data
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="e")

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.grid(row=1, column=0, sticky="e")
        
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1)

        self.hometown_label = tk.Label(root, text="Hometown:")
        self.hometown_label.grid(row=2, column=0, sticky="e")
        
        self.hometown_entry = tk.Entry(root)
        self.hometown_entry.grid(row=2, column=1)

        # Using Function as command
        # Creating buttons for actions
        self.save_button = tk.Button(root, text="Save", command=self.save_info)
        self.save_button.grid(row=3, column=0, pady=10)

        self.read_button = tk.Button(root, text="Display Info", command=self.read_info)
        self.read_button.grid(row=3, column=1, pady=10)
    
    # For saving info in the txt file
    # save_button command
    def save_info(self):
        # Getting user input and storing it in a variable
        name = self.name_entry.get()
        age = self.age_entry.get()
        hometown = self.hometown_entry.get()

        # Writing data to the file
        with open("bio.txt", "w") as file: # to create/open txt file
            # writing in the txt file with .write.
            # using the variable to display user input
            file.write(f"Name: {name}\n")  # displaying next info with \n new line with
            file.write(f"Age: {age}\n")
            file.write(f"Hometown: {hometown}\n")
        
        # Message box that tells the data successfully write on the txt file
        messagebox.showinfo("Information saved to bio.txt")
    
    # For reading the txt file 
    # read_button command
    def read_info(self):
        # Reading data from file and display
        try:
            with open("bio.txt", "r") as file:
                info = file.read() # reading the file / getting info to be used to display.
                messagebox.showinfo("Bio Information", info) # showing the info in the txt file with messagebox
        except FileNotFoundError: # incase of error
            messagebox.showerror("Error", "File 'bio.txt' not found. Save information first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Bio(root)
    root.mainloop()

