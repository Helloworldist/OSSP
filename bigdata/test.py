from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return  None
    try:
        bsObj=BeautifulSoup(html.read, "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title=getTitle("http://www.w3.org/1999/xhtml")
if title == None:
    print("Title couldn't found")
else:
    print(title)
# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsObj = BeautifulSoup(html.read(), "html.parser")
# print(bsObj.div)