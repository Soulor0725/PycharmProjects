import requests

keyword = "Python"

try:
	kv = {"wd":keyword}
	r = requests.get("https://www.baidu.com/s",params = kv)
	print("url:",r.request.url)
	r.raise_for_status()
	print(len(r.text))
except Exception as e:
	print("error:",e)
