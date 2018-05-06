print("布尔值：")

a,b=eval(input())
while True:
	if a>15 or b>15 or a>7 or b>7:
		break
	else:
		print("继续输入：")
		a,b=eval(input())