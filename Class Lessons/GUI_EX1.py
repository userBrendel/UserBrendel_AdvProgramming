from tkinter import *
root=Tk()
root.title('Exercise1')
root.geometry('200x200')

def click():
    print('WOW')
mybutton= Button(root, text="click this button", command=click)   
mybutton.pack(side=BOTTOM) 

root.mainloop()
