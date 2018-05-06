import requests
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')

# print(soup.find_all('a'))
# print(soup.find_all(["a","b"]))
# for tag in soup.find_all(True):
# 	print(tag.name)

# import re
# for tag in soup.find_all(re.compile('b')):
	# print(tag.name)

# print(soup.find_all("p","course"))
# print(soup.find_all(id="link1"))
# print(soup.find_all(id="link"))

# import re
# print(soup.find_all(id=re.compile('link')))

# print(soup.find_all("a"))

# print(soup.find_all(string="Basic Python"))

import re
print(soup.find_all(string=re.compile("python")))