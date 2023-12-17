#STUDENT CLASS
import tkinter as tk
from tkinter import ttk

# Class student to store details of student.
class student:
    def __init__(self, name, mark1, mark2, mark3):
        #name
        self.name = name
        #marks
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        average = (self.mark1 + self.mark2 + self.mark3) / 3 # formula to find average
        return average  

    def display(self): # for displaying the outcome
        return f"Name: {self.name}, Average Grade: {self.calcGrade():.2f}"

class widget:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.configure(bg='#e0f7fa')  

        # Custom font
        # styling same as Ex1
        font = ("Arial", 12)
        
        self.title_label = ttk.Label(root, text="Student Grade Calculator", font=font, background="#e0f7fa")
        self.title_label.pack(pady=20)

        # Entry widgets for student details ------------------------------------------------------
        self.name_label = ttk.Label(root, text="Student Name:", font=font, background="#e0f7fa")
        self.name_label.pack()
        self.name_entry = ttk.Entry(root, font=font, style='TEntry.Background.TEntry')
        self.name_entry.pack()
        
        # mark 1
        self.mark1_label = ttk.Label(root, text="Mark 1:", font=font, background="#e0f7fa")
        self.mark1_label.pack()
        self.mark1_entry = ttk.Entry(root, font=font, style='TEntry.Background.TEntry')
        self.mark1_entry.pack()
        
        # mark 2
        self.m2_label = ttk.Label(root, text="Mark 2:", font=font, background="#e0f7fa")
        self.m2_label.pack()
        self.m2_entry = ttk.Entry(root, font=font, style='TEntry.Background.TEntry')
        self.m2_entry.pack()
        
        # mark 3
        self.mark3_label = ttk.Label(root, text="Mark 3:", font=font, background="#e0f7fa")
        self.mark3_label.pack()
        self.mark3_entry = ttk.Entry(root, font=font, style='TEntry.Background.TEntry')
        self.mark3_entry.pack()

        # Button to create the outcome
        self.create_button = ttk.Button(root, text="Create Student", command=self.outcome, style='TButton')
        self.create_button.pack()

        # Output label for outcome
        self.output_label = ttk.Label(root, text="", font=font, wraplength=300, background="#e0f7fa")
        self.output_label.pack()
 
        # Style
        style = ttk.Style()
        style.configure('TButton', font=font, foreground='#000000', background='#00796b')  
        style.configure('TEntry.Background.TEntry', background='#ffffff') 
    
    
    # function to create student objects and display information
    def outcome(self):
        # Getting user input for student details
        name = self.name_entry.get()
        mark1 = float(self.mark1_entry.get())
        mark2 = float(self.m2_entry.get())
        mark3 = float(self.mark3_entry.get())

        # Creating updated student objects
        student1 = student(name, mark1, mark2, mark3)

        # Displaying student information
        # putting it in output_label position
        self.output_label.config(text=student1.display())

if __name__ == "__main__":
    root = tk.Tk()
    app = widget(root)
    root.mainloop()


