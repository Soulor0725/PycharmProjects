# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/?lang=en-us").text
# print(html)

soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.title.string)
# print(soup.head.meta['charset'])
# print(soup.p.string)

# print(soup.p.contents)

# print(soup.find_all('img'))
# print(soup.find_all('img')[0])

# print(soup.find_all(class_="tittle"))

# for ul in soup.select('ul'):
#     print(ul.select('li'))

for li in soup.select('li'):
    print(li.get_text())