from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from pandas import DataFrame

class getNews:

    def open(self):
        self.driver = webdriver.Chrome(executable_path='..\chromedriver\chromedriver.exe')

    def NewsDetail(self, result, newsList):

        self.driver.implicitly_wait(1)
        self.driver.get(newsList[3])

        time.sleep(3)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = pd.Series(soup.select('div.article_header > div.article_info > h3#articleTitle')[0].get_text())
        text = pd.Series(soup.select('div#articleBodyContents')[0].get_text().replace('\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}\n\n',''))
        wDate = pd.Series(soup.select('div.sponsor > span.t11')[0].get_text())
        name = pd.Series('')
        # email 여러개 들어 있는 케이스
        emails =[]
        email = soup.select('div#articleBodyContents > span.word_dic.en')
        for i in range(len(email)):
            if email[i].text.strip() == 'co':
                emails.append(email[i-2].text.strip()+"@"+email[i-1].text.strip()+email[i].text.strip()+".kr")
            if email[i].text.strip() == 'com':
                emails.append(email[i - 2].text.strip() + "@" + email[i - 1].text.strip() + email[i].text.strip())
        emails = pd.Series(emails)
        Media = pd.Series(soup.select('div.article_header > div.press_logo > a > img')[0].get_attribute_list('title')[0])
        area  = pd.Series(newsList[1])
        grades = pd.Series(soup.select('div._reactionModule.u_likeit > a  > span.u_likeit_text._count.num')[0].get_text())
        gain1 = pd.Series(soup.select('div._reactionModule.u_likeit > ul > li.u_likeit_list.good > a > span.u_likeit_list_count._count')[0].get_text())
        gain2 = pd.Series(soup.select('div._reactionModule.u_likeit > ul > li.u_likeit_list.warm > a > span.u_likeit_list_count._count')[0].get_text())
        gain3 = pd.Series(soup.select('div._reactionModule.u_likeit > ul > li.u_likeit_list.sad > a > span.u_likeit_list_count._count')[0].get_text())
        gain4 = pd.Series(soup.select('div._reactionModule.u_likeit > ul > li.u_likeit_list.angry > a > span.u_likeit_list_count._count')[0].get_text())
        gain5 = pd.Series(soup.select('div._reactionModule.u_likeit > ul > li.u_likeit_list.want > a > span.u_likeit_list_count._count')[0].get_text())
        rank = pd.Series(newsList[2])
        temp = DataFrame({'title' :title,'text':text,'wDate':wDate,'name':name,'emails':emails,'Media': Media,'area' :area,'grades' : grades,'gain1':gain1,'gain2':gain2,'gain3':gain3,'gain4':gain4,'gain5':gain5,'rank':rank},
                         columns=['title', 'text', 'wDate', 'name', 'emails', 'Media', 'area', 'grades', 'gain1', 'gain2', 'gain3',
                 'gain4', 'gain5', 'rank'])
        print(len(result))

        if len(result) == 0 :
            result = temp
        else:
            result = pd.concat([result,temp])
            print(result)

        return result


    def NewsComment(self, result, newsList):
        self.driver.implicitly_wait(1)
        self.driver.get(newsList[3])
        time.sleep(3)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        comment = pd.Series(soup.select('div.u_cbox_head > a > span.u_cbox_count')[0].get_text())
        male = pd.Series(soup.select('div.u_cbox_chart_sex > div.u_cbox_chart_progress.u_cbox_chart_male > span.u_cbox_chart_per')[0].get_text())
        female = pd.Series(soup.select('div.u_cbox_chart_sex > div.u_cbox_chart_progress.u_cbox_chart_female > span.u_cbox_chart_per')[0].get_text())
        age1 =  pd.Series(soup.select('div.u_cbox_chart_age > div > span > span.u_cbox_chart_per ')[0].get_text())
        age2 =  pd.Series(soup.select('div.u_cbox_chart_age > div > span > span.u_cbox_chart_per ')[1].get_text())
        age3 =  pd.Series(soup.select('div.u_cbox_chart_age > div > span > span.u_cbox_chart_per ')[2].get_text())
        age4 =  pd.Series(soup.select('div.u_cbox_chart_age > div > span > span.u_cbox_chart_per ')[3].get_text())
        age5 =  pd.Series(soup.select('div.u_cbox_chart_age > div > span > span.u_cbox_chart_per ')[4].get_text())
        comments = soup.select('div.u_cbox_comment_box > div.u_cbox_area > div.u_cbox_text_wrap > span.u_cbox_contents')
        comms = ''
        for i,comm in enumerate(comments):
            comms = comms + str(i+1) + '. '+ str(comm.get_text()) + '\n'
        comments = pd.Series(comms)

        temp = DataFrame({'comment' :comment,'male':male,'female':female,'age1':age1,'age2':age2,'age3': age3,'age4' :age4,'age5' : age5, 'comments' : comments},
                         columns=['comment', 'male', 'female', 'age1', 'age2', 'age3', 'age4', 'age5', 'comments'])


        if len(result) == 0 :
            result = temp
        else:
            result = pd.concat([result,temp])
            print(result)

        return result





    def getRank(self,section,maxNum,scrapingDate):
        result = []
        self.driver.implicitly_wait(1)
        url = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=" + str(section) + "&date=" + str(scrapingDate)
        self.driver.get(url)
        time.sleep(1)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        for i in range(1, maxNum + 1):
            href = soup.select('div.ranking_text > div.ranking_headline >  a')[i - 1].get_attribute_list('href')[0]
            print(soup.select('div.ranking_text > div.ranking_headline >  a')[i - 1].get_attribute_list('href')[0])
            result.append([scrapingDate, section, i, "http://news.naver.com/" + href])

        return result

    def close(self):
        self.driver.close()