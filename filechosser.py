from tkinter import *
from tkinter.filedialog import askopenfilename

root=Tk() # we don't want a full GUI, so keep the root window from appearing
def file():
    filename = askopenfilename()
    # show an "Open" dialog box and return the path to the selected file
    print(filename)
b=Button(command=file).pack()

mainloop()
