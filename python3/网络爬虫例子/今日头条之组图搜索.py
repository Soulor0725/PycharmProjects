import requests
import json
import re
import os 
import time

import sys    
reload(sys)  
sys.setdefaultencoding('utf8')   

def craw_group(name):
    # url = 'https://www.toutiao.com/api/pc/feed/?category=%E7%BB%84%E5%9B%BE&utm_source=toutiao&max_behot_time=0&as=A1F5CA1F97DEC9E&cp=5AF77E9C593E5E1&_signature=G5ojKQAAQXGbs2BWN.IppRuaIz'
    url = "https://www.toutiao.com/api/pc/feed/?"
    param = {
        "category":name,
        "utm_source":"toutiao",
        "max_behot_time":"0",
        "as":"A1F5CA1F97DEC9E",
        "cp":"5AF77E9C593E5E1",
        "_signature":"G5ojKQAAQXGbs2BWN.IppRuaIz"
    }

    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }
    res = requests.get(url,params=param,headers=header)

    # 字符串 转 字典
    dict_json = json.loads(res.text)

    # 字典数组
    for item in dict_json["data"]:
        item_id = item["item_id"]
        image_count = item["gallary_image_count"]
        
        craw_images(item['item_id'],image_count)
        time.sleep(1)

def craw_images(id,image_count):
    url = "https://www.toutiao.com/a"+id
    
    # 因为浏览器的原因
    header ={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }
    response = requests.get(url,headers=header)
    

    # 获取名称
    title = re.findall(r"title: '(.*?)',",response.content)[0]
    title = "({0}){1}".format(image_count,title)
    
    fileDir = './image/'+title+'/'
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)

    # 获取图片
    string_json = re.findall(r"gallery: JSON.parse\((.*?)\),",response.content)[0]
    dict_json = json.loads(string_json)
    
    # 不知道为什么需要转两次
    dict_json = json.loads(dict_json)
    
    # 获取图片描述
    image_desc = dict_json[r"sub_abstracts"]
    for i in range(len(image_desc)):
        print(image_desc[i])

    for i in range(len(dict_json["sub_images"])):
        item = dict_json["sub_images"][i]
        url = item["url"]

        # image_name = url.strip().split("/")[-1]
        image_name = image_desc[i]
        if not len(image_desc[i]):
            image_name = url.strip().split("/")[-1]
            
        image_name = str(i+1)+"、"+image_name    
        image_path = fileDir+image_name
        save_image(url,image_path)
        
def save_image(url,image_path):
    image = requests.get(url,stream=True)    
    with open(image_path,'wb') as fn:
        fn.write(image.content)

if __name__ == '__main__':
    craw_group("组图")
    # craw_images(id)