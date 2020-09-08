#https://pythonbasics.org/tkinter-frame/
from tkinter import *  
root = Tk()  

for fm in ['blue','red','yellow','green','white','black','purple','blue','red','yellow','green','white','black','purple']:  
    Frame(height = 20,width = 640,bg = fm).pack()  
root.mainloop() 