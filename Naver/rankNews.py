import getNews
import pandas as pd
import time
from pandas import DataFrame

"""
sectionId로 분야 구분
100: 정치 , 101 : 경제, 102: 사회, 103: 생활문화, 104 : 세계, 105: IT/과학, 106:연예 , 107: 스포츠
"""
###  class 생성
getNews = getNews.getNews()


## get Detail new
def getDetailNews(newsList):
    result = pd.DataFrame(columns=['title', 'text', 'wDate', 'name', 'emails', 'Media', 'area', 'grades', 'gain1', 'gain2', 'gain3','gain4', 'gain5', 'rank'])

    for i in range(len(newsList)):
        result = getNews.NewsDetail(result,newsList[i])
        print(len(result))


sectionId = [100,101,102,103,104,105,107]
scrapingDate = "20180702"


for section in sectionId:
    getNews.open()
    newsList = getNews.getRank(section, 3, scrapingDate)
    pd = getDetailNews(newsList)
    print('pd :', pd)
    getNews.close()
