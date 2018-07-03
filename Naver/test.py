import getNews
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# getNews = Naver.getNews.getNews()
#
# getNews.open()
#
# print(getNews.getRank('100',5,'20180314'))

driver = webdriver.Chrome(executable_path='..\chromedriver\chromedriver.exe')

result = []
driver.implicitly_wait(1)
section = 100
maxNum = 30
scrapingDate = '20180314'

url = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=" + str(section) + "&date=" + str(scrapingDate)
driver.get(url)
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

for i in range(1, maxNum + 1):
    if i <= 3:
        print(soup.select('li.ranking_item is_num' + str(i)))
        href = soup.select('li.ranking_item is_num' + str(i) +'  >div > div >  a').get_attribute_list('href')[0]
    elif i <= 10:
        href = soup.select('div.ranking_section.ranfir2 > ol > li.gnum' + str(i) + ' > dl > dt > a')[0].get_attribute_list('href')[0]
    elif i <= 30:
        href = soup.select('div.ranking_section > ol > li.gnum' + str(i) + ' > dl > dt > a')[0].get_attribute_list('href')[0]
    else:
        print(i, 'is out of index')
    result.append([scrapingDate, section, i, "http://news.naver.com/" + href])

print(result)

driver.close()