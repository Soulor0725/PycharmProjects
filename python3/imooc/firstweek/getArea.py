import requests

url = "http://www.ip138.com/ips138.asp?ip="
try:
	r = requests.get(url+"113.92.128.86")
	print(r.status_code)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text)
except:
	print("error")	
