# import requests
# url = "https://www.baidu.com/img/baidu_jgylogo3.gif"
# response = requests.get(url)
# print (response.content)
# with open('baidu.git','wb') as f:
#     f.write(response.content)
#     f.close
# v = 2
# a = 22
# print(v+a)

# import urllib.request

# response = urllib.request.urlopen('https://www.baidu.com/',timeout=1)
# print(response)

from urllib import request,error
try:
    response = request.urlopen('http://xiaoweihua.com/index.html')
    print (response)
except error.URLError as e:
    print (e.reason)