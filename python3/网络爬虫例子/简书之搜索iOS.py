import requests
import re
import json
import csv
import os
import time

import sys    
reload(sys)  
sys.setdefaultencoding('utf8')   

fileName = 'jianshu.csv'
def write_to_csv(array_result):
    with open(fileName,'a') as f:
        writer = csv.writer(f)

        # 判断是否有内容
        size = os.path.getsize(fileName)
        if size == 0:
            writer.writerow(["作者","标题",'文章地址',"内容"])

        for item in array_result:
            url = 'https://www.jianshu.com/p/'+item['slug']
            writer.writerow([item['username'],item['title'],url,item['content']])

def crawl(page):
    url = 'https://www.jianshu.com/search/do?'

    params = {
        "q":"iOS",
        "type":"note",
        "page":str(page),
        "order_by":"default",
    }
    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }
    
    res = requests.post(url,params,headers=header)

    # 字符串转成字典结构
    dict_json = json.loads(res.content)


    array_result = []
    for item in dict_json["entries"]:
        user_name = item['user']['nickname']
        user_name_re = re.split('<em class=\'search-result-highlight\'>|</em>',user_name)
        user_name = ''.join(user_name_re)

        title = item['title']
        title_re = re.split('<em class=\'search-result-highlight\'>|</em>',title)
        title = ''.join(title_re)

        content = item['content']
        content_re = re.split('<em class=\'search-result-highlight\'>|</em>',content)
        content = ''.join(content_re)

        # print(user_name,title,content)

        dict_result={}
        dict_result['username'] = user_name
        dict_result['title'] = title
        dict_result['content'] = content
        
        dict_result['slug'] = item['slug']


        array_result.append(dict_result)            
    write_to_csv(array_result)    
    time.sleep(3)


if __name__ == '__main__':
    if os.path.exists(fileName):
       print("删除")
       os.remove(fileName)

    for i in range(1,10):
        crawl(i)