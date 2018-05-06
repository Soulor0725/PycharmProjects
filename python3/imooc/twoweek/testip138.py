import requests
r = requests.get("http://www.ip138.com/")
r.encoding = r.apparent_encoding
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())