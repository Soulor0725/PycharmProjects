# -*- coding: utf-8 -*-

import requests
import re
# response = requests.get('https://httpbin.org/get')
# # print(type(response))
# # print(response.status_code)
# # print(response.cookies)
# print(response.text)
# print(response.json())

# data = requests.get('http://d.hiphotos.baidu.com/image/pic/item/43a7d933c895d1435eac3d047ff082025aaf073b.jpg').content
# with open('meinv.jpg','wb') as f:
#     f.write(data)
#     f.close()

response = requests.get('https://mp.weixin.qq.com/s/CIPosICgva9haqstMDIHag')
html = response.text
result = re.findall(r'<span style="letter-spacing: 1px;">(.*?)</span>', html)
for title in result:
    with open('jiagoushi.txt', 'a') as f:
        f.write(title)
        # f.close()