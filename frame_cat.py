#https://pythonbasics.org/tkinter-frame/
import tkinter as tk

root = tk.Tk()

textLabel = tk.Label(root,
                  text="Label",
                  justify=tk.LEFT,
                  padx=10)
textLabel.pack(side=tk.LEFT)

photo = tk.PhotoImage(file="cat.png")
imgLabel = tk.Label(root, image=photo)
imgLabel.pack(side=tk.LEFT)

tk.mainloop()