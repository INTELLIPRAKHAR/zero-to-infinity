from tkinter import *
import time
from tkinter import ttk
from PIL import Image, ImageTk
import wckToolTips as tip
import os
import requests
from bs4 import BeautifulSoup
#----------------librarys--------

root = Tk()
root.geometry("600x373+0+0")
root.resizable(height = False, width =False)
var=StringVar()
root.title("SUBMITTED AND DEVELOPED BY PRAKHAAR DUBEY")
#----------FRAME----------------------------------------------------
f1=Frame(root,width=800,height=93,bg="grey",relief=SUNKEN)
f1.pack(side=TOP)
ifra=Canvas(root)
ifra.pack(expand=True , fill=BOTH)
#----------IMAGES----------------------------------------------
image1=PhotoImage(file="dad.png")
t= ImageTk.PhotoImage(file="daddy.png")
but=PhotoImage(file="daddy.png")
but.subsample(1,1)
ifra.create_image(0, 0, anchor=NW, image=image1)
#------------time and weather-----------------------------------------
tine=time.asctime(time.localtime(time.time()))
def weather():
    page = requests.get("https://weather.com/en-IN/weather/today/l/12a3e44ae6895f6a5e60617371b3443fdfe52180d6efe583f1cc427ce6dfdea9")
    soup = BeautifulSoup(page.content, 'html.parser')
    d=soup.findAll(text=True)
    wea=d[97]+d[98]
    return(wea)
l=Label(f1,text="ZERO TO INFINITY",font=("SF Sports Night",51),bg="grey",fg="WHITE")
l.pack(side=BOTTOM,fill=BOTH)
l3=Label(f1,text=weather()+"C IN JHANSI",font=("AREIAL",13),bg="grey",fg="white")
l3.bind("<Button-1>",weather)
l3.pack(side=LEFT,anchor=NE)
l4=Label(f1,text=tine,font=("AREIAL",13),bg="grey",fg="white")
l4.bind("<Button-1>",weather)
l4.pack(side=RIGHT,anchor=NE)
#---------------FUNTIONS--------------
def but3():
    var.set(13)
    #os.system("python")
    b4['state']=NORMAL
    tip.register(progress,"YOU ARE REACHED LEVEL 1")
def but4():
    var.set(30)
    #os.system("python")
    b5['state']=NORMAL
    tip.register(progress,"YOU ARE REACHED LEVEL 2")
def but5():
    var.set(45)
    os.system("python topheadlines.py")
    b6['state']=NORMAL
    tip.register(progress,"YOU ARE REACHED LEVEL 3 ")
def but6():
    b7['state']=NORMAL
    #os.system("python auto.py")
    var.set(65)
    tip.register(progress,"YOU ARE REACHED LEVEL 4")
def but7():
    b8['state']=NORMAL
    os.system("python lot.py")
    var.set(75)
    tip.register(progress,"YOU ARE REACHED LEVEL 5 ")
def but8():
    var.set(80)
    b9['state']=NORMAL
    os.system("python virus.py")
    tip.register(progress,"YOU ARE REACHED LEVEL 6")
def but9():
    var.set(93)
    os.system("python desktopassis.py")
    b10['state']=NORMAL
    tip.register(progress,"YOU ARE REACHED LEVEL 7 ")
def but10():
    var.set(100)
    os.system("python attend.py")
    tip.register(progress,"YOU ARE GOOD TO GO TO ADVANCED USER")
    
   
    

#-----------BUTTONS---------------------------------------------------
b3=Button(ifra, text="HELLO UNIVERSE",image=t,compound=CENTER,command=but3,bd=13,bg="grey",relief=GROOVE)
b3.grid(row=300,column=930,padx=63)
b4=Button(ifra, text="b4",image=but,compound=CENTER,command=but4,state=DISABLED,bd=13,relief=GROOVE,bg="grey")
b4.grid(row=400,column=930)
b5=Button(ifra, text="WEBSCRAPING",image=but,compound=CENTER,command=but5,state=DISABLED,bd=13,relief=GROOVE,bg="grey")
b5.grid(row=500,column=930)
b6=Button(ifra, text="AUTOBOT",image=t,compound=CENTER,command=but6,bd=13,bg="grey",relief=GROOVE,state=DISABLED)
b6.grid(row=600,column=930)
b7=Button(ifra, text="AUTO_OTP",image=but,compound=CENTER,command=but7,state=DISABLED,bd=13,relief=GROOVE,bg="grey")
b7.grid(row=300,column=953)
b8=Button(ifra, text="RANSOME WARE",image=but,compound=CENTER,command=but8,state=DISABLED,bd=13,relief=GROOVE,bg="grey")
b8.grid(row=400,column=953)
b9=Button(ifra, text="VIRTUAl ASST.",image=but,compound=CENTER,command=but9,bd=13,state=DISABLED,relief=GROOVE,bg="grey")
b9.grid(row=500,column=953)
b10=Button(ifra, text="BIOMETRICS_AI",image=t,compound=CENTER,command=but10,bd=13,bg="grey",state=DISABLED,relief=GROOVE)
b10.grid(row=600,column=953)
#----------------------------TOOLTIP----------------------------------------
progress=ttk.Progressbar(root,length=800,variable=var)
progress.pack(side=BOTTOM)
tip.register(b3,"THIS IS LEVEL I")
tip.register(b4,"THIS IS LEVEL II")
tip.register(b5,"THIS IS LEVEL III")
tip.register(b6,"THIS IS LEVEL IV")
tip.register(b7,"THIS IS LEVEL V")
tip.register(b8,"THIS IS LEVEL VI")
tip.register(b9,"THIS IS LEVEL VII")
tip.register(b10,"THIS IS LEVEL VIII")
tip.register(l,"THIS IS TITLE OF PROJECT")
tip.register(l3,"SHOWS A CURRENT WEATHER ")
tip.register(progress,"SHOWS A PROGRESS")
#---------------------------------------------------------------------


root.mainloop()
