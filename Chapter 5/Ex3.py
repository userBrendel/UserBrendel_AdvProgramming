#EMPLOYEE CLASS
import tkinter as tk
from tkinter import ttk

class Employee: #class for storing info
    def __init__(self):
        #Empty details/ default
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = 0

    def setData(self, name, position, salary, employee_id): # details that will be needed
        # Getting user details to put in the empty details/defauls
        self.name = name
        self.position = position
        self.salary = salary
        self.id = employee_id

    def getData(self):
        # formatting the employee data/ Data that has been set
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"

class Widget:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Details")
        self.root.geometry("400x300")
        self.root.configure(bg='#e0f7fa') 

        # Custom font
        font = ("Arial", 12)
        
        #Header title
        self.title_label = ttk.Label(root, text="Employee Data!", font=font, background="#e0f7fa")
        self.title_label.pack(pady=20)

        # for list to store employee items
        self.employee_list = []

        # Entry widgets for employee details -----------------------------------------------------
        # Name
        self.name_label = ttk.Label(root, text="Employee Name:", font=font, background="#e0f7fa")
        self.name_label.pack()
        self.name_entry = ttk.Entry(root, font=font, style='TEntry.Background.TEntry')
        self.name_entry.pack()
        
        # position
        self.position_label = ttk.Label(root, text="Employee Position:", font=font, background="#e0f7fa")
        self.position_label.pack()
        self.position_entry = ttk.Entry(root, font=font, style='TEntry.Background.TEntry')
        self.position_entry.pack()
        
        # salary
        self.salary_label = ttk.Label(root, text="Employee Salary:", font=font, background="#e0f7fa")
        self.salary_label.pack()
        self.salary_entry = ttk.Entry(root, font=font, style='TEntry.Background.TEntry')
        self.salary_entry.pack()

        # Button to add employee ---------------------------------------------------------------------------
        self.add_button = ttk.Button(root, text="Add Employee", command=self.add_employee, style='TButton')
        self.add_button.pack(pady=(20,5))

        # Button to display employees
        self.display_button = ttk.Button(root, text="Display Employees", command=self.display_employees, style='TButton')
        self.display_button.pack()

        # Output label
        self.output_label = ttk.Label(root, text="", font=font, wraplength=300, background="#e0f7fa")
        self.output_label.pack()

        # Style 
        style = ttk.Style()
        style.configure('TButton', font=font, foreground='#000000', background='#00796b') 
        style.configure('TEntry.Background.TEntry', background='#ffffff') 
        
    # for add employee button
    # Getting user entry 
    def add_employee(self): 
        # Getting user input for employee details
        name = self.name_entry.get()
        position = self.position_entry.get()
        salary = float(self.salary_entry.get())

        # employee items and set data
        employee = Employee()
        employee.setData(name, position, salary, len(self.employee_list) + 1)  # Set data for the employee items

        # Add/appending employee items to the list
        self.employee_list.append(employee)

        # Clearing entry fields when button press/ resets
        self.name_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
    
    # Display button
    def display_employees(self): # to display output
        # Display employee data in the output label
        output_text = "Name\tPosition\tSalary\tID\n" #labels of the items
        for employee in self.employee_list:
            output_text += f"{employee.getData()}\n"  # Append formatted employee data to output_text from iteration
         # Set the text for output_text
        self.output_label.config(text=output_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = Widget(root)
    root.mainloop()
