import requests

url = "https://item.jd.com/5826214.html"

try:
	r = requests.get(url)
	r.raise_for_status()
	print(r.status_code)
	print(r.encoding)
	print(r.text[:1000])
except:
	print("爬取失败")
