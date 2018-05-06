 # 运行脚本将得到整个页面中包含图片的URL地址。
import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist      
   
html = getHtml("https://www.cnblogs.com/fnng/p/3576154.html")
print(getImg(html))