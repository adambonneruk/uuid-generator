from tkinter import *
import sys

try:
	sys.stdout.write("\n")
	sys.stdout.flush()
except:
	root = Tk()

	w = Label(root, text="Hello, world!")
	w.pack()

	root.minsize(256,256)
	root.mainloop()


'''
try:
    sys.stdout.write("\n")
    sys.stdout.flush()
except IOError:
    class dummyStream:
        def __init__(self): pass
        def write(self,data): pass
        def read(self,data): pass
        def flush(self): pass
        def close(self): pass
    # and now redirect all default streams to this dummyStream:
    sys.stdout = dummyStream()
    sys.stderr = dummyStream()
    sys.stdin = dummyStream()
    sys.__stdout__ = dummyStream()
    sys.__stderr__ = dummyStream()
    sys.__stdin__ = dummyStream()
'''