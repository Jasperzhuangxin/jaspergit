# The Entry widget is used to display 
# a single-line text field for 
# accepting values from user.

from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)

E1 = Entry(top, bd =3)
E1.pack( side = BOTTOM)

L2 = Label(top, text="Confirm")
L2.pack( side = RIGHT)

top.mainloop()
