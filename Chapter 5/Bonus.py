# Playing with class extension

# Instead of have the info already in stored, this program will ask user for  input
import tkinter as tk
from tkinter import ttk

#Same functions used
class Animal:
    def __init__(self, ani_type, name, color, age, weight, noise):
        self.type = ani_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise
    
    def sayHello(self):
        return f"Hello, I'm {self.name}!"

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

class Widget:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Details")
        self.root.geometry("400x300")
        self.root.configure(bg='#e0f7fa') 

        font = ("Arial", 12)
        
        #Instead of this:
        # dog = Animal("Dog", "Browny", "Brown", 3, 15, "Woof")
        # cat = Animal("Cat", "Tommy", "Ginger", 2, 8, "Meow")

        # I Asked the user to enter values for an animal:
        ani_type = input("Enter the type of animal: ")
        name = input("Enter the name of the animal: ")
        color = input("Enter the color of the animal: ")
        age = int(input("Enter the age of the animal: "))
        weight = float(input("Enter the weight of the animal: "))
        noise = input("Enter the noise the animal makes: ")

        # Putting the instance of the Animal class with user-input values
        user_animal = Animal(ani_type, name, color, age, weight, noise)

        # Label to display output
        self.output_label = ttk.Label(root, text="", font=font, wraplength=300, background="#e0f7fa")
        self.output_label.pack()

        # Buttons to interact with the user-input animal
        self.say_hello_button = ttk.Button(root, text=f"Say Hello {user_animal.type}", command=lambda: self.display_output(user_animal.sayHello()), style='TButton')
        self.say_hello_button.pack()

        self.make_noise_button = ttk.Button(root, text=f"Make Noise {user_animal.type}", command=lambda: self.display_output(user_animal.makeNoise()), style='TButton')
        self.make_noise_button.pack()

        self.show_details_button = ttk.Button(root, text=f"Show {user_animal.type} Details", command=lambda: self.display_output(user_animal.animalDetails()), style='TButton')
        self.show_details_button.pack()

    def display_output(self, message):
        # Displaying the output on the label
        self.output_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = Widget(root)
    root.mainloop()
