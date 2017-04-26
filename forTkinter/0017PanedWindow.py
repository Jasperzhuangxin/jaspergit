# A PanedWindow is a container widget that may contain any number of panes,
# arranged horizontally or vertically.

from tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)  # HORIZONTAL
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

m3 = PanedWindow()
m3.pack(fill=BOTH, expand=3)
right = Label(m3, text="right pane")
m3.add(right)

m4 = PanedWindow(m3, orient=VERTICAL)
m3.add(m4)


mainloop()