import requests
import re
import json
from gevent import monkey; monkey.patch_ssl()

import csv
import os

fileName = 'douban.csv'
def write_to_csv(movies_dict_json):
    with open(fileName,"a") as csvfile: 
        writer = csv.writer(csvfile)

        # 判断是否有内容
        size = os.path.getsize(fileName)
        if size == 0:
            writer.writerow(["电影名称","评分","评分来源"])

        #写入多行用writerows
        for movie in movies_dict_json:
            name = movie['ename']
            score = movie['additional'].split(':')[1]
            score_source = movie['additional'].split(':')[0]
            
            writer.writerow([name,score,score_source])
         

def crawl(page):
    pn = page*8
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28286&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E7%94%B5%E5%BD%B1&sort_key=16&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn="+ str(pn) +"&rn=8&cb=jQuery110206836959425005356_1525621153468&_=1525621153471"
    res = requests.get(url,verify=False)
    json_str_re = re.compile("{.*}")
    json_str = json_str_re.search(res.text).group()
    # 字符串转成字典
    movies_dict = json.loads(json_str)

    movies_dict_json = movies_dict["data"][0]['result']

    write_to_csv(movies_dict_json)
    # for movie in movies_dict_json:
    #     name = movie['ename']
    #     score = movie['additional']
    #     print("电影:"+name+'\t'+'评分:'+score)


if __name__ == "__main__":
    
    if os.path.exists(fileName):
        # 删除文件
        print('删除文件')
        os.remove(fileName)
    
    for i in range(0,50):
        crawl(i)    