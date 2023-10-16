from tkinter import *

main = Tk()
main.title("GUI EXERCISE 5")
main.geometry('1366x768')
main.resizable(0,0)

l1=Label(main, text="Enter your Password:", fill=X)
b1=Button(main, text="Search", bg='red')
v = StringVar()
Checkbutton(main, text='RememberMe', variable=v, value=True,)
Entry(main, width=30)
Radiobutton(main, text=Male, variable=v, value=1)
Radiobutton(main, text=Female, variable=v, value=2)



main.mainloop()
