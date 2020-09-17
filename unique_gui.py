"""foobar"""
import tkinter as tk
from tkinter import messagebox
import logging
from generate_uuid import generate_uuid
from valid import is_uuid_version

class Celsius:
    """temp conversion example"""
    def __init__(self, temperature=1):
        """foobar"""
        self.temperature = temperature

    def to_fahrenheit(self):
        """foobar"""
        return (self.temperature * 1.8) + 32

class Settings:
    """store session settings as a class"""
    def __init__(self):
        """initialise class variables"""
        logging.debug("initialise settings class")
        self.set_version(4)
        self.set_quantity(1)
        self.urn_flag = False
        self.upper_flag = False
        self.namespace = ""
        self.name = ""

    # version getter
    def get_version(self):
        logging.debug("getting version from settings class")
        return self._version

    # version setter
    def set_version(self, value):
        logging.debug("setting version for settings class")
        if not is_uuid_version(value):
            raise ValueError("not a vlid uuid or somethin")
        self._version = value

    # quantity getter
    def get_quantity(self):
        logging.debug("getting quantity from settings class")
        return self._quantity

    # quantity setter
    def set_quantity(self, value):
        logging.debug("setting quantity for settings class")
        self._quantity = value

    #property objects
    version = property(get_version, set_version)
    quantity = property(get_quantity, set_quantity)


def about():
    """Display About Message"""
    about_me = ["Unique: The UUID Generator",
                "Version 4",
                "MIT Licence",
                "Adam Bonner, 2020",
                "https://github.com/adambonneruk/uuid-generator"]
    messagebox.showinfo("About", "\n".join(about_me))

def add_uuids_to_pta(version):
    """Append a new UUID to the End of the Plain Text Area"""
    # Get Plain Text Area as text_blob
    logging.debug("Get Plain Text Area as text_blob")
    text_blob = plain_text_area.get('1.0', "end"+'-1c')

    logging.debug("current_settings.quantity is " + str(current_settings.quantity))
    for _ in range(0, current_settings.quantity):
        # Generate a UUID
        logging.debug("Generate a UUID")
        new_uuid = generate_uuid(version)
        logging.debug(new_uuid)

        # Insert text_blob into Plain Text Area with new UUID
        logging.debug("Insert text_blob into Plain Text Area with new UUID")
        if text_blob != "":
            logging.debug("Plain Text Area not empty, newline required")
            plain_text_area.insert("end", "\n")
        plain_text_area.insert("end", new_uuid)

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

def onehundred():
    current_settings.quantity = 100

def create_menu_bar():
    """creates the menu bar, including all menus and commands"""
    menu_bar = tk.Menu(window)

    # Create the File Menu
    logging.debug("Create the File Menu")
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_are_you_sure)
    #menu_bar.add_cascade(label="File", menu=file_menu)

    # Create the Generate Menu
    logging.debug("Create the Generate Menu")
    uuid_menu = tk.Menu(menu_bar, tearoff=0)
    uuid_menu.add_command(label="Version 1", command=lambda: add_uuids_to_pta(1))
    uuid_menu.add_command(label="Version 4", command=lambda: add_uuids_to_pta(4))
    uuid_menu.add_separator()
    #uuid_menu.add_command(label="Version 3", command=lambda: add_uuids_to_pta(3))
    #uuid_menu.add_command(label="Version 5", command=lambda: add_uuids_to_pta(5))
    #uuid_menu.add_separator()
    uuid_menu.add_command(label="Special Nil UUID", command=lambda: add_uuids_to_pta(0))
    menu_bar.add_cascade(label="Generate", menu=uuid_menu)

    # Create the Settings Menu
    logging.debug("Create the Settings Menu")
    settings_menu = tk.Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label="Quantity", command=onehundred)
    settings_menu.add_command(label="URN Prefix")
    settings_menu.add_command(label="Uppercase")
    settings_menu.add_separator()
    settings_menu.add_command(label="Set Namespace")
    settings_menu.add_command(label="Set Name")
    menu_bar.add_cascade(label="Settings", menu=settings_menu)

    # Create the Help Menu
    logging.debug("Create the Help Menu")
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About Unique...", command=about)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    window.config(menu=menu_bar)

DEBUG = True
if DEBUG:
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logging.debug("DEBUG MODE ACTIVE")

human = Celsius()
human.temperature = 37
print(human.temperature)

current_settings = Settings()

# Create the Window
logging.debug("Create the Window")
window = tk.Tk()
window.title("Unique: UUID Generator")
window.iconbitmap("./icon/icon.ico")
window.geometry("385x275")
#window.protocol("WM_DELETE_WINDOW", lambda: exit_are_you_sure(window))

# Create Plain Text Area
logging.debug("Create Plain Text Area")
plain_text_area = tk.Text(window)
scroll_bar = tk.Scrollbar(window, command=plain_text_area.yview)
plain_text_area.configure(yscrollcommand=scroll_bar.set, font=("Lucida Console", 10))
scroll_bar.pack(side='right', fill="both")
plain_text_area.pack(fill="both", expand="yes")

# Create the Menu Bar
logging.debug("Create the Menu Bar")
create_menu_bar()

# Start the Window Main Loop
logging.debug("Start tk Window Main Loop")
window.mainloop()
logging.debug("Stop tk Window Main Loop")
