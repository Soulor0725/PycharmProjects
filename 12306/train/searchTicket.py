# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12306
   Description :
   Author :       XWH
   date：          2018/1/31
-------------------------------------------------
   Change Activity:
                   2018/1/31:
-------------------------------------------------
"""
# python v2.7
__author__ = 'XWH'


from utils.cons import *
from prettytable import PrettyTable
from colorama import init, Fore
from utils.smtp import *
import time

# 获取余票信息
def getTickList():
    print '-----{0}-----'.format("开始获取余票信息")
    from_station = city()[from_city]
    to_station = city()[to_city]

    # 实例一个请求对象
    url = url_leftTicket + 'leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(train_date,from_station,to_station)
    req = urllib2.Request(url)
    req.headers = headers
    html = urllib2.urlopen(req).read()
    try:
        result = json.loads(html)
        if result['status'] == True:
            print'-----获取余票信息成功：{0}-----'.format(json.dumps(result['messages'], ensure_ascii=False))
            return result
        else:
            print'-----获取余票信息失败：{0}-----'.format(json.dumps(result['messages'], ensure_ascii=False))
            getTickList()
    except:
        print'获取余票信息失败,重新获取余票信息'
        time.sleep(5)
        getTickList()



"""
23：软卧
26：无座
28：硬卧
29：硬座
30：二等座
31：一等座
"""
# 开始搜索
def start_search():
    print '-----{0}-----'.format("开始搜索")
    ticketsInfo_yz = []
    ticketsInfo_yw = []
    ticketsInfo_edz = []
    for i in getTickList()['data']['result']:

        ret = i.split('|')[29]
        if ret.isdigit():
            ticketsInfo_yz.append(ret)
        else:
            if ret == u"有":
                ticketsInfo_yz.append(ret)

        ret = i.split('|')[28]
        if ret.isdigit():
            ticketsInfo_yw.append(ret)
        else:
            if ret == u"有":
                ticketsInfo_yw.append(ret)

        ret = i.split('|')[30]
        if ret.isdigit():
            ticketsInfo_edz.append(ret)
        else:
            if ret == u"有":
                ticketsInfo_edz.append(ret)

    ticketsInfo = []
    if len(ticketsInfo_edz):
        ticketsInfo.append('二等座')

    if len(ticketsInfo_yz):
        ticketsInfo.append('硬座')

    if len(ticketsInfo_yw):
        ticketsInfo.append('硬卧')


    if len(ticketsInfo):
        result_last = json.dumps(ticketsInfo, ensure_ascii=False)# 为了打印信息
        msg = "尊敬的用户" + username + ":\n" + "您好!\n" + "系统已经监测到(" + train_date + ")" + from_city + "-->" + to_city + "所有车次有余票，可以下单了!!!"
        msg = msg+'详细情况如下：\n\n'+','.join(ticketsInfo)
        print msg
        sendmail(msg)


class TrainsRow:
    header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()

    def __init__(self, r, station):
        self.trains = r
        self.station = station

    @property
    def get_trains(self):
        trains = self.trains
        trains_show = []
        for train in trains:
            cm = train.split('|')
            cq = {}
            cq['train_no'] = cm[2]#车票号
            cq['station_train_code'] = cm[3]#车次
            cq['start_station_telecode'] = cm[4]#起始站代号
            cq['end_station_telecode'] = cm[5]#终点站代号
            cq['from_station_telecode'] = cm[6]#出发站代号
            cq['to_station_telecode'] = cm[7]#到达站代号
            cq['start_time'] = cm[8]#出发时间
            cq['arrive_time'] = cm[9]#到达时间
            cq['lishi'] = cm[10]#历时
            cq['canWebBuy'] = cm[11]#是否能购买：Y 可以
            cq['yp_info'] = cm[12]
            cq['start_train_date'] = cm[13]#出发日期
            cq['train_seat_feature'] = cm[14]
            cq['location_code'] = cm[15]
            cq['from_station_no'] = cm[16]
            cq['to_station_no'] = cm[17]
            cq['is_support_card'] = cm[18]
            cq['controlled_train_flag'] = cm[19]
            cq['gg_num'] = cm[20] and cm[20] or '--'
            cq['gr_num'] = cm[21] and cm[21] or '--'
            cq['qt_num'] = cm[22] and cm[22] or '--'
            cq['rw_num'] = cm[23] and cm[23] or '--'#软卧
            cq['rz_num'] = cm[24] and cm[24] or '--'#软座
            cq['tz_num'] = cm[25] and cm[25] or '--'
            cq['wz_num'] = cm[26] and cm[26] or '--'#无座
            cq['yb_num'] = cm[27] and cm[27] or '--'
            cq['yw_num'] = cm[28] and cm[28] or '--'#硬卧
            cq['yz_num'] = cm[29] and cm[29] or '--'
            cq['ze_num'] = cm[30] and cm[30] or '--'
            cq['zy_num'] = cm[31] and cm[31] or '--'#一等座
            cq['swz_num'] = cm[32] and cm[32] or '--'#等座
            cq['srrb_num'] = cm[33] and cm[33] or '--'#商务特等座
            cq['yp_ex'] = cm[34]
            cq['ticket_types'] = cm[35]
            trains_show.append(cq)

            train_show = [
                cq['station_train_code'],
                (Fore.RED + self.station[cq['from_station_telecode']] + Fore.RESET),
                cq['start_time'],
                cq['lishi'],
                cq['zy_num'],
                cq['ze_num'],
                cq['rw_num'],
                cq['yw_num'],
                cq['yz_num'],
                cq['wz_num'],
            ]
            train_time_show = [
                '',
                (Fore.GREEN + self.station[cq['to_station_telecode']] + Fore.RESET),
                cq['arrive_time'],
                '',
                '',
                '',
                '',
                '',
                '',
                '',
            ]
            yield train_show
            yield train_time_show

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.get_trains:
            pt.add_row(train)
        print(pt)

# 展示余票信息
def show_ticks_list():
    result = getTickList()['data']['result']
    station = getTickList()['data']['map']
    TrainsRow(result, station).pretty_print()


def main():
    sendmail('hhh')
    show_ticks_list()
    getTickList()

if __name__ == '__main__':
    main()




