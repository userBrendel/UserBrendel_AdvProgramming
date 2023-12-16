#PLAYING AROUND CLASS
import tkinter as tk
from tkinter import ttk

class Animal: # Stores animal info
    def __init__(self, ani_type, name, color, age, weight, noise):
        self.type = ani_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise
    
    # to be used to display/return text with the data
    def sayHello(self):
        return f"Hello im {self.name}!"

    def makeNoise(self):
        return f"{self.noise}!"

    def animalDetails(self):
        details = (
            f"Type: {self.type}\n"
            f"Name: {self.name}\n"
            f"Color: {self.color}\n"
            f"Age: {self.age}\n"
            f"Weight: {self.weight}\n"
            f"Noise: {self.noise}"
        )
        return details

class widget:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Details")
        self.root.geometry("400x300")
        self.root.configure(bg='#e0f7fa') 

        # Custom font
        font = ("Arial", 12)

        # two Animal item
        # setting the details for class animal
        # setting to different variable to differentiate
        dog = Animal("Dog", "Browny", "Brown", 3, 15, "Woof")
        cat = Animal("Cat", "Tommy", "Ginger", 2, 8, "Meow")

        # Label to display output
        self.output_label = ttk.Label(root, text="", font=font, wraplength=300, background="#e0f7fa")
        self.output_label.pack()

        # Button sayHello() for Dog
        self.dog_button = ttk.Button(root, text="Say Hello Dog",
                                     command=lambda: self.display_output(dog.sayHello()), style='TButton')
        self.dog_button.pack()

        # Button  makeNoise() for Dog
        self.dog_noise_button = ttk.Button(root, text="Make Noise Dog",
                                           command=lambda: self.display_output(dog.makeNoise()), style='TButton')
        self.dog_noise_button.pack()

        # Button to display details for Dog
        self.dog_details_button = ttk.Button(root, text="Show Dog Details",
                                             command=lambda: self.display_output(dog.animalDetails()), style='TButton')
        self.dog_details_button.pack()

        # Separator/ line
        ttk.Separator(root, orient='horizontal').pack(fill='x', padx=10, pady=10)

        # Button sayHello() for Cat -------------------------------------------------------------------------
        self.cat_button = ttk.Button(root, text="Say Hello Cat", 
                                     command=lambda: self.display_output(cat.sayHello()), style='TButton')
        self.cat_button.pack()

        # Button makeNoise() for Cat
        self.cat_noise_button = ttk.Button(root, text="Make Noise Cat", 
                                           command=lambda: self.display_output(cat.makeNoise()), style='TButton')
        self.cat_noise_button.pack()

        # Button to display details for Cat
        self.cat_details_button = ttk.Button(root, text="Show Cat Details",
                                             command=lambda: self.display_output(cat.animalDetails()), style='TButton')
        self.cat_details_button.pack()

    def display_output(self, message):
        # Displaying the output on the label
        self.output_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = widget(root)
    root.mainloop()
