from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = TOP )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = TOP )

# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)



bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

root.mainloop()