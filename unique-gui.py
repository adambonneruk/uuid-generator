import tkinter as tk
from tkinter import scrolledtext

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

#labelHello = tk.Label(window, text="Hello, world!")
#labelHello.pack()

#canvas = tk.Canvas(window, width=800, height=600)  # define the size
#canvas.pack()


'''for fm in ['blue','red','yellow','green','white','black','purple','blue','red','yellow','green','white','black','purple']:  
    Frame(height = 20,width = 640,bg = fm).pack()  
root.mainloop() '''

master_width = 800
master_height = 480
master_frame = tk.Frame(window, width = master_width, height = master_height, bg = "purple")
master_frame.pack()

left_frame = tk.Frame(master_frame, width = master_width/4, height = master_height, bg = "red")
left_frame.place(x=0,y=0)

right_top_frame = tk.Frame(master_frame, width = master_width/4*3, height = master_height/16, bg = "blue")
right_top_frame.place(x=master_width/4,y=0)

right_middle_frame = tk.Frame(master_frame, width = master_width/4*3, height = master_height/16*14, bg = "green")
right_middle_frame.place(x=master_width/4,y=master_height/16)

right_bottom_frame = tk.Frame(master_frame, width = master_width/4*3, height = master_height/16, bg = "yellow")
right_bottom_frame.place(x=master_width/4,y=master_height/16*15)




'''left_frame = tk.Frame(height = 600, width = 256)
left_frame.pack(side="left")

for i in range(0,7):
	print(i)
	hello = tk.Label(left_frame,text="hello world")
	hello.pack(padx = 10, pady = 10) #hello.place(x=10,y=60)

right_frame = tk.Frame(height = 600, width = (800-256))
right_frame.pack(side="left")

text_area = scrolledtext.ScrolledText(right_frame,wrap = tk.WORD,font = ("Lucida Console",10)) 
text_area.grid(column = 0, pady = 10, padx = 10)'''

#photo = tk.PhotoImage(file="./design/mockup-cut.png")
#imgLabel = tk.Label(right_frame, image=photo)
#imgLabel.pack()


#tk.Frame(height = 256, width = 256, bg = "grey").pack(side="left")
#tk.Frame(height = 256, width = 256, bg = "red").pack(side="left")

#bluebutton = tk.Button(frame, text="Blue", fg="blue")
#bluebutton.pack(side="left")

#photo = tk.PhotoImage(file="./design/mockup-cut.png")
#imgLabel = tk.Label(window, image=photo)
#imgLabel.pack(side="left")

#for fm in ['blue','red','yellow','green','white','black']:
#	tk.Frame(height = 20,width = 640,bg = fm).pack()

#label = tk.Label(frame.frame,text='General Inf', bd='3', fg='blue', font='Helvetica 9 bold')  # placing labels
#entry_field = tk.Entry(frame.frame, bd='3', justify="center")
#check_button = tk.Checkbutton(frame.frame_test, text="1", variable= check_1, onvalue=1, offvalue=0)

#frame = tk.Frame(window, bg="grey")
#frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

#window.title('Unique: The UUID Generator') #https://stackoverflow.com/questions/33637292/change-tkinter-frame-title
#window.iconbitmap('./icon/icon.ico') #https://www.delftstack.com/howto/python-tkinter/how-to-set-window-icon-in-tkinter/
window.mainloop()


'''
import tkinter as tk
window = tk.Tk()
window.title("Example for Tkinter")  # to define the title
window.mainloop()
'''