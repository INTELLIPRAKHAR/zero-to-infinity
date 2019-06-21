import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.indiatoday.in/news.html")
page=page.text
#print(page)
soup = BeautifulSoup(page, 'html.parser')
#d=soup.findAll('div')
a1 = soup.findAll('h3')
print(len(a1))
for i in range(len(a1)):
                    print(a1[i].get_text())
