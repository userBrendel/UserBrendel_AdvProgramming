#REGISTRATION FORM

import tkinter as tk
from tkinter import ttk  # modern tkinter|| for dropbox

#  FOR SUBMIT BUTTON
# Defining a function
 # To be used later on as command
def on_submit():
    print("Submitted!") # Will print

# FOR CLEAR BUTTON
 # To be used later on as command
def on_clear():
    #clearing the entry and check boxes
    name_entry.delete(0, 'end')
    mobile_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    gender_dropdown.set('')
    course_var.set('')
    english.set(False)
    tagalog.set(False)
    hindu.set(False)

root = tk.Tk()
root.title('Register')
root.geometry('600x1000')

# adding  image
header_img = tk.PhotoImage(file=r"Chapter 2\university.png")
header_img = header_img.subsample(5, 5)  # used to reduce the size of the image

#  a frame for the header with a background color
header_frame = tk.Frame(root, bg="#071a33" )
header_frame.grid(row=0, column=0, columnspan=3, sticky="ew",  pady=(20, 20))

# Header with the image
Header = tk.Label(header_frame, image=header_img, bg="#071a33")
Header.image = header_img
Header.grid(row=0, column=0, sticky="w")  # Use sticky="w" to align to the left



# Frame of everything inside the form
frame = tk.Frame(root, bg='lightgrey', padx=30, pady=10) 
frame.grid(columnspan=3)

# Configuring column for the header and frame label to expand horizontally
 # I used this method to specify how much space a column should occupy concerning the available horizontal space.
for i in range(3):
    root.columnconfigure(i, weight=1)

# --------------------------------- Inside the frame ---------------------------
# Title label
label_title = tk.Label(frame, text="Student Management System", bg="lightgrey", font=('Arial', 18, 'bold'))
label_title.grid(row=0, column=0, columnspan=3, pady=5) # starting point position

# New label below 'label_title'
label_2_title = tk.Label(frame, text="New Student Registration", bg="lightgrey", font=('Monospace', 15,))
label_2_title.grid(row=1, column=0, columnspan=3, pady=(4, 15)) # next row to the first label/ underneath. 
#pad-y used for spacing y axis of the label

# Student name
name_label = tk.Label(frame, text="Student Name", bg="lightgrey")
name_label.grid(row=2, column=0, pady=5) # Next row
name_entry = tk.Entry(frame)
name_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="ew")   # same row different column || taking up 2 columnspan

# Mobile number 
 # Notice how grid attribute change for the following 
mobile_label = tk.Label(frame, text="Mobile Number", bg="lightgrey")
mobile_label.grid(row=3, column=0, pady=5)
mobile_entry = tk.Entry(frame)
mobile_entry.grid(row=3, column=1, columnspan=2, pady=5, sticky="ew")  

# Email ID
email_label = tk.Label(frame, text="Email ID", bg="lightgrey")
email_label.grid(row=4, column=0, pady=5)
email_entry = tk.Entry(frame)
email_entry.grid(row=4, column=1, columnspan=2, pady=5, sticky="ew")  

# Home address
address_label = tk.Label(frame, text="Home Address", bg="lightgrey")
address_label.grid(row=5, column=0, pady=5)
address_entry = tk.Entry(frame)
address_entry.grid(row=5, column=1, columnspan=2, pady=5, sticky="ew") 

# Gender label
gender_label = tk.Label(frame, text="Gender", bg="lightgrey")
gender_label.grid(row=6, column=0, pady=5)

# Gender dropdown || This is different from entry
gender_var = tk.StringVar()  # A variable to store the selected gender and to specify its data type
gender_options = ['Male', 'Female', 'Other']  # List / Options for the dropdown
gender_dropdown = ttk.Combobox(frame, textvariable=gender_var, values=gender_options, state='readonly')
# Creating a Combobox with the  variable and value
# state='read only' is to prevent user from typing 

gender_dropdown.grid(row=6, column=1, columnspan=2, pady=5, sticky="ew") # position
 

# Course Enrolled label
course_label = tk.Label(frame, text="Course Enrolled", bg="lightgrey")
course_label.grid(row=7, column=0, pady=5)

# Course radio buttons with circles on the right 
 # Same method for storing variable and list
course_var = tk.StringVar()
course_options = ['BSc CC', 'BSc CY', 'BSc PSY', 'BA & BM']

for i, option in enumerate(course_options): #  iterates over the course options and their corresponding index 
    # Creating the Radiobutton  with the specified text, variable, and value
    radio_button = tk.Radiobutton(frame, text=option, variable=course_var, value=option, bg="lightgrey")
    # The row position is calculated based on the loop index, adding 7 + i to the base row position. 
    radio_button.grid(row=7 + i, column=1, pady=5, sticky="w")  # Adjusting the row position

# Language Known label
Language_label = tk.Label(frame, text="Language Known", bg="lightgrey")
Language_label.grid(row=11, column=0, pady=5) # Radio button took up to 7-10 row so therefore we are now on the 11th row

# Language checkboxes
english = tk.BooleanVar()
english_box = tk.Checkbutton(frame, text="English", variable=english, bg="lightgrey")
english_box.grid(row=11, column=1, pady=5, sticky="w")

tagalog = tk.BooleanVar()
tagalog_box = tk.Checkbutton(frame, text="Tagalog", variable=tagalog, bg="lightgrey")
tagalog_box.grid(row=11, column=2, pady=5, sticky="w")

hindu = tk.BooleanVar()
hindu_box = tk.Checkbutton(frame, text="Hindu/Urdu", variable=hindu, bg="lightgrey")
hindu_box.grid(row=12 + 1, column=1, pady=5, sticky="w")

# Communication skill rating label
com_label = tk.Label(frame, text="Rate your English communication skills", bg="lightgrey")
com_label.grid(row=14, column=0, columnspan=3, pady=5, sticky="ew")

# Scale widget for rating skills
 # That has a minimum of 0 and maximum of 10. The scale is horizontal and has a length of 300
 # 'sliderlength=20' The length of the slider (the draggable part) is set to 20 pixels.
 # The variable associated with the scale is set to a DoubleVar(), which is a Tkinter variable that can store floating-point values.
scale = tk.Scale(frame, bg='lightgrey', from_=0, to=10, orient="horizontal", 
                                      length=300, sliderlength=20, variable=tk.DoubleVar(),)
scale.grid(row=15, column=0, columnspan=3, pady=5, sticky="ew")

#------------------------------- Buttons ---------------------------------------------
#  a submit button inside the frame
 # Using the function that was made earlier as command
 # When button clicked it would execute
submit_button = tk.Button(frame, text='Submit', command=on_submit,  bg='#295c8c', fg='white')
submit_button.grid(row=16, column=0, columnspan=1, pady=20, sticky="ew")  

#  a clear button inside the frame
clear_button = tk.Button(frame, text='Clear', command=on_clear, bg='#295c8c', fg='white')
clear_button.grid(row=16, column=2, columnspan=1, pady=20, sticky="ew") 
root.mainloop()



































