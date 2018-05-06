# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     获取豆瓣上舌尖上的中国3评论
   Description :
   Author :       XWH
   date：          2018/3/9
-------------------------------------------------
   Change Activity:
                   2018/3/9:
-------------------------------------------------
"""
__author__ = 'XWH'

import requests
import re

cookie = {'Cookie':'ll="118282"; bid=Wgkew3FktNk; __utma=30149280.1011446617.1514816664.1517628811.1520525306.8; __utmc=30149280; __utmz=30149280.1520525306.8.8.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1902279383.1520525317.1520525317.1520525317.1; __utmb=223695111.0.10.1520525317; __utmc=223695111; __utmz=223695111.1520525317.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1520525317%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E8%2588%258C%25E5%25B0%2596%25E4%25B8%258A%25E7%259A%2584%25E4%25B8%25AD%25E5%259B%25BD%22%5D; _pk_ses.100001.4cf6=*; _vwo_uuid_v2=D0563EBC9C558892A667BEF40709C773A|3146fe02b15d5a821de578daf664d4fc; __utmt=1; __utmb=30149280.7.10.1520525306; ap=1; ps=y; dbcl2="150915621:lGpfOEF8S30"; ck=JgUE; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=2233e90295c748d8.1520525317.1.1520529036.1520525317.'}

for m in range(0,2000,20):
    # 网址
	url = 'https://movie.douban.com/subject/25875034/comments?start={0}&limit=20&sort=new_score&status=P&percent_type='.format(m)
	print(url)
	html = requests.get(url, cookies = cookie)

	data = re.findall('<p class=""> (.*?)\n        </p>',html.text)
	print(len(data))
	if len(data):
		with open('comment.txt','a') as ff:
		    for n in data:
		        ff.write(n+'\n\n')
	# else:
	# 	exit()