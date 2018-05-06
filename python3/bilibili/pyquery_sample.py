from pyquery import PyQuery as pq 
import requests

# html = requests.get('https://www.baidu.com/?lang=en-us').text

# doc = pq(html)
# print(doc('li'))


html = requests.get('https://www.baidu.com/').text
doc = pq(html)
print(doc('head'))