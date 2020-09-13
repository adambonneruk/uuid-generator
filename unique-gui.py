import tkinter as tk
from tkinter import simpledialog
import logging

from toast import quit, about
from generate_uuid import generate_uuid

debug = True
if debug:
	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
	logging.debug("DEBUG MODE ACTIVE")

# Default the number of UUIDs generated to 0, to prompt question
uuidCount = 0

# Create the Window
window = tk.Tk()
window.title("Unique: UUID Generator")
window.iconbitmap("./icon/icon.ico")
window.geometry("310x275")

def insertUuid(version=4):
	global uuidCount
	if uuidCount == 0:
		quantity()
	for i in range(0,uuidCount):
		plainText = plainTextArea.get('1.0', "end"+'-1c')
		uuid = generate_uuid(version)
		if plainText != "":
			plainTextArea.insert("end","\n")
		plainTextArea.insert("end",uuid)

#Create Text Area
plainTextArea = tk.Text(window)
scrollBar = tk.Scrollbar(window, command=plainTextArea.yview)
plainTextArea.configure(yscrollcommand=scrollBar.set,font=("Lucida Console", 10))
scrollBar.pack(side='right', fill="both")
plainTextArea.pack(fill="both", expand="yes")

# Create the Top Menu Bar
menuBar = tk.Menu(window)

fileMenu = tk.Menu(menuBar,tearoff=0)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As...")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=lambda: quit(window))
menuBar.add_cascade(label="File", menu=fileMenu)

def quantity():
	global uuidCount
	uuidCount = simpledialog.askinteger("UUID Quantity", "Configure Number of UUIDs to Generate")

uuidMenu = tk.Menu(menuBar,tearoff=0)
#uuidMenu.add_command(label="Version 0")
#uuidMenu.add_command(label="Version 1")
uuidMenu.add_command(label="Version 0",command=lambda: insertUuid(0))
uuidMenu.add_command(label="Version 1",command=lambda: insertUuid(1))
uuidMenu.add_command(label="Version 4",command=lambda: insertUuid())
#uuidMenu.add_separator()
#uuidMenu.add_command(label="Version 3")
#uuidMenu.add_command(label="Version 5")
menuBar.add_cascade(label="Generate UUIDs", menu=uuidMenu)

configMenu = tk.Menu(menuBar,tearoff=0)
configMenu.add_command(label="Quantity",command=lambda: quantity())
menuBar.add_cascade(label="Configuration", menu=configMenu)

helpMenu = tk.Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About",command=lambda: about(window))
menuBar.add_cascade(label="Help", menu=helpMenu)

window.config(menu=menuBar)

# Start the Window Main Loop
window.mainloop()