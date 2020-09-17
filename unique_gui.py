"""foobar"""
import tkinter as tk
from tkinter import messagebox
import logging
from generate_uuid import generate_uuid
from valid import is_reasonable_quantity

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
        self.quantity = 1
        self.urn_flag = False
        self.upper_flag = False
        self.namespace = ""
        self.name = ""
        self.quant_colour = "pale green"

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
    logging.debug("----------------------------------------")
    logging.debug("generating uuid(s), heres some settings:")
    logging.debug("current_settings.urn_flag is %s", str(current_settings.urn_flag))
    logging.debug("current_settings.namespace is %s", str(current_settings.namespace))
    logging.debug("current_settings.name is %s", str(current_settings.name))
    logging.debug("current_settings.upper_flag is %s", str(current_settings.upper_flag))
    logging.debug("...and im going to do it %s times", str(current_settings.quantity))
    logging.debug("...afor a version %s uuid", str(version))

    for _ in range(0, current_settings.quantity):
        # Get Plain Text Area as text_blob
        logging.debug("Get Plain Text Area as text_blob")
        text_blob = plain_text_area.get('1.0', "end"+'-1c')

        # Generate a UUID
        logging.debug("Generate a UUID")
        generated_uuid = generate_uuid(version,
                                       current_settings.urn_flag,
                                       current_settings.namespace,
                                       current_settings.name,
                                       current_settings.upper_flag)
        logging.debug(generated_uuid)

        # Insert text_blob into Plain Text Area with new UUID
        logging.debug("Insert text_blob into Plain Text Area with generated UUID")
        if text_blob != "":
            logging.debug("Plain Text Area not empty, newline required")
            plain_text_area.insert("end", "\n")
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

#def onehundred():
#    """scaffolding, please delete"""
#    current_settings.quantity = 100

def options_popup():
    """foobar"""
    #Creating Popup for Options
    logging.debug("Creating Popup for Options")
    popup = tk.Toplevel(window)
    popup.transient(window)
    popup.title("Options")
    popup.geometry("+150+150")
    popup.iconbitmap("./icon/icon.ico")

    # QUANTITY ##################################################################

    quant_var = tk.StringVar()

    #Log currentsetting.quantity
    logging.debug("Log current_setting.quantity")
    logging.debug(current_settings.quantity)
    quant_var.set(str(current_settings.quantity))

    current_settings.quant_colour = "pale green"
    quant = tk.Entry(popup, width=6, textvariable=quant_var, bg=current_settings.quant_colour)
    tk.Label(popup, text="Quantity").grid(sticky="w", padx=2, row=0, column=0)
    quant.grid(row=0, column=1, pady=8)

    def set_quant():
        logging.debug(quant_var.get())
        new_quant = quant_var.get()
        try:
            int(new_quant)
            logging.debug("yay its an int")
            if is_reasonable_quantity(int(new_quant)):
                #set currentsetting.quantity
                logging.debug("set current_setting.quantity")
                current_settings.quantity = int(new_quant)
                current_settings.quant_colour = "pale green"
                quant.config(bg=current_settings.quant_colour) #refresh
            else:
                logging.debug("eek, too big (or small)")
                current_settings.quant_colour = "light goldenrod"
                quant.config(bg=current_settings.quant_colour) #refresh
                messagebox.showwarning("Quantity", "Value too large (1 - 65536)")
        except ValueError:
            logging.debug("nay, not an int")
            current_settings.quant_colour = "light coral"
            quant.config(bg=current_settings.quant_colour) #refresh
            messagebox.showerror("Quantity", "Value not an integer")

    button = tk.Button(popup, text="Set", command=set_quant)
    button.grid(row=0, column=2)

    # URN PREFIX ##################################################################
    prefixes_var = tk.StringVar()
    prefixes = {"Disabled", "Enabled"}

    # Set prefixes_var.set based on current_settings Class
    if current_settings.urn_flag:
        logging.debug("urn currently true so show enabled")
        prefixes_var.set("Enabled")
    else:
        logging.debug("urn currently false so show disabled")
        prefixes_var.set("Disabled")

    tk.Label(popup, text="URN Prefix").grid(sticky="w", padx=2, row=1, column=0)
    prefixes_popup = tk.OptionMenu(popup, prefixes_var, *prefixes)
    prefixes_popup.grid(row=1, column=1, columnspan=2, padx=2, pady=2)

    def change_prefix(*args):
        """Changing the Prefix"""
        #Grab Prefix Selection
        logging.debug("Grab Prefix Selection")
        logging.debug(args)
        current_prefix = prefixes_var.get()
        logging.debug(current_prefix)

        #Update current_settings Class
        logging.debug("Update current_settings Class")
        if current_prefix == "Enabled":
            current_settings.urn_flag = True
        else:
            current_settings.urn_flag = False

    prefixes_var.trace('w', change_prefix)

    # UPPERCASE #################################################################
    uppercase_var = tk.StringVar()
    uppercase = {"Enabled", "Disabled"}

    # Set uppercase_var.set based on current_settings Class
    if current_settings.upper_flag:
        logging.debug("upper currently true so show enabled")
        uppercase_var.set("Enabled")
    else:
        logging.debug("upper currently false so show disabled")
        uppercase_var.set("Disabled")

    tk.Label(popup, text="Uppercase").grid(sticky="w", padx=2, row=2, column=0)
    uppercase_popup = tk.OptionMenu(popup, uppercase_var, *uppercase)
    uppercase_popup.grid(row=2, column=1, columnspan=2, padx=2, pady=2)

    def change_uppercase(*args):
        """Changing the uppercase"""
        #Grab uppercase Selection
        logging.debug("Grab uppercase Selection")
        logging.debug(args)
        current_uppercase = uppercase_var.get()
        logging.debug(current_uppercase)

        #Update current_settings Class
        logging.debug("Update current_settings Class")
        if current_uppercase == "Enabled":
            current_settings.upper_flag = True
        else:
            current_settings.upper_flag = False

    uppercase_var.trace('w', change_uppercase)

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
window.geometry("385x275+100+100")

#Close Buttom Prompt
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
