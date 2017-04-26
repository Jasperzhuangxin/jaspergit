# A labelframe is a simple container widget.
# Its primary purpose is to act as a spacer
# or container for complex window layouts.

from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()
 
root.mainloop()