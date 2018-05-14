import requests
import json,re
import os 

import sys
reload(sys)
sys.setdefaultencoding('utf8')   

def getGroupID(search_content,offset):
    url = "https://www.toutiao.com/search_content/?"
    param = {
        "offset":offset,
        "format":"json",
        "keyword":search_content,
        "autoload":"true",
        "count":20,
        "cur_tab":1,
        "from":"search_tab"
    }
    header = {
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }

    response = requests.get(url,params=param,headers=header)
    dict_json = json.loads(response.content)
    
    # 数组
    arrayResult = []
    arrayData = dict_json["data"]
    for i in range(1,len(arrayData)):
        item = arrayData[i]
        # 先判断是不是视频
        if item.get("has_video") == False:
        
            group_id = item.get("group_id",'not exist')
            title = item.get("title",'not exist')
            datetime = item.get("datetime",'not exist')
            
            arrayResult.append(item)

            get_article(group_id)

def get_article(article_id):
    url = "https://www.toutiao.com/a"+article_id

    header ={
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
        }
    response = requests.get(url,headers=header)
    
    title = re.findall("title: '(.*?)',",response.content)[0]
    content = re.findall("content: '(.*?)',",response.content)[0]
    
    save_artcle(title,content)

def save_artcle(title,content):

    fileDir = "./article/"
    if not os.path.exists(fileDir):
        os.mkdir(fileDir)
    
    fileName = fileDir+title+".txt"
    with open(fileName,"wb") as fn:
        fn.write(content)        

if __name__ == '__main__':
    for i in range(10):
        getGroupID("战略家",i)
    