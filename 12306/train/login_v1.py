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

import urllib
import json
from utils.cons import *
from PIL import Image
from train.orderTicket import *

# 获取验证码图片
def get_verify_code():
  req = urllib2.Request(url_captcha_image)
  req.headers = headers
  result = opener.open(req).read()
  # print result
  with open(name_verification_code,'wb') as fn:
      fn.write(result)

# 显示图片
def showCodeImage():
    imageCode = Image.open(name_verification_code)
    print imageCode
    # 展示验证码图片，会调用系统自带的图片浏览器打开图片，线程阻塞
    imageCode.show()
    # 关闭，只是代码关闭，实际上图片浏览器没有关闭，但是终端已经可以进行交互了(结束阻塞)
    imageCode.close()



# 手动验证验证码
def manual_input_code_value():
    print("""-----------------
| 1 | 2 | 3 | 4 |
-----------------
| 5 | 6 | 7 | 8 |
-----------------""")
    solution = raw_input("输入验证码索引(见上图，以','分割）: ")
    # 一共有8个验证码，验证码我们编号从做到右从上到下，依次为0，1，2，3，4，5，6，7（程序员思维，见谅），为序号转坐标做准备
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
        try:
            yanList.append(yanSol[int(item)-1])
        except:
            main()
    # 正确验证码的坐标拼接成字符串，作为网络请求时的参数
    code = ','.join(yanList)
    return code

# 联网验证验证结果
def captcha_check(code):
    
    data = {
        'answer':code,
        'login_site':'E',
        'rand':'sjrand',
    }
    data = urllib.urlencode(data) # 把字典类型转换成查询字符串

    req = urllib2.Request(url_captcha_check)
    req.headers = headers
    
    html = opener.open(req,data=data).read()
    result = json.loads(html)

    if result['result_code'] == '4':
        print '-----{0}-----'.format(result['result_message'])
    else:
        print '-----{0}-----'.format(result['result_message'])
        main()


# 登陆
def web_login():
    print '-----{0}-----'.format("登陆中")

    data = {
        'username':username,
        'password':password,
        'appid':'otn',
    }
    data = urllib.urlencode(data)

    req = urllib2.Request(url_web_login)
    req.headers = headers
    html = opener.open(req,data=data).read()
    result = json.loads(html)
    # print(result)
    if result['result_code'] == 0:
        print '-----{0}-----'.format(result['result_message'])
    else:
        print '-----{0}-----'.format(result['result_message'])



# 第一次认证
def web_auth_login():
    yzData = {
            'appid':'otn'
    }
    yzData = urllib.urlencode(yzData)

    req = urllib2.Request(url_web_auth_login)
    req.headers = headers
    html = opener.open(req,data=yzData).read()
    result = json.loads(html)

    if result['result_code'] == 0:
        print'-----第一次认证{0}-----'.format(result['result_message'])
    else:
        print'-----第一次认证{0}-----'.format(result['result_message'])

    loginMessage = result[u'newapptk']
    return loginMessage

# 第二次认证
def uamauthclient(loginMessage):

    data = {
            'tk': loginMessage
    }
    data = urllib.urlencode(data)

    req = urllib2.Request(url_uamauthclient)
    req.headers = headers
    html = opener.open(req,data=data).read()
    try:
        result = json.loads(html)

        if result['result_code'] == 0:
            print'-----第二次认证{0}-----'.format(result['result_message'])
        else:
            print'-----第二次认证{0}-----'.format(result['result_message'])
            exit()
        apptk = result['apptk']
        return apptk
    except:
        print('第二次认证失败，重新登陆')
        main()

def main():

    if not 2300 > int(time.strftime("%H%M")) > 0600:
        print("现在是系统例行维护时间（23:00-06:00），在此期间不受理订票和改签业务 ")
        exit()

    get_verify_code()
    showCodeImage()
             
    code = manual_input_code_value()
    captcha_check(code)
    web_login()
    loginMessage = web_auth_login()
    uamauthclient(loginMessage)
    print '\n\n'

    startBuyTicket()

if __name__ == '__main__':
    main()