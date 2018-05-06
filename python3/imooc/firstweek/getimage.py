import requests
import os

url = "https://news.nationalgeographic.com/content/dam/news/2018/01/06/booktalk-animal-personalities/01-booktalk-animal-personalities-NationalGeographic_2495705.ngsversion.1515168759455.adapt.1190.1.jpg"

root = "./a/"
path = root + url.split('/')[-1]

try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)

		print(r.status_code)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()	
			print("Successful")
	else:
		print("FILE existed")	
except:
	print("error")		