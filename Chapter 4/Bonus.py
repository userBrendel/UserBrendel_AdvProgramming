import tkinter as tk
from tkinter import messagebox

def stats(): # Function for command
        # Opening the file for reading
        with open("Chapter 4\petrolPrice.txt", "r") as file:
            # Read all lines from the file, skipping the header line
            data = file.readlines()[1:]  

            # variables that will store calculations
            total_cost, total_liters, under_liters = 0, 0, 0

            # Iterate through each line in the file
            for line in data:
                # Splitting the line into liters and cost using tab as a separator
                liters, cost = map(float, line.split("\t"))
                
                # total cost and total liters from file
                total_cost += cost # will contain the sum of all petrol costs
                total_liters += liters # will contain the sum of all liters purchased

                # if the cost per liter is less than 3.5 AED
                if cost / liters < 3.5:
                    under_liters += liters

            # Calculate cost per liter, average price per liter, and display results
            cost_per_liter = total_cost / total_liters if total_liters > 0 else 0
            avg_price_per_liter = total_cost / len(data) if len(data) > 0 else 0

            # strings with the calculated results
            # used to display info
            result_text = (
                f"Cost of petrol per liter bought: {cost_per_liter:.2f} AED\n"
                f"Overall average price per liter: {avg_price_per_liter:.2f} AED\n"
                f"Liters bought at under 3.5 AED per liter: {under_liters:.2f} liters"
            )

            # Show an info dialog with the results
            messagebox.showinfo("Results", result_text)


# main window
root = tk.Tk()
root.title("Petrol Price Calculator")
root.geometry("500x200")

# calculate button
calculate_button = tk.Button(root, text="Calculate", command=stats) # Command
calculate_button.pack(pady=20)

root.mainloop()
