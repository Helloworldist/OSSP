from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return  None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%A1%9C%ED%8C%8C_(%EC%9C%84%EC%84%B1)")
if title == None:
    print("Title couldn't found")
else:
    print(title)

# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsObj = BeautifulSoup(html.read(), "html.parser")
# print(bsObj.div)