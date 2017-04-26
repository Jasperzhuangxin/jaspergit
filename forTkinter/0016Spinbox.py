# The Spinbox widget is a variant of the standard Tkinter Entry widget, 
# which can be used to select from a fixed number of values.

from tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=10)
w.pack()

mainloop()