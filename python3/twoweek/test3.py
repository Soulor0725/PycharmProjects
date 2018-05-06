#输入数字输出中文星期
weeks="星期一星期二星期三星期四星期五星期六星期日"
n=input("输入数字1-7：")
pos=(int(n)-1)*3
weeksday=weeks[pos:pos+3]
print("是："+weeksday)