import requests
import re
import os

def crawl_image(image_url,image_local_path):
    r = requests.get(image_url,stream=True)
    # print(image_local_path)
    with open(image_local_path,'wb') as fn:
        fn.write(r.content)


def crawl(page):
    url = 'https://www.qiushibaike.com/imgrank/page/'+str(page)

    res = requests.get(url)

    html = res.content.decode('utf-8')

    content_list = re.findall('<div class=\"thumb\">(.*?)</div>',html,re.S)

    for content in content_list:
        image_list = re.findall("<img src=\"(.*?)\" alt=",content)
        # print(image_list)
        for image_url in image_list:
            image_url = 'https:'+image_url
            # print(image_url)            
            print(image_url.strip().split("/")[-1])
            crawl_image(image_url,'./image/'+image_url.strip().split("/")[-1])
    


if __name__ == '__main__':
    if not os.path.exists('./image'):
        os.mkdir('./image')
    for i in range(1,10):
        crawl(i)    