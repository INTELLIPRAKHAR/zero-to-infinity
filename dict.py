import requests
from bs4 import BeautifulSoup
from tkinter import *

# making the window
root = Tk()
root.title("Dictionary!")
root.geometry("400x250")
root.resizable(0,0)
root.configure(background='grey')
#

#function that optain meaning
def findMeaning():
    
    source_code = requests.get("http://dictionary.reference.com/browse/" + str(word.get()))
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    try:
        a1 = soup.find('span', {'class': 'one-click-content css-98tqe9 e1q3nk1v4'})
        
        meaning.set(a1.get_text())
    except:
        meaning.set("Error-Word not found")
    
    

        


    


#variables that hold user imput
word = StringVar()
meaning = StringVar()
#end



#buttons
btnFind = Button(root, text="Find", width=10, height=3, font="Helvetic 10 bold",command=findMeaning, bg="white", fg="black")
btnFind.place(x=150, y=170)
#end

#making the label
lblWord = Label(root, text="Enter the word you want find the meaning:", font="Helvetic 8 bold", bg="GREY")
lblWord.place(x=0, y=90)
lblMeaning = Label(root, text="The meaning:", font="Helvetic 8 bold",bg="GREY")
lblMeaning.place(x=0, y=110)
#end

#the textboxes
txtWord = Entry(root, font="Helvetic 8 bold", width=24,textvariable=word)
txtWord.place(x=250, y=90)
txtMeaning = Label(root, font="Helvetic 8 bold", width=52, textvariable=meaning)
txtMeaning.place(x=80, y=110)
#end




root.mainloop()




