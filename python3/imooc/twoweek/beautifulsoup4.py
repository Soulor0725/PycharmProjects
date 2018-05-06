import requests

r = requests.get("https://python123.io/ws/demo.html")
# print(r.text)

demo = r.text

from bs4 import BeautifulSoup
 
soup = BeautifulSoup(demo,"html.parser") 
# print(soup.prettify())
# print(end=" ")

# soup1 = BeautifulSoup("<html>data</html>","html.parser") 
# print(soup1.prettify())
print(soup.title)

tag = soup.a
print(tag)


print(soup.a.name)


print(soup.a.parent.name)
print(soup.a.parent.parent.name)

print(tag.attrs)

print(tag.attrs['href'])
print(tag.attrs['class'])
print(type(tag.attrs))
print(type(tag))

print(soup.a.string)

print(soup.p.string)

print(type(soup.p.string))