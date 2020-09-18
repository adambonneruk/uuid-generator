"""gui-based version of unique uuid generator tool"""
import tkinter as tk
from tkinter import messagebox, simpledialog
import logging
import re

from generate_uuid import generate_uuid

DEBUG = False
if DEBUG:
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logging.debug("DEBUG MODE ACTIVE")

def are_you_sure():
    """Display Exit Message before destorying Window"""
    if tk.messagebox.askyesno("Quit", "Exit Tool?"):
        window.destroy()

def about():
    """Display About Message"""
    about_me = ["Unique: The UUID Generator", 'Adam Bonner, 2020', 'MIT Licence', 'https://github.com/adambonneruk/uuid-generator']
    messagebox.showinfo("About", "\n".join(about_me))

def setQuantity():
    global uuidCount
    uuidCount = simpledialog.askinteger("UUID Quantity", "Configure Number of UUIDs to Generate")
    logging.debug(uuidCount)

def setNamespace():
    global namespace
    namespace = simpledialog.askstring("Namespace", "Set the Required Namespace (e.g. DNS)")
    namespace = namespace.lower()
    logging.debug(namespace)

def setName():
    global name
    name = simpledialog.askstring("Name/Value", "Set the Required Name/Value (e.g. python.org)")
    logging.debug(name)

def setUppercase():
    global uppercase
    if messagebox.askyesnocancel("Uppercase UUID", "Set Uppercase for UUID Generation? ", default="no"):
        uppercase = True
    elif "no":
        uppercase = False
    else:
        pass

def setUrnPrefix():
    global urnprefix
    if messagebox.askyesnocancel("UUID URN Prefix", "Set Prefix for URN:UUID Generation? ", default="no"):
        urnprefix = True
    elif "no":
        urnprefix = False
    else:
        urnprefix = uppercase

def insertUuid(version=4):

    if uuidCount == 0:
        setQuantity()

    for _ in range(0,uuidCount):
        plainText = plainTextArea.get('1.0', "end"+'-1c')

        if version == 3 or version == 5: #ask for namespace and name

            while not re.search(r"^(DNS|URL|OID|X500)$",str(namespace).upper()):
                setNamespace()
            if name == "":
                setName()

        uuid = generate_uuid(version,urnprefix,namespace,name,uppercase)

        if plainText != "":
            plainTextArea.insert("end","\n")
        plainTextArea.insert("end",uuid)

# Default the number of UUIDs generated to 0, to prompt question
uuidCount = 0
uppercase = False
urnprefix = False
namespace = ""
name = ""

# Create the Window
window = tk.Tk()
window.title("Unique: UUID Generator")
window.iconbitmap("./icon/icon.ico")
window.geometry("385x275")

#Create Text Area
plainTextArea = tk.Text(window)
scrollBar = tk.Scrollbar(window, command=plainTextArea.yview)
plainTextArea.configure(yscrollcommand=scrollBar.set,font=("Lucida Console", 10))
scrollBar.pack(side='right', fill="both")
plainTextArea.pack(fill="both", expand="yes")

# Create the Top Menu Bar
menuBar = tk.Menu(window)

fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As...")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=lambda: are_you_sure())
menuBar.add_cascade(label="File", menu=fileMenu)

uuidMenu = tk.Menu(menuBar, tearoff=0)
uuidMenu.add_command(label="Version 4", command=lambda: insertUuid())
uuidMenu.add_separator()
uuidMenu.add_command(label="Version 1", command=lambda: insertUuid(1))
uuidMenu.add_separator()
uuidMenu.add_command(label="Version 3", command=lambda: insertUuid(3))
uuidMenu.add_command(label="Version 5", command=lambda: insertUuid(5))
uuidMenu.add_separator()
uuidMenu.add_command(label="Special Nil UUID", command=lambda: insertUuid(0))
menuBar.add_cascade(label="Generate UUIDs", menu=uuidMenu)

configMenu = tk.Menu(menuBar,tearoff=0)
configMenu.add_command(label="Quantity", command=lambda: setQuantity())
configMenu.add_command(label="URN Prefix", command=lambda: setUrnPrefix())
configMenu.add_command(label="Uppercase", command=lambda: setUppercase())
configMenu.add_separator()
configMenu.add_command(label="Version 3/5 Only",state="disabled")
configMenu.add_command(label="Set Namespace", command=lambda: setNamespace())
configMenu.add_command(label="Set Name", command=lambda: setNamespace())
menuBar.add_cascade(label="Configuration", menu=configMenu)

helpMenu = tk.Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About", command=lambda: about())
menuBar.add_cascade(label="Help", menu=helpMenu)

window.config(menu=menuBar)

# Start the Window Main Loop
window.mainloop()
