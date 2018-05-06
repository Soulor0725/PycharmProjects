# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     smtp
   Description :
   Author :       XWH
   date：          2018/2/3
-------------------------------------------------
   Change Activity:
                   2018/2/3:
-------------------------------------------------
"""
__author__ = 'XWH'

# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from utils.configure import *

def sendmail(orderId):
    msg_from = email_from
    passwd =  email_passwd
    msg_to = email_to

    subject = "12306_Python自动抢票结果"  # 主题
    content =  msg = '您已成功订购火车票！请在30分钟内前往12306官方网站(https://kyfw.12306.cn/otn/login/init)进行支付！\n\n\
        订单号：{0}\n\
        发车时间：{1}\n\
        乘车人：{2}\n\
        出发地：{3}\n\
        目的地：{4}\n\
        票类型：{5}\n\
        座位类型：{6}'.format(orderId,train_date,username_buy,from_city,to_city,seat_name,ticket_type_zh)
        # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.163.com", 465)# 邮件服务器及端口号 qq->"smtp.qq.com", 465
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print "EMAIL发送成功"
    except:
        print "EMAIL发送失败"
    finally:
        s.quit()