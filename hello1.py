#https://effbot.org/tkinterbook/tkinter-hello-tkinter.htm

from tkinter import *

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()