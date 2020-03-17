import requests
from bs4 import BeautifulSoup
import pandas as pd

l1=[]
l2=[]

for i in range(1,21):                                                    #first 20 pages on the topic will be scraped 
    url = 'https://timesofindia.indiatimes.com/topic/topic-name/'+str(i) #put the TOI url of required topic here
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    links=[]
    for article in soup.findAll('li',class_='article'):
        links.append('https://timesofindia.indiatimes.com'+article.a['href'])
    for ur in links:
        getter=requests.get(ur)
        sup=BeautifulSoup(getter.text,'lxml')
        l1.append(sup.h1.text)
        news=sup.find('div',class_='_3WlLe clearfix')
        try:
            l2.append(news.text)
        except AttributeError:
            try:
                new=sup.find('div',class_='section1')
                new.script.decompose()
                l2.append(new.text)
            except:l1.pop()

toi=pd.DataFrame()
toi['Headline']=l1
toi['Article']=l2
toi.to_csv('topic-name.csv',index=False)                                 #gives output in .csv file

