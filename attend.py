#import module from tkinter for UI
from tkinter import *
from playsound import playsound
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="GREY")

#root.geometry("300x300")

def function1():
    playsound("student.mp3")
    os.system("python dataset_capture.py")
    playsound("student.mp3")
    
def function2():
    
    os.system("python training_dataset.py")

def function3():

    os.system("python recognizer.py")
    playsound('sound.mp3')
    
def function6():

    root.destroy()

def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')

#stting title for the window
root.title("BIOMETRIC ARTIFICIAL INTELLIGENCE ASSITANT ATTENDANCE MANAGER")

#creating a text label
Label(root, text="BIOMETRIC ARTIFICIAL INTELLIGENCE ATTENDANCE MANAGER",font=("times new roman",20),fg="#F4BB1E",bg="grey",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="CREATE DATASET",font=("times new roman",20),bg="white",fg="#F4BB1E",command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="TRAIN DATASET",font=("times new roman",20),bg="white",fg="#F4BB1E",command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="RECOGNIZE AND ATTENDANCE",font=('times new roman',20),bg="white",fg="#F4BB1E",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="ATTENDANCE SHEET",font=('times new roman',20),bg="white",fg="#F4BB1E",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating FOURTH button
Button(root,text="EXIT",font=('times new roman',20),bg="grey",fg="#F4BB1E",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
