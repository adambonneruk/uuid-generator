
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
import tkinter as tk
from tkinter import ttk
 
 
window = tk.Tk()
 
window.title("Python Tkinter Text Box")
window.minsize(600,400)
 
def clickMe():
    label.configure(text= 'Hello ' + name.get())
 
label = ttk.Label(window, text = "Enter Your Name")
label.grid(column = 0, row = 0)
 
 
 
 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)
 
 
button = ttk.Button(window, text = "Click Me", command = clickMe)
button.grid(column= 0, row = 2)
 
window.mainloop()