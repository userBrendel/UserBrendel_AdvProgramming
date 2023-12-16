#PASSWORD CHECK

import tkinter as tk
from tkinter import messagebox

# Function for command
def check_pass():
    password = entry_password.get() # storing the user entry password
 
    # Check if the password meets certain criteria
    if (
     any(char.islower() for char in password) and  # At least entry_password has one lowercase character
     any(char.isupper() for char in password) and  # At least entry_password has one uppercase character
     any(char.isdigit() for char in password) and  # At least entry_password has one entry_password has digit
     any(char in "$#@ " for char in password) and  # At least entry_password has one special entry_password has character ($, #, @, or space)
     6 <= len(password) <= 12  #entry_password length should be between 6 and 12 characters
   ):
        
     # If the password is valid, show an information message box
     messagebox.showinfo("Password Check", "Password is valid!")
     root.destroy()  # '.destroy' to close the window after successful validation
     
    else:
    # If the password is invalid, it will decrease the attempts counter
     global attempts # global variable
     attempts -= 1 # decrease
     # It will also show a warning message box with the number of attempts left
     messagebox.showwarning("Password Check", f"Invalid password! Attempts left: {attempts}")

    # Check if there are no attempts left
    if attempts == 0: # when equal to 0
        # If 0 it will show an error message box indicating that authorities have been alerted
        messagebox.showerror("Alert", "Authorities have been alerted!")
        root.destroy()  


# main window -------------------------------------------------------------------------------------
root = tk.Tk()
root.resizable(0,0)

# Set the number of attempts
attempts = 5

# labels and entry for password
label_password = tk.Label(root, text="Enter Password:", font=("Helvetica", 14))
label_password.pack()

entry_password = tk.Entry(root, font=("Helvetica", 12), bd=5, relief=tk.GROOVE)
entry_password.pack()

# Displaying password rules 
label_rules = tk.Label(root, text="Password Rules:", font=("Helvetica", 12, "bold"), pady=10)
label_rules.pack()

rules_text = "- At least 1 lowercase letter\n" \
             "- At least 1 uppercase letter\n" \
             "- At least 1 digit (0-9)\n" \
             "- At least 1 of the following: $, #, @\n" \
             "- Minimum length: 6 characters\n" \
             "- Maximum length: 12 characters"

rules_info = tk.Label(root, text=rules_text, font=("Helvetica", 10), justify=tk.LEFT)
rules_info.pack()

# a creative button with additional styling
button_check = tk.Button(root, text="Check Password", command=check_pass, font=("Helvetica", 12),
                         bg="#4CAF50", fg="white", padx=10, pady=5, bd=5)
button_check.pack()

root.mainloop()
