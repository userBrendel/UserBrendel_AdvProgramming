from tkinter import *

root=Tk()
root.title("Widget Example")

mylabel = Label(root, text="I am a label widget")
mylabel.pack()

mybutton = Button(root, text="I am a button")
mybutton.pack(side=LEFT)

root.geometry('350x200')

root.mainloop()