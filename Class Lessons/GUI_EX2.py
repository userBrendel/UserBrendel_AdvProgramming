from tkinter import *

app = Tk()
app.title("GUI EXAMPLE 2")

label1 = Label(app, text="Changed text")
label1.pack(side='bottom')

button1 = Button(app, text="Click Me")
button1.pack(side='bottom')

app.mainloop()
