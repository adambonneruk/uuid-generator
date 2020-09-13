import tkinter as tk
from tkinter import messagebox

def quit(window):
	if tk.messagebox.askyesno("Quit", "Quit without Saving?"):
		window.destroy()

def about(window):
	aboutMe = ["Unique: The UUID Generator", 'Adam Bonner, 2020', 'MIT Licence', 'https://github.com/adambonneruk/uuid-generator']
	messagebox.showinfo("About", "\n".join(aboutMe))