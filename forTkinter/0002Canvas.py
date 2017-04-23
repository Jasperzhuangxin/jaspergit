# The Canvas widget is used to draw shapes, 
# such as lines, ovals, polygons, and rectangles, 
# in your application.

# w = Canvas(master, option=value, ...)

import tkinter
import tkinter.messagebox

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 10, 250, 250
arc = C.create_arc(coord, start=0, extent=250, fill="yellow")

C.pack()
top.mainloop()
