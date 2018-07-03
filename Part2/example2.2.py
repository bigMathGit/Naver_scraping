from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span",{"class":"green","class":"red"})

for name in nameList:
    print(name.get_text())


findPrince = bsObj.findAll(text="the prince")
print(len(findPrince))

allText = bsObj.findAll(id="text")
print(allText[0].get_text())