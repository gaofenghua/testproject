from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except HTTPError as e:
    print(e)
if html is None:
    print("URL is not found")

else:
    bsObj = BeautifulSoup(html)
    print(bsObj.h1)

    nameList = bsObj.findAll("span", {"class":"green"})
    for name in nameList:
        print(name.get_text())
