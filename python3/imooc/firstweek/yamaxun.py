import requests

url = "http://www.amazon.cn/dp/B00JZ96ZI8"

try:
	r = requests.get(url)
	r.raise_for_status()
	print(r.status_code)
	print(r.text[1000:2000])
except Exception as e:
	print("ERROR")