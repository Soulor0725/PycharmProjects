import requests
r = requests.get("http://www.ip138.com/")
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
for link in soup.find_all("a"):
	print(link.get("href"))
