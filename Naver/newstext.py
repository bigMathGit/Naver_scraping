from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=081&aid=0002896571&date=20180301&type=1&rankingSectionId=101&rankingSeq=5"

html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")


title = bsObj.find("h3",{"id":"articleTitle"}).get_text()
text = bsObj.find("div",{"id":"articleBodyContents"}).get_text()
name = ""
email = ""
wDate = bsObj.findAll("span",{"class":"t11"})[0].get_text()
gain = bsObj.findAll("span",{"class":"word_dic en"})


print(wDate)
print(gain)

"""
기사 제목   : title 
기사내용    : text
작성자      : name
기자 이메일 : email
작성일      : wDate
언론사명    : Media
분야        : area
평점        : grades
좋아요수         : gain1
훈훈해요수       : gain2
슬퍼요수         : gain3
화나요수         : gain4
후속기사원해요수  : gain5
위치             : rank 
댓글수           : comment
남성             : male
여성             : female
연령10           : age1
연령20           : age2
연령30           : age3
연령40           : age4
연령50+          : age5
"""

html.close()