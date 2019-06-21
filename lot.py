import smtplib
import time
import secrets
import random
from tkinter import *
from tkinter import messagebox
otp=random.randint(100000,999999)
lot=str(hex(otp))
root=Tk()
root.title('AUTO OTP DRAWER')
def lotery():
    import secrets
    print(list(volun))
    win=secrets.choice(list(volun))
    winner=volun[win]
    print(win)
    l.config(text="DRAWING A LOTTERY")
    string=f'congragulations!!!!!   {win} with emailid : {winner}    YOU HAVE WON A PRICE WORTH RS.15 LAKHS please dont share this is your one time passcode----------------%{lot} and lottery number {otp} '.upper()
    print(string)
    to=('yesdaddygon@gmail.com','clubjack@rediffmail.com')
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('yesdadgonpapa@gmail.com','yesdadgon543')
    server.sendmail('yesdadgonpapa@gmail.com',winner,string.upper())
    server.close()
    messagebox.showinfo("WINNER", string)
    b.config(state=DISABLED)
volun={}
print(volun)
def volunt():
    i=b4.get()
    j=b5.get()
    volun[i]=j
    print(volun)
    b4.delete(0, END)
    b5.delete(0, END)
l=Label(text="PRESS BUTTON TO DRAW A LOTTERY",font=('times new roman',13,'bold'))
l.grid(row=0,column=0)
b=Label(text="ADD VOLUNTEER NAME")
b.grid(row=3,column=0)
b3=Button(command=lotery,text="DRAW",relief='raised')
b3.grid(row=5,column=1)
b5=Label(text="ADD EMAIL")
b5.grid(row=4,column=0)
b4=Entry(width=13,relief='raised')
b4.grid(row=3,column=1)
b5=Entry(width=13,relief='raised')
b5.grid(row=4,column=1)
b6=Button(text="ADD VOLUNTEER TO PARTICIPATE",relief='raised',command=volunt)
b6.grid(row=5,column=0)
mainloop()
