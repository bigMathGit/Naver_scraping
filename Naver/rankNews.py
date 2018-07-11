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
def getDetailNews(result,result_comment,newsList):
    for i in range(len(newsList)):
        #result = getNews.NewsDetail(result,newsList[i])
        result_comment = getNews.NewsComment(result_comment,newsList[i])
    return result


#sectionId = [100,101,102,103,104,105]
num = 3
sectionId = [101]

scrapingDate = "20180702"
getNews.open()
result = pd.DataFrame(columns=['title', 'text', 'wDate', 'name', 'emails', 'Media', 'area', 'grades', 'gain1', 'gain2', 'gain3','gain4', 'gain5', 'rank'])
result_comment = pd.DataFrame(columns=['comment','male', 'female', 'age1','age2','age3','age4','age5'])


for section in sectionId:
    newsList = getNews.getRank(section, num, scrapingDate)
    result = getDetailNews(result,result_comment,newsList)
    print('pd :', result)
getNews.close()
result.to_csv('result.csv', index=False)