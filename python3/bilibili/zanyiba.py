# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zanyiba
   Description :
   Author :       XWH
   date：          2018/3/6
-------------------------------------------------
   Change Activity:
                   2018/3/6:
-------------------------------------------------
"""
import re

import requests

__author__ = 'XWH'

class Spider:
    def __init__(self):
        self.session = requests.Session()

    def run(self,start_url):
        img_ids = self.get_img_item_ids(start_url)
        print (img_ids)

    def get_img_item_ids(self,start_url):
        response = self.download(start_url)
        if response:
            html = response.text
            ids = re.findall(r'http://www.27270.com/word/gaoxiaoqutu/2015/(\d+).html',html)
            return set(ids)

    def download(self,url):
        try:
            html = self.session.get(url)
            return html
        except Exception as e:
            print(e)

if __name__ == '__main__':
    spider = Spider()
    spider.run('http://www.27270.com/word/gaoxiaoqutu/')