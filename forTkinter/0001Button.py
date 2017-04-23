# The Button widget is used to display buttons in your application.
# w = Button(master,option=value,...)



import tkinter
import tkinter.messagebox

top = tkinter.Tk()

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World, Hello Jasper")

B = tkinter.Button(top, text ="Hello,Python!少壮不努力，老大学编程.-易百在线教程 - www.yiibai.com", command = helloCallBack)

B.pack()
top.mainloop()




