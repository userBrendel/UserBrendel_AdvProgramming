#MANAGING LAYOUT
import tkinter as tk

root = tk.Tk()
root.title("GUI Box")

# Different label for each box
# A text with background color and a border style with 'relief.'  'bd' for border width
A = tk.Label(root, text="A", width=12, bg='red', relief=tk.GROOVE, bd=5) 
B = tk.Label(root, text="B", width=12,  bg='yellow', relief=tk.RAISED, bd=2) # Different border style.
C = tk.Label(root, text="C", width=12, bg='blue',)
D = tk.Label(root, text="D", width=12, bg='white', )

# Adding positioning and layout information with .pack before adding the label to the root
# 'A' label will be at the top. 
# Fill x is to specific how the box would expand in a x or horizontal way.
# expand = 1 is to specify that the box should expand. default is expand = 0 || not expandable
A.pack(side='top', fill=tk.X, expand=1) 
B.pack(side='bottom')
C.pack(side='left', fill=tk.Y, expand=True)  # Expands at y axis. Expand = true is similar to expand = 1
D.pack(side='right')

root.mainloop()
