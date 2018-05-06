# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mmkao
   Description :
   Author :       XWH
   date：          2018/3/6
-------------------------------------------------
   Change Activity:
                   2018/3/6:
-------------------------------------------------
"""
import requests
import re

__author__ = 'XWH'

class Spider:
    def __init__(self):
        self.session = requests.Session()

    def run(self,start_url):
        print('start...')
        img_ids = self.get_item_ids(start_url)
        print(img_ids)

    def get_item_ids(self,start_url):
        response = self.download(start_url)
        print(response)
        if response:
            html = response.text
            # ids = re.findall(r'http://www.mmkao.net/Photo/201710/(\d+).jpg',html)
            ids = re.findall(r'http://www.27270.com/ent/meinvtupian/2015/(\d+).html',html)
            return set(ids)

    def download(self,start_url):
        try:
            print(start_url)
            result = self.session.get(start_url)
            print(result)
            return result
        except Exception as e:
            print(e)

if __name__ == "__main__":
    spider = Spider()
    # start_url = 'http://mmkao.net/DISI/'
    start_url = 'http://www.27270.com/zt/90hou'
    spider.run(start_url)
    