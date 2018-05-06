print("空气质量提醒:")

def main():
	PM=eval(input("What is today's PM2.5?"))
	if PM>75:
		print("不咋滴，小心")
	else:
		print("还行吧，let's go")	

main()