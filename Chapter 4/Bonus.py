import tkinter as tk
from tkinter import messagebox

def calculate_stats():
    try:
        with open("Chapter 4\petrolPrice.txt", "r") as file:
            data = file.readlines()[1:]  # Skip header line
            total_cost, total_liters, under_3_5_liters = 0, 0, 0

            for line in data:
                liters, cost = map(float, line.split("\t"))
                total_cost += cost
                total_liters += liters

                if cost / liters < 3.5:
                    under_3_5_liters += liters

            cost_per_liter = total_cost / total_liters if total_liters > 0 else 0
            avg_price_per_liter = total_cost / len(data) if len(data) > 0 else 0

            result_text = (
                f"Cost of petrol per liter bought: {cost_per_liter:.2f} AED\n"
                f"Overall average price per liter: {avg_price_per_liter:.2f} AED\n"
                f"Liters bought at under 3.5 AED per liter: {under_3_5_liters:.2f} liters"
            )

            messagebox.showinfo("Results", result_text)

    except FileNotFoundError:
        messagebox.showerror(
            "File Not Found", "petrolPrice.txt not found. Please make sure the file is in the same directory as this script."
        )

# Create main window
root = tk.Tk()
root.title("Petrol Price Calculator")
root.geometry("500x200")

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_stats)
calculate_button.pack(pady=20)

# Start the tkinter event loop
root.mainloop()
