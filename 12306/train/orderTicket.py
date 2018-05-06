# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12306_buy
   Description :
   Author :       XWH
   date：          2018/2/4
-------------------------------------------------
   Change Activity:
                   2018/2/4:
-------------------------------------------------
"""
__author__ = 'XWH'

import datetime
import time
import re
import io
from utils.cons import *
from utils.configure import *
from train.searchTicket import *
import urllib

class OrderConfig():
    # def __init__(self,count):
    count = 0

# 开始抢票
def startBuyTicket():
    print '-----{0}-----'.format("开始抢票了。。。")

    # 提交下单请求
    submitOrderRequest()

    # 确认旅客票（单程、返程）类型
    html = getGlobalRepeatSubmitTokenValue()
    ticketInfoForPassengerForm = decodeTicketInfoForPassengerForm(html)
    globalRepeatSubmitToken = re.findall(r"var globalRepeatSubmitToken = '(.*)'", html)[0]

    # 获取所有乘客信息列表
    passengers = getPassengersInfo(globalRepeatSubmitToken)
    passengerTicketStr,oldPassengerStr = getNeedBuyPassengerInfo(passengers)

    # 检测订单信息
    checkOrderInfo(ticketInfoForPassengerForm,globalRepeatSubmitToken,passengerTicketStr,oldPassengerStr)

    # 获取余票和排队信息
    getQueueCount(ticketInfoForPassengerForm,globalRepeatSubmitToken)

    # 订单入队确认
    confirmGoForQueue(ticketInfoForPassengerForm,globalRepeatSubmitToken,passengerTicketStr,oldPassengerStr)

    # 获取订单id
    orderId = waitForOrderId(ticketInfoForPassengerForm,globalRepeatSubmitToken)

    if orderId:
        sendmail(orderId)

    # 查看订单结果
    # getResultOrder(globalRepeatSubmitToken,orderId)

# 检测订单信息
def checkOrderInfo(ticketInfoForPassengerForm,globalRepeatSubmitToken,passengerTicketStr,oldPassengerStr):
    print '-----{0}-----'.format("开始检测订单信息")
    cancel_flag = ticketInfoForPassengerForm['orderRequestDTO']['cancel_flag'] or '2'
    bed_level_order_num = ticketInfoForPassengerForm['orderRequestDTO']['bed_level_order_num'] or '000000000000000000000000000000'
    tour_flag = ticketInfoForPassengerForm['tour_flag'] or 'dc'

    formData = {
        'cancel_flag':cancel_flag,
        'bed_level_order_num':bed_level_order_num,
        'passengerTicketStr':passengerTicketStr,
        'oldPassengerStr':oldPassengerStr,
        'tour_flag':tour_flag,
        'randCode':'',
        'whatsSelect':'1',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken,
    }
    formData = urllib.urlencode(formData)

    req = urllib2.Request(url_checkOrderInfo)
    req.headers = headers
    html = opener.open(req, data=formData).read()
    result = json.loads(html)

    if result['status'] == True:
        print'-----检测订单信息成功：{0}-----'.format(json.dumps(result['messages'], ensure_ascii=False))
    else:
        print'-----检测订单信息失败：{0}-----'.format(json.dumps(result['messages'], ensure_ascii=False))
        exit()


# 提交下单请求
def submitOrderRequest():
    print '-----{0}-----'.format("提交订单")

    secretStrValue_list = getSecretStrValue()
    if not secretStrValue_list:
        print('乘客信息获取失败')
        exit()
    # 编码问题
    secretStrValue_list = urllib.unquote(secretStrValue_list).replace('\n', '')

    formData = {
        'secretStr':secretStrValue_list,
        'train_date':tomorrow,
        'back_train_date':today,
        'tour_flag':'dc',# 单程，返程
        'purpose_codes':'ADULT',
        'query_from_station_name':from_city,
        'query_to_station_name':to_city,
        'undefined':''
    }
    formData = urllib.urlencode(formData)

    req = urllib2.Request(url_submitOrder)
    req.headers = headers
    html = opener.open(req, data=formData).read()
    try:
        result = json.loads(html)
        if result['status'] == True:
            print'-----提交下单请求成功：{0}-----'.format(json.dumps(result[u'messages'], ensure_ascii=False))
        else:
            print'-----提交下单请求失败：{0}-----'.format(json.dumps(result[u'messages'], ensure_ascii=False))
            getTickList()
    except:
        print('提交下单请求失败,重新获取余票信息')
        getTickList()        


# 获取globalRepeatSubmitToken
def getGlobalRepeatSubmitTokenValue():
    formData = {
        '_json_att':''
    }
    formData = urllib.urlencode(formData)

    req = urllib2.Request(url_confirmPassenger_dc)
    req.headers = headers
    html = opener.open(req, data=formData).read()
    return html


# 获取余票和排队信息
def getQueueCount(ticketInfoForPassengerForm,globalRepeatSubmitToken):
    print '-----{0}-----'.format("开始获取余票和排队信息")

    train_date = ticketInfoForPassengerForm['queryLeftTicketRequestDTO']['train_date']
    train_date = time.strptime(train_date,'%Y%m%d')
    train_date = time.strftime("%a %b %d %Y %H:%M:%S GMT+0800 (CST)", train_date)
    train_no = ticketInfoForPassengerForm['queryLeftTicketRequestDTO']['train_no']
    leftTicketStr = ticketInfoForPassengerForm['leftTicketStr']
    purpose_codes = ticketInfoForPassengerForm['purpose_codes']
    train_location = ticketInfoForPassengerForm['train_location']
    station_train_code = ticketInfoForPassengerForm['queryLeftTicketRequestDTO']['station_train_code']

    formData = {
        'train_no': train_no,
        'train_date': train_date,
        'stationTrainCode': station_train_code,
        'seatType': ticket_type_code[ticket_type_zh],
        'fromStationTelecode': city()[from_city],
        'toStationTelecode': city()[to_city],
        'leftTicket': leftTicketStr,
        'purpose_codes': purpose_codes,
        'train_location': train_location,
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': globalRepeatSubmitToken,
    }
    formData = urllib.urlencode(formData)

    req = urllib2.Request(url_getQueueCount)
    req.headers = headers
    html = opener.open(req, data=formData).read()
    result = json.loads(html)

    if result['status'] == True:
        print'-----获取余票和排队信息成功：{0}-----'.format(json.dumps(result['messages'], ensure_ascii=False))
        print('剩余车票:{0} ,目前排队人数: {1}'.format(json.dumps(result['data']['ticket'], ensure_ascii=False),json.dumps(result['data']['count'], ensure_ascii=False)))
    else:
        print'-----获取余票和排队信息失败：{0}-----'.format(json.dumps(result['messages'], ensure_ascii=False))
        exit()
        getTickList()


# 订单入队确认过程
def confirmGoForQueue(ticketInfoForPassengerForm,globalRepeatSubmitToken,passengerTicketStr,oldPassengerStr):
    print '-----{0}-----'.format("开始订单入队确认过程")
    
    purpose_codes = ticketInfoForPassengerForm['purpose_codes']
    key_check_isChange = ticketInfoForPassengerForm['key_check_isChange']
    leftTicketStr = ticketInfoForPassengerForm['leftTicketStr']
    train_location = ticketInfoForPassengerForm['train_location']
    station_train_code = ticketInfoForPassengerForm['queryLeftTicketRequestDTO']['station_train_code']

    # 高铁可选座
    res = re.findall('G', station_train_code)
    choose_seats_value = ''
    if len(res):
        choose_seats_value = choose_seats

    formData = {
        'passengerTicketStr': passengerTicketStr,
        'oldPassengerStr': oldPassengerStr,
        'randCode': '',
        'purpose_codes': purpose_codes,
        'key_check_isChange': key_check_isChange,
        'leftTicketStr': leftTicketStr,
        'train_location': train_location,
        'choose_seats': choose_seats_value,#座位选择，暂时随机
        'seatDetailType':'000',
        'whatsSelect': '1',
        'roomType': '00',
        'dwAll':'N',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken,      
    }
    formData = urllib.urlencode(formData)

    req = urllib2.Request(url_confirmSingleForQueue)
    req.headers = headers
    html = opener.open(req, data=formData).read()
    result = json.loads(html)

    if result['status'] == True:
        print'-----{0}-----'.format('订单入队确认请求成功')
        if result['data']['submitStatus'] == True:
            print'-----订单入队成功-----'
        else:
            print'-----订单入队失败：{0}-----'.format(json.dumps(result['data']['errMsg'], ensure_ascii=False))
            exit()
    else:
        print'-----订单入队确认失败：{0}-----'.format(json.dumps(result['messages'], ensure_ascii=False))
        getTickList()

# 查看订单结果
def getResultOrder(globalRepeatSubmitToken,orderId):
    print '-----{0}-----'.format('查看订单结果')

    formData = {
        'orderSequence_no': orderId,
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': globalRepeatSubmitToken,
    }
    formData = urllib.urlencode(formData)

    req = urllib2.Request(url_resultOrderForDcQueue)
    req.headers = headers
    html = opener.open(req, data=formData).read()
    result = json.loads(html)

    if result['status'] == True:
        print'-----查看订单结果成功----'
    else:
        print'-----查看订单结果失败：{0}-----'.format(json.dumps(result['data']['errMsg'], ensure_ascii=False))
        return False


# 获取订单id
def waitForOrderId(ticketInfoForPassengerForm,globalRepeatSubmitToken):
    print '-----{0}-----'.format('获取订单id')

    count = 0
    while True:
        count += 1
        waitTime, queryOrderWaitTimeStatus, orderId,msg = queryOrderWaitTime(ticketInfoForPassengerForm,globalRepeatSubmitToken)
        print(waitTime,queryOrderWaitTimeStatus,orderId,msg)
        print('[%d]正在等待订单提交结果。。。')
        if waitTime < 0:
            if orderId:
                print('订单提交成功，订单号：%s'% orderId)
                return orderId
            else:
                print('订单提交失败:'+msg)
                return None
        interval = waitTime // 60 #取整除 - 返回商的整数部分
        print ('未出票，订单排队中...预估等待时间: %s 分钟' % (interval if interval <= 30 else '超过30'))
        # 动态调整查询时间
        if interval > 30:
            time.sleep(2 * 60)
        elif interval > 20:
            time.sleep(60)
        elif interval > 10:
            time.sleep(30)
        else:
            time.sleep(3)
    return None

# 排队获取订单
def queryOrderWaitTime(ticketInfoForPassengerForm,globalRepeatSubmitToken):
    print '-----{0}-----'.format('正在排队获取订单')

    formData = {
        'random': '%10d' % (time.time() * 1000),
        'tourFlag': ticketInfoForPassengerForm['tour_flag'] or 'dc',
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': globalRepeatSubmitToken,
    }
    formData = urllib.urlencode(formData)

    req = urllib2.Request(url_queryOrderWaitTime+"?"+formData)
    req.headers = headers
    html = opener.open(req).read()
    result = json.loads(html)

    if result['status'] == True:
        print'-----排队获取订单成功：{0}-----'
        return result['data']['waitTime'],result['data']['queryOrderWaitTimeStatus'],json.dumps(result['data']['orderId'], ensure_ascii=False),result['data']['msg'] if 'msg' in result['data'] else None
    else:
        print'-----排队获取订单失败：{0}-----'.format(json.dumps(result['messages'], ensure_ascii=False))


# 获取ticketInfoForPassengerForm
def decodeTicketInfoForPassengerForm(html):
    try:
        ticketInfoForPassengerForm = re.findall(r'var ticketInfoForPassengerForm=(.*);', html)[0]
        return json.loads(ticketInfoForPassengerForm.replace("'", "\""))
    except:
        if not 2300 > int(time.strftime("%H%M")) > 0600:
            print("现在是系统例行维护时间（23:00-06:00），在此期间不受理订票和改签业务")
        else:
            print("可能是该订单已经存在，请先处理")
        exit()


# 获取secretStr
def getSecretStrValue():
    ticketsInfo_yz = []
    secretStr_list = []

    for i in getTickList()['data']['result']:

        ret = i.split('|')[seat_type_code[seat_name]]
        if ret.isdigit():
            ticketsInfo_yz.append(ret)
        else:
            if ret == u"有":
                ticketsInfo_yz.append(ret)

        if len(ticketsInfo_yz):
            secretStr = i.split('|')[0]
            secretStr_list.append(str(secretStr))

    if len(secretStr_list):
        return secretStr_list[0]
    else:

        OrderConfig.count += 1
        print('第[{0}]查询'.format(OrderConfig.count) +seat_name+'暂未找到，重新查询')
        getSecretStrValue()
        return None


# 得到买票的 passengerTicketStr、oldPassengerStr
def getNeedBuyPassengerInfo(passengers):
    passengerTicketStr = [] # 如果有多个乘客，那么各个乘客之间用一个_分隔
    oldPassengerStr = [] # 如果有多个乘客，那么直接拼接到后面
    for passenger in passengers['data']['normal_passengers']:
        if passenger['passenger_id_no'] == user_idcard_buy:
            # passengerTicketStr 这个参数的组合方式为：1(seatType),0,1(车票类型:ticket_type_codes),张三(passenger_name),1(证件类型:passenger_id_type_code),320xxxxxx(passenger_id_no),151xxxx(mobile_no),N
            passengerTicketStr.append(ticket_type[seat_name])
            passengerTicketStr.append('0')#因为少了一个参数，调试许久
            passengerTicketStr.append(ticket_type_code[ticket_type_zh])
            passengerTicketStr.append(passenger['passenger_name'])
            passengerTicketStr.append(passenger['passenger_id_type_code'])
            passengerTicketStr.append(passenger['passenger_id_no'])
            passengerTicketStr.append(passenger['mobile_no'])
            passengerTicketStr.append('N')#似乎为默认值

            oldPassengerStr.append(passenger['passenger_name'])
            oldPassengerStr.append(passenger['passenger_id_type_code'])
            oldPassengerStr.append(passenger['passenger_id_no'])
            oldPassengerStr.append(ticket_type_code[ticket_type_zh]+'_') #似乎为默认值

    return ','.join(passengerTicketStr),','.join(oldPassengerStr)


# 获取乘客信息
def getPassengersInfo(globalRepeatSubmitToken):

    formData = {
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken
    }
    formData = urllib.urlencode(formData)

    req = urllib2.Request(url_getPassengerDTOs)
    req.headers = headers
    html = opener.open(req, data=formData).read()
    result = json.loads(html)

    if result['status'] == True:
        print'-----获取乘客信息成功：{0}-----'.format(json.dumps(result['data']['exMsg'], ensure_ascii=False))
        return result
    else:
        print'-----获取乘客信息失败：{0}-----'.format(json.dumps(result['data']['exMsg'], ensure_ascii=False))
        getPassengersInfo(globalRepeatSubmitToken)


# def main():
#     orderId = 'R57888'
#     if orderId:
#         sendmail(orderId)
#
#
# if __name__ == '__main__':
#     main()

