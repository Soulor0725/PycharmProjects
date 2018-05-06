''''' 
伪装浏览器 
 
对于一些需要登录的网站，如果不是从浏览器发出的请求，则得不到响应。 
所以，我们需要将爬虫程序发出的请求伪装成浏览器正规军。 
具体实现：自定义网页请求报头。 
'''  
  
#实例二：依然爬取豆瓣，采用伪装浏览器的方式  
import urllib.request

#定义保存函数
def saveFile(data):
	path="douban.html"
	f=open(path,"wb")
	f.write(data)
	f.close()

#网址
url="https://www.douban.com"	
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
req=urllib.request.Request(url=url,headers=headers)

res=urllib.request.urlopen(req)

data=res.read()


#保存内容
saveFile(data)

data=data.decode('utf-8')

print(data)