from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

#try:
#    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#except HTTPError as e:
#    print(e)
#    # null을 반환하거나, break 문을 실행하거나, 기타 다른방법도 가능
#else:
#    # 프로그램을 계속해서 실행. except ㅈ러에서 return 이나 brack사용했다면 필요 없음
#    bsObj = BeautifulSoup(html.read(), "html.parser")
#    print(bsObj.h1)
#
#try:
#    badContent = bsObj.nonExistingTag.anotherTag
#except AttributeError as e:
#    print("Tag was not found")
#else:
#    if badContent == None:
#        print("Tag was not found")
#    else:
#        print(badContent)
