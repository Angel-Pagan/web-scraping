""" Import packages """
import pandas as pd
import requests 
from bs4 import BeautifulSoup 

""" Import Yahoo Html """
yahoo_articles = requests.get ('https://yahoo.com') #Requesting Yahoo Website
soup = BeautifulSoup(yahoo_articles.text, 'html.parser') #Converting file to html
print(soup.prettify()) # Print Html in human readable format

""" Acquire Html article titles """

soup.find_all('h3',class_='LineClamp(2,2.6em) Mend(50px) Mb(4px) Mt(1px) Lh(1.33) Fz(18px) Fz(16px)--maw1024 Fw(b) stream-item-title') # Using HTML div type and class to acquire article title
article = soup.find_all('h3',class_='LineClamp(2,2.6em) Mend(50px) Mb(4px) Mt(1px) Lh(1.33) Fz(18px) Fz(16px)--maw1024 Fw(b) stream-item-title') # assigning articles 

for i in article: 
    print(i.text)
    
articles = []
for item in article:
    print(item.text)
    name = item.text 
    ## clean name remove whitespace
    name = name.strip()
    ## remove new line
    name = name.replace('\n','')
    articles.append(name)
len(articles)

""" Acquire Html Article Descriptions """

soup.find_all('p',class_='finance-ticker-fetch-success_D(n) LineClamp(2,40px) sub-upsell-fetch-success_D(n) Mend(50px) Fz(14px) Lh(1.43) C(--batcave) My(2px) Mb(4px) Bxz(bb) Wob($break-word)')
article_description = soup.find_all('p',class_='finance-ticker-fetch-success_D(n) LineClamp(2,40px) sub-upsell-fetch-success_D(n) Mend(50px) Fz(14px) Lh(1.43) C(--batcave) My(2px) Mb(4px) Bxz(bb) Wob($break-word)')

article_descriptions = []
for item in article_description:
    print(item.text)
    desc = item.text 
    ## clean name remove whitespace
    desc = desc.strip()
    ## remove new line
    desc = desc.replace('\n','')
    article_descriptions.append(desc)
len(article_descriptions)

""" Save Yahoo articles titles and Yahoo articles description into CSV file """

df = pd.DataFrame({'article_title':articles,'article_description':article_descriptions})
df.to_csv('data/yahoo_for_you_articles')

""" Import Nba HTML """

nba = requests.get ('https://www.nba.com/')
soup = BeautifulSoup(nba.text, 'html.parser')
print(soup.prettify())

""" Acquire NBA.com Around the NBA Article titles """

soup.find_all('h3', class_='Text_text__I2GnQ ArticleTile_tileTitle__aA8g7')
nba_around_the_nba = soup.find_all('h3', class_='Text_text__I2GnQ ArticleTile_tileTitle__aA8g7')
for i in nba_around_the_nba: 
    print(i.text) 

nba_articles_titles = []
for item in nba_around_the_nba:
    print(item.text)
    name = item.text 
    ## clean name remove whitespace
    name = name.strip()
    ## remove new line
    name = name.replace('\n','')
    nba_articles_titles.append(name)
len(nba_articles_titles)

""" Acquire NBA.com Around the NBA Article descriptions"""

nba_around_the_nba_descriptions =soup.find_all ('p','Text_text__I2GnQ ArticleTile_tileSub__kiMA0')
for i in nba_around_the_nba_descriptions: 
    print(i.text) 
    
nba_articles_disc = []
for item in nba_around_the_nba_descriptions:
    print(item.text)
    name = item.text 
    ## clean name remove whitespace
    name = name.strip()
    ## remove new line
    name = name.replace('\n','')
    nba_articles_disc.append(name)
len(nba_articles_disc)

""" Convert NBA Article titles and Nba Article descriptions into a csv file """

df = pd.DataFrame({'article_title':nba_articles_titles,'article_description': nba_articles_disc})
df.to_csv('data/nba_articles_around_the_nba')
