# grabs news to perform searches

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()
soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")


text = ['facebook', 'youtube', 'amazon', 'selenium docs python',
        'beautifulsoup docs python', 'ebay', 'weather', 'netflix', 'hulu',
        'python documentation', 'stackoverflow', 'reddit', 'news', 'gmail',
        'python types', 'codecademy', 'texas state', 'twitter', 'speed test',
        'steam', 'spotify', 'ups tracking', 'fedex tracking', 'discord',
        'google drive', 'twitch', 'google docs', 'instagram', 'python3', 'rpi',]

for news in news_list:
  text.insert(0, news.title.text)

