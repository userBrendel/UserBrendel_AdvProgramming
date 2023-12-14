# SQUARE GRID

import tkinter as tk

root = tk.Tk()
root.title("Square Grid")

# --------------------  left frame for a and b --------------------------------------------
left_frame = tk.Frame(root, bg='lightgrey', bd=5, relief=tk.GROOVE) # Frame Border of a and b
# Positioning || Frame on left
left_frame.pack(side='left', fill=tk.BOTH, expand=1) # Expandable/ The frame would adjust depending on the space available

# Creating labels A and B inside the left frame
# 'a' is inside left_frame. and left_frame is in root
a = tk.Label(left_frame, text='A', fg='white', width=12, bg='#2a2a5c') # Style of label. fg for font color
# Placing a at the top of left frame.
#Expandable from x to y axis
a.pack(side='top', fill=tk.BOTH, expand=1) 

#SAME APPROACH
b = tk.Label(left_frame, text='B', width=12, bg='white', bd=2, relief=tk.RAISED) #different border style
b.pack(side='bottom', fill=tk.BOTH, expand=1) #placing at the bottom of left_frame
 
# ------------------------- right frame --------------------------------------

right_frame = tk.Frame(root, bg='lightgrey', bd=5, relief=tk.GROOVE)
right_frame.pack(side='right', fill=tk.BOTH, expand=1) # Frame at right

# labels C and D inside the right frame
c = tk.Label(right_frame, text='C', width=12, bg='white')
c.pack(side='top', fill=tk.BOTH, expand=1)

d = tk.Label(right_frame, text='D', fg='white', width=12, bg='#2a2a5c')
d.pack(side='bottom', fill=tk.BOTH, expand=1)

root.mainloop()




