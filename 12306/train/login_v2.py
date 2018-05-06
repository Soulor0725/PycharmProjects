# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12306-login
   Description :
   Author :       XWH
   date：          2018/1/31
-------------------------------------------------
   Change Activity:
                   2018/1/31:
-------------------------------------------------
"""
# https://www.jianshu.com/p/ca93eba60609

# python v2.7
__author__ = 'XWH'

import urllib2
import urllib
import ssl
import cookielib
import user
import json
from cons import *
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

c = cookielib.LWPCookieJar()
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)


# 获取验证码图片
req = urllib2.Request(url_verification_code_get_v2)
req.headers = headers
codeimg = opener.open(req).read()
with open(name_verification_code,'wb') as fn:
    fn.write(codeimg)


# 手动验证验证码
imageCode = Image.open(name_verification_code)
# 展示验证码图片，会调用系统自带的图片浏览器打开图片，线程阻塞
imageCode.show()
# 关闭，只是代码关闭，实际上图片浏览器没有关闭，但是终端已经可以进行交互了(结束阻塞)
imageCode.close()
solution = raw_input('请输入验证码位置，以","分割[例如2,5]:')

# 一共有8个验证码，验证码我们编号从做到右从上到下，依次为0，1，2，3，4，5，6，7（程序员思维，见谅），为序号转坐标做准备
# --------------------------------------------------
#              |               |                |
#      0       |       1       |        2       |       3
#              |               |                |
# --------------------------------------------------
#              |               |                |
#      4       |       5       |        6       |       7
#              |               |                |
# --------------------------------------------------
# 大约一个验证码的宽高在70左右，所以每个验证码的坐标中点大约为，注意大约，请勿上纲上线
# -------------------------------------------------------
#               |                |               |
#     35,35     |     105,35     |     175,35    |    245,35
#               |                |               |
# -------------------------------------------------------
#               |                |               |
#     35,105    |     105,105    |     175,105   |    245,105
#               |                |               |
# -------------------------------------------------------

# 分割用户输入的验证码位置
soList = solution.split(',')
# 由于12306官方验证码是验证正确验证码的坐标范围,我们取每个验证码中点的坐标(大约值)
yanSol = ['35,35','105,35','175,35','245,35','35,105','105,105','175,105','245,105']
yanList = []
for item in soList:
    # print (int(item)-1)
    yanList.append(yanSol[int(item)-1])
# 正确验证码的坐标拼接成字符串，作为网络请求时的参数
code = ','.join(yanList)

req = urllib2.Request(url_verification_code_check_v2)
data = {
    'answer':code,
    'login_site':'E',
    'rand':'sjrand',
}
data = urllib.urlencode(data) # 把字典类型转换成查询字符串
req.headers = headers
# print data
html = opener.open(req,data=data).read()
result = json.loads(html)

if result['data']['result'] == '1':
    print '-----{0}-----'.format(result['data']['msg'])
else:
    print '-----{0}-----'.format(result['data']['msg'])
    exit()


# 登陆
print '-----{0}-----'.format("登陆中")
req = urllib2.Request(url_login)
req.headers = headers
data = {
    'username':user.username,
    'password':user.password,
    'appid':'otn',
}
data = urllib.urlencode(data)
html = opener.open(req,data=data).read()
result = json.loads(html)
# print(result)
if result['result_code'] == 0:
    print '-----{0}-----'.format(result['result_message'])
else:
    print '-----{0}-----'.format(result['result_message'])
    exit()



# 第一次验证
req = urllib2.Request(url_login_verify_first)
req.headers = headers

yzData = {
        'appid':'otn'
}
yzData = urllib.urlencode(yzData)
html = opener.open(req,data=yzData).read()
result = json.loads(html)

if result['result_code'] == 0:
    print'-----第一次{0}-----'.format(result['result_message'])
else:
    print'-----第一次{0}-----'.format(result['result_message'])
    exit()

loginMessage = result[u'newapptk']

# 第二次验证开始
req = urllib2.Request(url_login_verify_second)
req.headers = headers

data = {
        'tk': loginMessage
}
data = urllib.urlencode(data)
html = opener.open(req,data=data).read()
result = json.loads(html)

if result['result_code'] == 0:
    print'-----第二次{0}-----'.format(result['result_message'])
else:
    print'-----第二次{0}-----'.format(result['result_message'])
    exit()
apptk = result['apptk']
print 'apptk:',apptk
