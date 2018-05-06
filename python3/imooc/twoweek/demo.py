
import requests

r = requests.get("https://python123.io/ws/demo.html")

demo = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(demo,'html.parser')

# print(soup.head)
# print(soup.head.contents)

# print(soup.body.contents)
# # print(soup.head.contents.chirldren)

# print(len(soup.body.contents))

print(soup.body.contents[1])
