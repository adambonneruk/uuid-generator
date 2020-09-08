#https://codeloop.org/how-to-create-textbox-in-python-tkinter/

import tkinter as tk
 
 
window = tk.Tk()
 
window.title("Python Tkinter Text Box")
window.minsize(600,400)
 
def clickMe():
    label.configure(text= 'Hello ' + name.get())
 
label = tk.Label(window, text = "Enter Your Name")
label.grid(column = 0, row = 0)
 
 
 
 
name = tk.StringVar()
nameEntered = tk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)
 
 
button = tk.Button(window, text = "Click Me", command = clickMe)
button.grid(column= 0, row = 2)
 
window.mainloop()