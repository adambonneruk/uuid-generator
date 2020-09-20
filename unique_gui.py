"""Generate UUIDs using a Simple GUI"""
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import logging
import re
from generate_uuid import generate_uuid
from valid import is_reasonable_quantity

class Settings:
    """Settings for UUID Generation Class
       Learning Classes from: https://www.programiz.com/python-programming/property"""
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
    """Empties the Plain Text Area (prompting to save a non-empty area first)"""
    logging.debug("---------")
    logging.debug("File: New")
    logging.debug("Getting contents of \"Plain Text Area\"")
    text_blob = plain_text_area.get('1.0', "end"+'-1c')
    logging.debug(text_blob)

    #if text_block is not empty, then prompt to save changes
    """if contents != "":
        if messagebox.askyesnocancel("Save Changes", "Do you want to Save your changes? ", default='yes'):
            savef()
        elif "no":
            text.delete('1.0', END)
        else:
            text.config(text=contents)
    """

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
    quit_ask = messagebox.askyesnocancel("Save", "Save changes to file?")
    if quit_ask:
        logging.debug("Save & Quit")
        # Save Logic Here
    elif quit_ask is None:
        logging.debug("Cancel")
    else:
        logging.debug("Quit")
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

def create_menu_bar():
    """creates the menu bar, including all menus and commands"""
    menu_bar = tk.Menu(window)

    # Create the File Menu
    logging.debug("Create the File Menu")
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=file_new)
    #file_menu.add_command(label="Open")
    file_menu.add_command(label="Save", command=file_save)
    file_menu.add_command(label="Save As...", command=file_save_as)
    #file_menu.add_separator()
    #file_menu.add_command(label="Exit", command=exit_are_you_sure)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Create the Generate Menu
    logging.debug("Create the Generate Menu")
    uuid_menu = tk.Menu(menu_bar, tearoff=0)
    uuid_menu.add_command(label="Version 1", command=lambda: add_uuids_to_pta(1))
    uuid_menu.add_command(label="Version 4", command=lambda: add_uuids_to_pta(4))
    uuid_menu.add_separator()
    uuid_menu.add_command(label="Version 3", command=lambda: add_uuids_to_pta(3), state="disabled")
    uuid_menu.add_command(label="Version 5", command=lambda: add_uuids_to_pta(5), state="disabled")
    uuid_menu.add_separator()
    uuid_menu.add_command(label="Special Nil UUID", command=lambda: add_uuids_to_pta(0))
    menu_bar.add_cascade(label="Generate", menu=uuid_menu)

    # Create the Tools Menu
    logging.debug("Create the Tools Menu")
    tools_menu = tk.Menu(menu_bar, tearoff=0)
    tools_menu.add_command(label="Options...", command=options_popup)
    menu_bar.add_cascade(label="Tools", menu=tools_menu)

    # Create the Help Menu
    logging.debug("Create the Help Menu")
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About Unique...", command=about)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    window.config(menu=menu_bar)

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
#window.protocol("WM_DELETE_WINDOW", lambda: exit_are_you_sure(window)) #Close Buttom Prompt

# Create Plain Text Area
logging.debug("Create Plain Text Area")
plain_text_area = tk.Text(window)
scroll_bar = tk.Scrollbar(window, command=plain_text_area.yview)
plain_text_area.configure(yscrollcommand=scroll_bar.set, font=("Lucida Console", 10))
scroll_bar.pack(side='right', fill="both")
plain_text_area.pack(fill="both", expand="yes")

#debugging saving
logging.debug("Current Filename: \"%s\"", current_settings.short_fn())
current_settings.quantity = 5
add_uuids_to_pta(1)

# Create the Menu Bar
logging.debug("Create the Menu Bar")
create_menu_bar()

# Start the Window Main Loop
logging.debug("------------------------------\nStart Tkinter Window Main Loop")
window.mainloop()
logging.debug("=============================\nStop Tkinter Window Main Loop")
