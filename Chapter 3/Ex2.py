# COFFEE VENDING MACHINE

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk # Module to add images

class CoffeeShop:
    # setting up various variables (coffee_var, sugar_var, milk_var, cream_var, money_var) to track the user's choices.
    def __init__(self, root): 
        self.root = root
        self.root.title("Coffee Vending Machine")

# Variables and dictionaries -------------------------------------------------------------------
        # setting a variable to define its data type and to be used in 'textvariable' to get the input of user in entry.
        self.coffee_var = tk.StringVar()
        self.sugar_var = tk.IntVar()
        self.milk_var = tk.IntVar()
        self.cream_var = tk.IntVar()
        self.money_var = tk.DoubleVar() # for floating point

    # dictionary coffee_options for different types of coffee and their prices
        self.coffee_options = {
            "Espresso": 10.5,
            "Latte": 8.0,
            "Cappuccino": 5.5,
            "Black Coffee": 6.0
        }
        
    # dictionary for storing image paths for each type of coffee.
        self.coffee_img = {
            "Espresso": "chapter 3/images/espresso.jpg",
            "Latte": "chapter 3/images/latte.jpg",
            "Cappuccino": "chapter 3/images/cappuccino.jpg",
            "Black Coffee": "chapter 3/images/black coffee.jpg"
        }

        # Additional charge for cream
        self.cream_additional_charge = 0.5
        
        # setting up the GUI when an instance of the CoffeeShop class is created.
        # Creating the GUI || Any UI elements
        self.widget()

    def widget(self): # Consist of every widget displayed
        coffee_label = tk.Label(self.root, text="Select your coffee", font=("Helvetica", 25))
        coffee_label.pack(pady=10)
 
    # Making combobox for coffee_options
        # Using the variable made earlier to display text 
        # When the user interacts with the widget, the associated variable's value is automatically updated.
        # It will change to the variable also update the widget.
        coffee_combobox = ttk.Combobox(self.root, textvariable=self.coffee_var,
                                       values=list(self.coffee_options.keys()), state="readonly")
           
        # bind method associates the update method with the "ComboboxSelected" event
        # so when the user selects a coffee, the update method is called
        # It will update picture and price when a item in combobox is selected
          # 'self.update' will be under the code
        coffee_combobox.pack(pady=10)
        coffee_combobox.bind("<<ComboboxSelected>>", self.update)

        self.coffee_image_label = tk.Label(self.root)
        self.coffee_image_label.pack()


# setting the type of variables with the respective widgets --------------------------------------------------------------------
    # Addition for coffee checkboxes
        sugar_check = ttk.Checkbutton(self.root, text="Add Sugar", variable=self.sugar_var)
        sugar_check.pack(pady=5)

        milk_check = ttk.Checkbutton(self.root, text="Add Milk", variable=self.milk_var)
        milk_check.pack(pady=5)
        
        #update command for cream additional charge
        cream_check = ttk.Checkbutton(self.root, text="Add Cream (+$0.50)", variable=self.cream_var,
                                      command=self.update)
        cream_check.pack(pady=5)
    
    # Money
        money_label = tk.Label(self.root, text="Insert Money ($)", font=("Helvetica", 12))
        money_label.pack(pady=10)

        money_entry = ttk.Entry(self.root, textvariable=self.money_var, font=("Helvetica", 12))
        money_entry.pack(pady=10)

        cost_label = tk.Label(self.root, text="Cost: $0.0", font=("Helvetica", 12))
        cost_label.pack(pady=10)

    #Button
      # A command when user press button
        order_button = ttk.Button(self.root, text="Place Order", command=self.place_order)
        order_button.pack(pady=20)

        # references to the cost label and money entry
        self.cost_label = cost_label
        self.money_entry = money_entry
        
    # For the button command || when the button is press this function will execute.    
    def place_order(self): 
        # variables that will be use to display text accordingly in the message box
        coffee = self.coffee_var.get() # Coffee the user choose       
        # if user pick with sugar a message 'with sugar' would appear. 
          # If  not it will be blank  
        sugar = "with Sugar" if self.sugar_var.get() else ""                                                                   
        milk = "with Milk" if self.milk_var.get() else ""
        cream = "with Cream" if self.cream_var.get() else ""
        # sets a variable to define data type and It has been updated with 'money_entry.'
        money_inserted = self.money_var.get() # Gets the amount of money inserted from 'money_var.' 
        
        # Calculating the total cost, checks for sufficient funds--------------------------------------
        # Check if a coffee type is selected
        if coffee:
            # Checks if coffee is in the dictionary. 
            if coffee in self.coffee_options: 
                # Setting a variable to handle price. Getting price from the dictionary
                coffee_price = self.coffee_options[coffee]
                # Checks if the user has selected the option to add cream
                if self.cream_var.get():
                # If cream is selected, the additional charge for cream will add to 'coffee_price'
                 coffee_price += self.cream_additional_charge
                # Incase the user have a change:
                # Setting a variable that Calculates the change.
                change = money_inserted - coffee_price # subtracting money inserted by the entry with the coffee price
                
                # Setting up the messagebox when every variable is set to display data.
                if change >= 0: 
                    order_message = f"Enjoy your {coffee}!"

                    order_message += f" {sugar} {milk} {cream}"

                    order_message += f"\nChange: ${change:.2f}"
                    messagebox.showinfo("Order Successful", order_message)
                    
                    # Reset the following when order made
                    self.coffee_var.set("")
                    self.sugar_var.set(0)
                    self.milk_var.set(0)
                    self.cream_var.set(0)
                    self.money_var.set(0.0)
                    self.update_cost_label("")  
        
        # displaying an error message using messagebox, incase of user not having enough funds and invalid selection
                else:
                    messagebox.showerror("Insufficient Funds", "Please insert sufficient money for your order.")
            else:
                messagebox.showerror("Invalid Coffee Type", "Please select a valid coffee type.")
        else:
            messagebox.showerror("No Coffee Selected", "Please select a coffee type.")
            
    def update(self, event=None): # For changing images and updating cost label
      # Getting the currently selected coffee type from the coffee_var
       selected_coffee = self.coffee_var.get()
       # if the selected coffee type in the dictionary 'coffee_img'
       if selected_coffee in self.coffee_img:
        image_path = self.coffee_img[selected_coffee] # Variable that gets the image path for the selected coffee type
        coffee_image = self.load_image(image_path)  # Load and resize the image using the load_image method
        self.coffee_image_label.configure(image=coffee_image)  # Configuring the coffee_image_label to display the loaded image
        self.coffee_image_label.image = coffee_image # Set the image attribute of coffee_image_label to the loaded image
        self.update_cost_label(selected_coffee) # Updating the cost label based on the selected coffee type

       else:
        # If the selected coffee type has no associated image, clear the image_label
        self.coffee_image_label.configure(image="")

        # Update the cost label with an empty string as no coffee type is selected
        self.update_cost_label("")
        
        
    def load_image(self, path, size=(300,300)): # Resizing images
      img = Image.open(path)
      img = img.resize(size)
      img = ImageTk.PhotoImage(img)
      return img
    

    def update_cost_label(self, coffee): # updating 'cost_label' text
        if coffee in self.coffee_options:
            cost = self.coffee_options[coffee]
            # Additional charge for cream
            if self.cream_var.get():
                cost += self.cream_additional_charge
            self.cost_label.config(text=f"Cost: ${cost:.2f}") 
        else:
            self.cost_label.config(text="Cost: $0.0")



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    app = CoffeeShop(root)
    root.mainloop()





