#LOGIN PAGE

import tkinter as tk

root = tk.Tk()
root.title("Login Page")
root.resizable(0, 0)

# -------------------- the username Label and Entry ---------------------

# Label
# Here I used Method chaining as a shortcut.
# Different method chain together
tk.Label(root, text="Username:").grid(row=0, column=0, pady=5) #Using grid to specify the position of the label.


# Entry
username_entry = tk.Entry(root).grid(row=0, column=1, pady=5)  # This puts the label in the next column of the label

# --------------------- Password Label and Entry ------------------------------
#Label
tk.Label(root, text="Password:").grid(row=1, column=0, pady=5) # Display at the bottom of first label/ next row

# Entry
password_entry = tk.Entry(root).grid(row=1, column=1, pady=5)  # Position at same row of 2nd label and at the bottom of 1st label

# Login Button
tk.Button(root, text="Login").grid(row=2, column=0, columnspan=2, pady=10) # columnspan to occupy space2 row


root.mainloop()


