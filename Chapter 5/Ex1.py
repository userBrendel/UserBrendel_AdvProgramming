#WOOF WOOF

import tkinter as tk
from tkinter import ttk

# A Class named Dog for storing dogs' name and age || to find oldest dog
class Dog:
    # initializing the Dog object with a name and age
    def __init__(self, name, age):
        #Setting attributes
        self.name = name  
        self.age = age    

    # returning a woof message based on the dog's name
    def woof(self):
        return f"{self.name} says: Woof! Woof!"

    # Class method to find the oldest dog from a list and make it woof
    @classmethod
    def find_oldest(cls, dogs):
        # To find the oldest dog using the max function and a lambda function 
        oldest_dog = max(dogs, key=lambda x: x.age)
        # return the woof message after getting all info
        return oldest_dog.woof()

# Class for the window and widget
class Window:
    def __init__(self, master):
        self.master = master
        self.master.title("Woof Woof GUI")
        self.master.geometry("400x300")
        self.master.configure(bg='#e0f7fa')  
        
        # A variable for Custom font.
        # use to make styling less redundant
        font = ("Arial", 12,)

        self.title_label = ttk.Label(master, text="WOOF WOOF INFO!", font=font, background="#e0f7fa")
        self.title_label.pack(pady=20)

        # Entry name for Dog 1 -----------------------------------------------------------------------------------
        self.dog1_name_label = ttk.Label(master, text="Dog 1 Name:", font=font, background="#e0f7fa")
        self.dog1_name_label.pack()
        self.dog1_name_entry = ttk.Entry(master, font=font, style='TEntry.Background.TEntry')
        self.dog1_name_entry.pack()
        
        # Entry dog 1 age
        self.dog1_age_label = ttk.Label(master, text="Dog 1 Age:", font=font, background="#e0f7fa")
        self.dog1_age_label.pack()
        self.dog1_age_entry = ttk.Entry(master, font=font, style='TEntry.Background.TEntry')
        self.dog1_age_entry.pack()

        # Entry name for Dog 2 --------------------------------------------------------------------
        self.dog2_name_label = ttk.Label(master, text="Dog 2 Name:", font=font, background="#e0f7fa")
        self.dog2_name_label.pack()
        self.dog2_name_entry = ttk.Entry(master, font=font, style='TEntry.Background.TEntry')
        self.dog2_name_entry.pack()

        self.dog2_age_label = ttk.Label(master, text="Dog 2 Age:", font=font, background="#e0f7fa")
        self.dog2_age_label.pack()
        self.dog2_age_entry = ttk.Entry(master, font=font, style='TEntry.Background.TEntry')
        self.dog2_age_entry.pack()

        # Button to store the command
        self.woof_button = ttk.Button(master, text="Make Oldest Dog Woof", command=self.Info_Woof, style='TButton')
        self.woof_button.pack()

        # Output label
        self.output_label = ttk.Label(master, text="", font=font, wraplength=300, background="#e0f7fa")
        self.output_label.pack()

        # Styling for the button and entry background
        style = ttk.Style()
        style.configure('TButton', font=font, foreground='#000000', background='#00796b')  # button style
        style.configure('TEntry.Background.TEntry', background='#ffffff')  # entry background style

    #
    def Info_Woof(self):
        # Getting user input for Dog 1 and Dog 2
        dog1_name = self.dog1_name_entry.get()
        dog1_age = int(self.dog1_age_entry.get())

        dog2_name = self.dog2_name_entry.get()
        dog2_age = int(self.dog2_age_entry.get())

        # Creating Dog objects
        # using class 'Dog'
        dog1 = Dog(dog1_name, dog1_age)
        dog2 = Dog(dog2_name, dog2_age)

        # Displaying data for each dog
        self.output_label.config(text=f"Dog 1: Name - {dog1.name}, Age - {dog1.age}\n"
                                      f"Dog 2: Name - {dog2.name}, Age - {dog2.age}")

        # Making the oldest dog woof
        woof_text = Dog.oldest_dog_woof([dog1, dog2])
        self.output_label.config(text=f"{self.output_label.cget('text')}\n{woof_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
