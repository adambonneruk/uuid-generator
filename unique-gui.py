import tkinter as tk

window = tk.Tk()

menuBar = tk.Menu(window)

fileMenu = tk.Menu(menuBar,tearoff=0)
fileMenu.add_command(label="Save as...")
fileMenu.add_command(label="Close")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
menuBar.add_cascade(label="File", menu=fileMenu)

optionsMenu = tk.Menu(menuBar,tearoff=0)
optionsMenu.add_command(label="X-Ray")
optionsMenu.add_command(label="Yankee")
optionsMenu.add_separator()
optionsMenu.add_command(label="Zulu")
menuBar.add_cascade(label="Options", menu=optionsMenu)

window.config(menu=menuBar)

labelHello = tk.Label(window, text="Hello, world!")
labelHello.pack()

labelUsername = tk.Label(window, text="User Name:")
labelUsername.pack(side="left")

text = tk.Text(window)
text.pack()

bigtext = tk.scrolledtext(window)
bigtext.pack()

canvas = tk.Canvas(window, width=800, height=600)  # define the size
canvas.pack()

#label = tk.Label(frame.frame,text='General Inf', bd='3', fg='blue', font='Helvetica 9 bold')  # placing labels
#entry_field = tk.Entry(frame.frame, bd='3', justify="center")
#check_button = tk.Checkbutton(frame.frame_test, text="1", variable= check_1, onvalue=1, offvalue=0)

frame = tk.Frame(window, bg="grey")
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

window.title('Unique: The UUID Generator') #https://stackoverflow.com/questions/33637292/change-tkinter-frame-title
window.iconbitmap('./icon/icon.ico') #https://www.delftstack.com/howto/python-tkinter/how-to-set-window-icon-in-tkinter/
window.mainloop()


'''
import tkinter as tk
window = tk.Tk()
window.title("Example for Tkinter")  # to define the title
window.mainloop()
'''