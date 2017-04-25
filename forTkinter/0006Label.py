# The Label widget is used to provide a single-line caption for other widgets.
# It can also contain images.

from tkinter import *

root = Tk()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()