from tkinter import *

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.title('Unique: The UUID Generator') #https://stackoverflow.com/questions/33637292/change-tkinter-frame-title
root.minsize(800,600)
root.iconbitmap('./icon/icon.ico') #https://www.delftstack.com/howto/python-tkinter/how-to-set-window-icon-in-tkinter/
root.mainloop()