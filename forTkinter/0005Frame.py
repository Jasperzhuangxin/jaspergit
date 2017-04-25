# The Frame widget is used as a container widget 
# to orginaze other widgets.

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = RIGHT )

whitebutton = Button(frame, text="White", fg="white")
whitebutton.pack( side = RIGHT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )



blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()
