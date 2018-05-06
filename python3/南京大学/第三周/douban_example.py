# import requests

# r = requests.get('https://book.douban.com/subject/1084336/')
# print(r.status_code)

# from bs4 import BeautifulSoup

# markup = '<p class="title"><b>the title is pig</b></p>'
# soup = BeautifulSoup(markup,'lxml')
# print(soup.b.string)
# print(soup.p.string)

# print(soup.find_all('b'))

import requests
from bs4 import BeautifulSoup
import re

response = requests.get('https://book.douban.com/subject/1084336')
# print(response.status_code)
soup = BeautifulSoup(response.text,'lxml')
comments = soup.find_all('p','comment-content')
for i in range(0,len(comments)):
    comment = str(i+1)+'.'+comments[i].string
    print(comment)

pattern_s = re.compile('<span class="user-stars allstar(.*?) rating" ti')
p = re.findall(pattern_s,response.text)
for item in p:
    print(item)