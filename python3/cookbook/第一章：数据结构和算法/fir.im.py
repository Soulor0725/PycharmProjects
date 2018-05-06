#
import urllib.request

# 网址
url = "https://api.fir.im/apps?page=1" 
# params = {
#     "page":"1",
# }
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
    "set-cookie":"__cfduid=d558a90848bdf2c82ff5281c007d11e721524503085; expires=Tue, 23-Apr-19 17:04:45 GMT; path=/; domain=.fir.im; HttpOnly"
}
# request = urllib.request.Request(url,params,header)
# data = urllib.parse.urlencode(params)
# response_result = urllib.request.urlopen(url,header).read()

# request = urllib.request.Request(url,params,header)

# #爬取结果  
# response = urllib.request.urlopen(url) 

# data = response.read() 
# print(response_result)

# weburl = "http://www.douban.com/"
webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 
req = urllib.request.Request(url=url, headers=webheader)  
webPage=urllib.request.urlopen(req)
data = webPage.read()
data = data.decode('UTF-8')
print(data)