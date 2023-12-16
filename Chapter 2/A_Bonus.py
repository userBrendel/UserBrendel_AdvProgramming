import tkinter as tk
from tkinter import ttk

# Function to convert Celsius to Fahrenheit
def c_to_f(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to handle the conversion button click
def convert():
    try:
        # Getting the entered temperature of user and setting it as float
        temperature = float(entry_temperature.get())

        # Checking/condition of the selected conversion type
        if var_temperature.get() == "Celsius to Fahrenheit": # if c_to_f
            result = c_to_f(temperature)  # formula
            result_label.config(text=f"Result: {result:.2f} °F")# outcome
            
        elif var_temperature.get() == "Fahrenheit to Celsius":
            result = f_to_c(temperature)
            result_label.config(text=f"Result: {result:.2f} °C")
            
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# WIDGETS -------------------------------------------------------------------------------
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x300")
root.configure(bg="#e0e0e0")

# Frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, padx=20, pady=20)
frame.configure(relief="solid", borderwidth=2)

# Label for temperature entry
label_temperature = ttk.Label(frame, text="Enter Temperature:", font=(15))
label_temperature.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Entry widget for temperature input
entry_temperature = ttk.Entry(frame)
entry_temperature.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Variable to track the selected conversion type
var_temperature = tk.StringVar()
var_temperature.set("Celsius to Fahrenheit")

# Radio button for Celsius to Fahrenheit conversion
radio_c_to_f = ttk.Radiobutton(frame, text="Celsius to Fahrenheit", variable=var_temperature, 
                               value="Celsius to Fahrenheit")
radio_c_to_f.grid(row=2, column=0, columnspan=2, pady=(0, 10))

# Radio button for Fahrenheit to Celsius conversion
radio_f_to_c = ttk.Radiobutton(frame, text="Fahrenheit to Celsius", variable=var_temperature,
                               value="Fahrenheit to Celsius")
radio_f_to_c.grid(row=3, column=0, columnspan=2, pady=(0, 10))

# Button to trigger the conversion
button_convert = ttk.Button(frame, text="Convert", command=convert)
button_convert.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Label to display the result
result_label = ttk.Label(frame, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2, pady=(0, 10))


root.mainloop()

