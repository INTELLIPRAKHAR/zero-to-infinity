import requests
from bs4 import BeautifulSoup
from tkinter import *
root=Tk()
root.title("NEWS")
root.geometry("800x153+0+0")
f=Frame(root,height=800,width=153,bg="grey")
f.pack(side=TOP,fill=BOTH)
page = requests.get("https://www.indiatoday.in/news.html")
page=page.text
#print(page)
soup = BeautifulSoup(page, 'html.parser')
#d=soup.findAll('div')
a1 = soup.findAll('h3')
a3=soup.findAll("p")
print(len(a3))
print(len(a1))
a4=[]
a5=[]
e=Listbox(f,bg="grey",fg="white")
e.pack(fill=BOTH,expand=1)
print("_________________TOP HEADLINES FROM INDIA TODAY________________")
for i in range(11):
                    print(f"BULLETIN{i+1}:",a1[i].get_text())
                    a5.append(a1[i].get_text())
                    e.insert(END,f"BULLETIN{i+1}: "+a5[i])
for i in range(0,3):
    print("\n")
print("________________TRENDING NEWS FROM INDIA TODAY__________________")
for i in range(0,63):
                    print(f"BULLETIN{i+1}:",a3[i].get_text())
                    a4.append(a3[i].get_text())


root.mainloop()
