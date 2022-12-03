from tkinter import *

window = Tk()
window.title("Python GUI using TKINTER")

window.geometry('450x450')

lbl = Label(window, text="Starting with TKINTER",fg="green")
lbl.grid(row=0, column=0)


def clicked():
    lbl.configure(text="I just got clicked")
bt= Button(window, text = "Click me" ,fg = "red",bg="black",command=clicked)
bt.grid(row=0,column=1)

window.mainloop()