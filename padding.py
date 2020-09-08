import tkinter as tk

class MyApp():
    def __init__(self):
        self.root = tk.Tk()
        l1 = tk.Label(self.root, text="Hello")
        l2 = tk.Label(self.root, text="World")
        l1.grid(row=0, column=0, padx=(100, 10))
        l2.grid(row=1, column=0, padx=(10, 100)) 

app = MyApp()
app.root.mainloop()