import tkinter as tk

def count_strings():
    # getting what the user what to search and storing it with a variable
    first_search = First_entry.get().strip()
    add_search = add_search_entry.get().strip()

    # Checking if first_search is provided
    if first_search:
            with open("Chapter 4\sentences.txt", "r") as file: # Opening the file for reading and setting its name as 'file'
                # To read the content of the text file
                text_file = file.read()
                # Making a variable to store the first_search string occurrence with '.count' in a case-insensitive manner
                count_strings = text_file.lower().count(first_search.lower())

                # Additional search handling
                if add_search:
                    # If add_search is provided, it will count its occurrences as well
                    count_strings += text_file.lower().count(add_search.lower()) # it will add with the count of first_search
                # Displaying the result in the result_label
                result_label.config(text=f"The word appears {count_strings} times.") 

    else:
        result_label.config(text="Please enter a search string.")


# main window -----------------------------------------------------------------
root = tk.Tk()
root.title("String Occurrence Counter")
root.geometry("400x250")

# Widgets ---------------------------------------------------------------------
# labels and entry fields
label_entry = tk.Label(root, text="Enter word to search:", font=(15))
label_entry.pack()

First_entry = tk.Entry(root)
First_entry.pack()

label_free_search = tk.Label(root, text="Enter another word to Search:")
label_free_search.pack()

add_search_entry = tk.Entry(root)
add_search_entry.pack()

# button
# Command is in store here
button_count = tk.Button(root, text="Count Strings", command=count_strings)  
button_count.pack()

# label to display result
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()


root.mainloop()
