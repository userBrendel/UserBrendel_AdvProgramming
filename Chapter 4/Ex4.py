#LETTER COUNT

import tkinter as tk
from tkinter import ttk, messagebox

class CountLetter:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")

        # Variable to store the entered letter and setting its data type
        self.letter_var = tk.StringVar()

        # Creating the widgets
        self.widgets()

    def widgets(self):
        # Enter label and Letter entry ------------------------------------------------------------
        letter_label = ttk.Label(self.root, text="Enter a letter:", font=("Helvetica", 14))
        letter_label.pack(pady=10)

        # Entry widget
        # setting the entry input as string
        letter_entry = ttk.Entry(self.root, textvariable=self.letter_var, font=("Helvetica", 12))
        letter_entry.pack(pady=10, ipadx=20)
        
        # Button with command -----------------------------------------------------------------
        count_button = ttk.Button(self.root, text="Count Occurrences", command=self.count)
        count_button.pack(pady=20, ipadx=10)

    # Used as command
    def count(self):
        # Getting the entered letter and storing it in a variable
        letter = self.letter_var.get()

        # if a letter is not entered and if it doesn't have a length of 1 (1 letter)
        if not letter.isalpha() or len(letter) != 1:
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        # Reading the infos of sentences.txt that was also used for Exercise 2.
        with open("Chapter 4/sentences.txt", "r") as file:
            info = file.read()

            # Counting occurrences of the entered letter
            count = info.lower().count(letter.lower())

            # Showing the result in a message box
            messagebox.showinfo("Letter Count Result", f"The letter '{letter}' occurs {count} times.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CountLetter(root)
    root.mainloop()


