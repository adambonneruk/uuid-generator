"""Generate UUIDs using a Simple GUI"""
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import logging
import re
from generate_uuid import generate_uuid
from valid import is_reasonable_quantity

class Settings:
    """Settings for UUID Generation Class"""
    def __init__(self):
        """Initialise Application Settings Class"""
        logging.debug("Initialise Application Settings Class")
        self.quantity = 1
        self.urn_flag = False
        self.upper_flag = False
        self.namespace = ""
        self.name = ""
        self.quant_colour = "pale green"
        self.filename = ""
        self.title = ""

    def short_fn(self):
        """Return just the short name (instead of whole path) of the current_settings.filename"""
        try:
            shortfilename = re.search(r"[a-zA-Z0-9#! ._\-+\(\)]+?$", self.filename).group()
            #logging.debug("\tRegEx Match: %s", shortfilename)
        except AttributeError:
            shortfilename = ""
        return str(shortfilename)

    def window_title(self):
        """Create or Update the window title using current file name (if applicable)"""
        if self.short_fn() != "":
            title = "Unique: UUID Generator - " + self.short_fn()
        else:
            title = "Unique: UUID Generator"

        window.title(title)

def about():
    """Display About Message"""
    about_me = ["Unique: The UUID Generator",
                "Version 4.0.0",
                "MIT Licence",
                "Adam Bonner, 2020",
                "https://github.com/adambonneruk/uuid-generator"]
    messagebox.showinfo("About", "\n".join(about_me))

def empty_pta():
    """Empty the plain text area and reset the current filename"""
    plain_text_area.delete('1.0', "end")
    current_settings.filename = ""
    current_settings.window_title()

def file_load():
    """Open file dialog to select a file, then loads file into plain text area"""
    persisted_file = filedialog.askopenfile(defaultextension='.txt',
                                            mode='r',
                                            title='Select your file',
                                            filetypes=[("All Files", ".*"),
                                                       ("UUID Plain Text", ".uuid"),
                                                       ("Text Documents", ".txt")])

    if persisted_file is not None:
        empty_pta()
        text_blob = persisted_file.read()
        plain_text_area.insert('1.0', text_blob)
        persisted_file.close()

        # Saved File Settings
        current_settings.filename = str(persisted_file.name)
        logging.debug("\tFilename: %s", current_settings.filename)

        # Refresh Window Title
        current_settings.window_title()

def file_save_as():
    """Prompt for Save As File Location and Write to the File"""
    logging.debug("----------------")
    logging.debug("File: Save As...")
    logging.debug("\tOpening Save As FileDialog")
    persisted_file = filedialog.asksaveasfile(initialdir="~",
                                              defaultextension='.txt',
                                              mode='w',
                                              title="Save As",
                                              filetypes=[("Text Documents", ".txt"),
                                                         ("UUID Plain Text", ".uuid"),
                                                         ("All Files", ".*")])

    if persisted_file is not None:
        logging.debug("\tSaving...")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')
        persisted_file.write(text_blob)
        persisted_file.close()
        logging.debug("\tSaved")

        # Saved File Settings
        current_settings.filename = str(persisted_file.name)
        logging.debug("\tFilename: %s", current_settings.filename)

        # Refresh Window Title
        current_settings.window_title()

    else:
        logging.debug("\tCancelled")

def file_save():
    """Save to existing file, or Prompt for Save As if no existning file"""
    logging.debug("----------")
    logging.debug("File: Save")

    if current_settings.filename == "":
        logging.debug("\tNo File!, Launch Save As...")
        file_save_as()
    else:
        logging.debug("\tWe have a file: %s", current_settings.filename)

        # Compare text_blob to file contents
        logging.debug("\tCompare text_blob to file contents")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')
        persisted_file = open(current_settings.filename, "r")
        if text_blob == persisted_file.read():
            logging.debug("\tPlain Text Area and File Contents are the Same, No Save")
        else:
            logging.debug("\tPlain Text Area and File Contents are Different, Saving...")
            persisted_file = open(current_settings.filename, "w")
            persisted_file.write(text_blob)
            persisted_file.close()
            logging.debug("\t...Saved")

def file_new():
    """Display are you sure message before emptying window"""
    logging.debug("---------\nFile: New")
    if current_settings.filename != "":
        logging.debug("\twe have an existing savefile")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')
        persisted_file = open(current_settings.filename, "r")
        if text_blob != persisted_file.read():
            logging.debug("\tthere are changes")

            message = "Save changes to " + current_settings.short_fn() + "?"
            quit_ask = messagebox.askyesnocancel(current_settings.short_fn(), message)

            if quit_ask: #Yes
                logging.debug("\tOption: Save & New")
                empty_pta()

            elif quit_ask is None: #Cancel
                logging.debug("\tOption: Cancel")
            else: #No
                logging.debug("\tOption: New")
                empty_pta()

        else: #theres no changes
            logging.debug("\tthere are no changes")
            empty_pta()

    else:
        logging.debug("\twe don't have an existing savefile")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')
        if text_blob != "": #plain text is not empty
            quit_ask = messagebox.askyesnocancel("Untitled", "Save changes to \"Untitled\"?")
            if quit_ask: #Yes
                logging.debug("\tOption: Save & New")
                file_save()
                empty_pta()
            elif quit_ask is None: #Cancel
                logging.debug("\tOption: Cancel")
            else: #No
                logging.debug("\tOption: New")
                empty_pta()
        else: #no file, and no text area contents
            logging.debug("\tNo content in the \"Plain Text Area\" detected, Do Nothing")

def file_open(): #ctrl o
    """Display are you sure message before opening file, then load the new file in"""
    logging.debug("----------\nFile: Open")
    if current_settings.filename != "":
        logging.debug("\twe have an existing savefile")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')
        persisted_file = open(current_settings.filename, "r")
        if text_blob != persisted_file.read():
            logging.debug("\tthere are changes")

            message = "Save changes to " + current_settings.short_fn() + "?"
            quit_ask = messagebox.askyesnocancel(current_settings.short_fn(), message)

            if quit_ask: #Yes
                logging.debug("\tOption: Save & Open")
                file_load()

            elif quit_ask is None: #Cancel
                logging.debug("\tOption: Cancel")
            else: #No
                logging.debug("\tOption: Just Open")
                file_load()

        else: #theres no changes
            logging.debug("\tthere are no changes")
            file_load()

    else:
        logging.debug("\twe don't have an existing savefile")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')
        if text_blob.strip != "": #plain text is not empty
            quit_ask = messagebox.askyesnocancel("Untitled", "Save changes to \"Untitled\"?")
            if quit_ask: #Yes
                logging.debug("\tOption: Save & Open")
                file_save()
                file_load()
            elif quit_ask is None: #Cancel
                logging.debug("\tOption: Cancel")
            else: #No
                logging.debug("\tOption: Just Open")
                file_load()
        else: #no file, and no text area contents
            logging.debug("\tNo content in the \"Plain Text Area\" detected, Just Open")
            file_load()

    return "break" #fix for default ctrl + o binding

def add_uuids_to_pta(version):
    """Append a new UUID(s) to the Plain Text Area"""
    logging.debug("---------------------------------------------")
    logging.debug("Append a new UUID(s) to the \"Plain Text Area\"")

    #Settings
    logging.debug("Version: %s", str(version))
    if version == 3 or version == 5:
        logging.debug("\tNamespace:%s", str(current_settings.namespace).upper())
        logging.debug("\tName: %s", str(current_settings.name))
    logging.debug("Quantity: %s", str(current_settings.quantity))
    logging.debug("URN Prefix?: %s", str(current_settings.urn_flag))
    logging.debug("Uppercase?: %s", str(current_settings.upper_flag))

    for _ in range(0, current_settings.quantity):
        # Generate a UUID
        logging.debug("Generate a UUID:")
        generated_uuid = generate_uuid(version,
                                       current_settings.urn_flag,
                                       current_settings.namespace,
                                       current_settings.name,
                                       current_settings.upper_flag)
        logging.debug(generated_uuid)

        # Get contents of "Plain Text Area" as text_blob
        logging.debug("Get contents of \"Plain Text Area\" as text_blob")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')

        #If the "Plain Text Area" isn't Empty, Newline Required
        if text_blob != "":
            logging.debug("\"Plain Text Area\" isn't Empty, Newline Required")
            plain_text_area.insert("end", "\n")

        # Insert text_blob into Plain Text Area with new UUID
        logging.debug("Insert UUID at \"end\" of plain_text_area")
        plain_text_area.insert("end", generated_uuid)

def exit_are_you_sure():
    """Display exit message before destorying window"""
    logging.debug("----\nExit")
    if current_settings.filename != "":
        logging.debug("\twe have an existing savefile")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')
        persisted_file = open(current_settings.filename, "r")
        if text_blob != persisted_file.read():
            logging.debug("\tthere are changes")

            message = "Save changes to " + current_settings.short_fn() + "?"
            quit_ask = messagebox.askyesnocancel(current_settings.short_fn(), message)

            if quit_ask: #Yes
                logging.debug("\tOption: Save & Quit")
                file_save()
                window.destroy()
            elif quit_ask is None: #Cancel
                logging.debug("\tOption: Cancel")
            else: #No
                logging.debug("\tOption: Quit")
                window.destroy()

        else: #theres no changes
            logging.debug("\tthere are no changes")
            window.destroy()

    else:
        logging.debug("\twe don't have an existing savefile")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')
        if text_blob != "": #plain text is not empty
            quit_ask = messagebox.askyesnocancel("Quit", "Save changes to \"Untitled\"?")
            if quit_ask: #Yes
                logging.debug("\tOption: Save & Quit")
                file_save()
                window.destroy()
            elif quit_ask is None: #Cancel
                logging.debug("\tOption: Cancel")
            else: #No
                logging.debug("\tOption: Quit")
                window.destroy()
        else: #no file, and no text area contents
            window.destroy()

def options_quantity(popup):
    """Create Quantity Entry Box"""
    logging.debug("Create Quantity Entry Box")
    quant_var = tk.StringVar()

    # Log current_settings.quantity
    logging.debug("Original Quantity: %s", str(current_settings.quantity))
    quant_var.set(str(current_settings.quantity))
    current_settings.quant_colour = "pale green"

    #Create Entry Box with current colour
    quant = tk.Entry(popup, width=6, textvariable=quant_var, bg=current_settings.quant_colour)
    tk.Label(popup, text="Quantity").grid(sticky="w", padx=2, row=0, column=0)
    quant.grid(row=0, column=1, pady=8)

    def set_quant():
        """Quanitiy Set Button Pressed"""
        logging.debug("Event: Quanitiy Set Button Pressed")
        new_quant = quant_var.get()
        try:
            int(new_quant)
            logging.debug("\tValue is an Integer")
            if is_reasonable_quantity(int(new_quant)):
                logging.debug("\t...and of a reasonable quanitity")
                logging.debug("\tSaving new quanitity is current_settings")
                current_settings.quantity = int(new_quant)
                current_settings.quant_colour = "pale green"
                quant.config(bg=current_settings.quant_colour) #refresh
            else:
                logging.debug("\t...but too low or high")
                current_settings.quant_colour = "light goldenrod"
                quant.config(bg=current_settings.quant_colour) #refresh
                messagebox.showwarning("Quantity", "Value too large (1 - 65536)")
        except ValueError:
            logging.debug("\tValue is not an Integer")
            current_settings.quant_colour = "light coral"
            quant.config(bg=current_settings.quant_colour) #refresh
            messagebox.showerror("Quantity", "Value not an integer")

    button = tk.Button(popup, text="Set", command=set_quant)
    button.grid(row=0, column=2)

def options_urnprefix(popup):
    """Create URN Prefix Option Box"""
    logging.debug("Create URN Prefix Option Box")

    prefixes_var = tk.StringVar()
    prefixes = {"Disabled", "Enabled"}

    # Set and Log current_settings.urn_flag
    logging.debug("Original URN Prefix Flag: %s", str(current_settings.urn_flag))
    if current_settings.urn_flag:
        prefixes_var.set("Enabled")
    else:
        prefixes_var.set("Disabled")

    # Create Option Box
    tk.Label(popup, text="URN Prefix").grid(sticky="w", padx=2, row=1, column=0)
    prefixes_popup = tk.OptionMenu(popup, prefixes_var, *prefixes)
    prefixes_popup.grid(row=1, column=1, columnspan=2, padx=2, pady=2)

    def change_prefix(*args):
        """Changing the Prefix"""
        logging.debug("Event: Changing the URN Prefix Flag with the following arguments: %s",
                      str(args))

        current_prefix = prefixes_var.get()
        logging.debug("\tNew Selection is: %s", current_prefix)

        #Update current_settings Class
        logging.debug("\tSaving new URN Prefix Flag choice in current_settings")
        if current_prefix == "Enabled":
            current_settings.urn_flag = True
        else:
            current_settings.urn_flag = False

    prefixes_var.trace('w', change_prefix)

def options_uppercase(popup):
    """Create Uppercase Option Box"""
    logging.debug("Create Uppercase Option Box")

    uppercase_var = tk.StringVar()
    uppercase = {"Enabled", "Disabled"}

    # Set and Log current_settings.upper_flag
    logging.debug("Original Uppercase Flag: %s", str(current_settings.upper_flag))
    if current_settings.upper_flag:
        uppercase_var.set("Enabled")
    else:
        uppercase_var.set("Disabled")

    tk.Label(popup, text="Uppercase").grid(sticky="w", padx=2, row=2, column=0)
    uppercase_popup = tk.OptionMenu(popup, uppercase_var, *uppercase)
    uppercase_popup.grid(row=2, column=1, columnspan=2, padx=2, pady=2)

    def change_uppercase(*args):
        """Changing the Prefix"""
        logging.debug("Event: Changing the Uppercase Flag with the following arguments: %s",
                      str(args))

        current_uppercase = uppercase_var.get()
        logging.debug("\tNew Selection is: %s", current_uppercase)

        #Update current_settings Class
        logging.debug("\tSaving new Uppercase Flag choice in current_settings")
        if current_uppercase == "Enabled":
            current_settings.upper_flag = True
        else:
            current_settings.upper_flag = False

    uppercase_var.trace('w', change_uppercase)

def options_popup():
    """Create a Small Popup Window to Set Application Options"""
    logging.debug("------------------------------------------------------")
    logging.debug("Create a Small Popup Window to Set Application Options")
    popup = tk.Toplevel(window)
    popup.transient(window)
    popup.title("Options")
    popup.geometry("+150+150")
    popup.iconbitmap("./icon/icon.ico")

    #Quanitity Entrybox
    options_quantity(popup)

    #URN Prefix Drop Down
    options_urnprefix(popup)

    #URN Prefix Drop Down
    options_uppercase(popup)

DEBUG = True
if DEBUG:
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logging.debug("-----------------\nDEBUG MODE ACTIVE\n-----------------")

current_settings = Settings()

# Create the Window
logging.info("Create the Window")
window = tk.Tk()
#window.title(current_settings.title)
current_settings.window_title()
window.iconbitmap("./icon/icon.ico")
window.geometry("385x275+100+100")
window.wm_attributes("-topmost", 1) #always on top
window.protocol("WM_DELETE_WINDOW", exit_are_you_sure) #Close Buttom Prompt

# Create the Menu Bar
logging.debug("Create the Menu Bar")
menu_bar = tk.Menu(window)

# Load Icons
new_icon = tk.PhotoImage(file='icon/vswin2019/NewFile_16x.png')
open_icon = tk.PhotoImage(file='icon/vswin2019/OpenFile_16x.png')
save_icon = tk.PhotoImage(file='icon/vswin2019/Save_16x.png')
saveas_icon = tk.PhotoImage(file='icon/vswin2019/SaveAs_16x.png')
exit_icon = tk.PhotoImage(file='icon/vswin2019/CloseSolution_16x.png')
uuid0_icon = tk.PhotoImage(file='icon/vswin2019/LevelAll_16x.png')
uuid1_icon = tk.PhotoImage(file='icon/vswin2019/LevelOne_16x.png')
uuid3_icon = tk.PhotoImage(file='icon/vswin2019/LevelThree_16x.png')
uuid4_icon = tk.PhotoImage(file='icon/vswin2019/LevelFour_16x.png')
uuid5_icon = tk.PhotoImage(file='icon/vswin2019/LevelFive_16x.png')
options_icon = tk.PhotoImage(file='icon/vswin2019/Settings_16x.png')
about_icon = tk.PhotoImage(file='icon/vswin2019/InformationSymbol_16x.png')

# Create the File Menu
logging.debug("Create the File Menu")
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", accelerator='Ctrl+N', compound=tk.LEFT,
                      image=new_icon, underline=0, command=file_new)
file_menu.add_command(label="Open", accelerator='Ctrl+O', compound=tk.LEFT,
                      image=open_icon, underline=0, command=file_open)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound=tk.LEFT,
                      image=save_icon, underline=0, command=file_save)
file_menu.add_command(label="Save As...", compound=tk.LEFT,
                      image=saveas_icon, underline=0, command=file_save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator='Alt+F4', compound=tk.LEFT,
                      image=exit_icon, underline=0, command=exit_are_you_sure)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the Generate Menu
logging.debug("Create the Generate Menu")
uuid_menu = tk.Menu(menu_bar, tearoff=0)
uuid_menu.add_command(label="Version 1 UUID", accelerator='Ctrl+1', compound=tk.LEFT,
                      image=uuid1_icon, underline=0, command=lambda: add_uuids_to_pta(1))
uuid_menu.add_command(label="Version 4 UUID", accelerator='Ctrl+4', compound=tk.LEFT,
                      image=uuid4_icon, underline=0, command=lambda: add_uuids_to_pta(4))
uuid_menu.add_separator()
uuid_menu.add_command(label="Version 3 UUID", accelerator='Ctrl+3', compound=tk.LEFT,
                      image=uuid3_icon, underline=0, command=lambda: add_uuids_to_pta(3),
                      state="disabled")
uuid_menu.add_command(label="Version 5 UUID", accelerator='Ctrl+5', compound=tk.LEFT,
                      image=uuid5_icon, underline=0, command=lambda: add_uuids_to_pta(5),
                      state="disabled")
uuid_menu.add_separator()
uuid_menu.add_command(label="Special Nil UUID", accelerator='Ctrl+0', compound=tk.LEFT,
                      image=uuid0_icon, underline=0, command=lambda: add_uuids_to_pta(0))
menu_bar.add_cascade(label="Generate", menu=uuid_menu)

# Create the Tools Menu
logging.debug("Create the Tools Menu")
tools_menu = tk.Menu(menu_bar, tearoff=0)
tools_menu.add_command(label="Options...", accelerator='F9', compound=tk.LEFT,
                       image=options_icon, underline=0, command=options_popup)
menu_bar.add_cascade(label="Tools", menu=tools_menu)

# Create the Help Menu
logging.debug("Create the Help Menu")
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About Unique...", accelerator='F1', compound=tk.LEFT,
                      image=about_icon, underline=0, command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

# Create Plain Text Area
logging.debug("Create Plain Text Area")
plain_text_area = tk.Text(window)
scroll_bar = tk.Scrollbar(window, command=plain_text_area.yview)
plain_text_area.configure(yscrollcommand=scroll_bar.set, font=("Lucida Console", 10))
scroll_bar.pack(side='right', fill="both")
plain_text_area.pack(fill="both", expand="yes")

# Bind Keyboard Shortcuts to the Plain Text Area
window.bind_all('<Control-Key-N>', lambda event: file_new())
window.bind_all('<Control-Key-n>', lambda event: file_new())
window.bind_all('<Control-Key-S>', lambda event: file_save())
window.bind_all('<Control-Key-s>', lambda event: file_save())
window.bind_all('<Control-Key-0>', lambda event: add_uuids_to_pta(0))
window.bind_all('<Control-Key-1>', lambda event: add_uuids_to_pta(1))
window.bind_all('<Control-Key-4>', lambda event: add_uuids_to_pta(4))
window.bind('<F9>', lambda event: options_popup())
window.bind('<F1>', lambda event: about())

# Fix for Default Ctrl+O Binding
window.bind('<Control-Key-O>', lambda event: file_open())
window.bind('<Control-Key-o>', lambda event: file_open())
plain_text_area.bind('<Control-Key-o>', lambda event: file_open())
plain_text_area.bind('<Control-Key-o>', lambda event: file_open())

# Start the Window Main Loop
logging.debug("------------------------------\nStart Tkinter Window Main Loop")
window.mainloop()
logging.debug("=============================\nStop Tkinter Window Main Loop")
