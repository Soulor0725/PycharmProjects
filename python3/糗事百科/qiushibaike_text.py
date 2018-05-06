import re
import requests
import html
import time

def crawl_joke_list(page=1):
    # https://www.qiushibaike.com/text/page/2/
    url = 'https://www.qiushibaike.com/text/page/'+str(page)
    
    res = requests.get(url)
    
    pattern = re.compile("<div class=\"article block untagged mb15.*?<div class=\"content\">.*?</div>",re.S)
    body = html.unescape(res.text).replace("<br/>","\n")
    
    m = pattern.findall(body)
    
    # 用户
    user_pattern = re.compile("<div class=\"author clearfix\">.*?<h2>(.*?)</h2>",re.S)    
    # print(user_pattern)
    # 段子
    content_pattern = re.compile("<div class=\"content\">\n<span>(.*?)</span>",re.S)

    for joke in m:
        user = user_pattern.findall(joke)
        # print(url)
        output = []
        if len(user)>0:
            output.append('\n\n用户名:'+user[0])
        
        content = content_pattern.findall(joke)            
        if len(content)>0:
            output.append('发布的内容:'+content[0].replace("\n",""))

        print("\t".join(output))    

    time.sleep(1)    

if __name__ == '__main__':
    # crawl_joke_list(1)    
    for i in range(1,10):
        print(i)
        crawl_joke_list(i)    