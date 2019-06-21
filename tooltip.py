from tkinter import *
import wckToolTips

root = Tk()

b = Button(root, text="Click me!", command=root.quit)
b.pack()

wckToolTips.register(b, "This button exits the program")

mainloop()
