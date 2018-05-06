import turtle 
def main():
	turtle.title('数据驱动的动态路径绘制')
	turtle.setup(800,600,0,0)

	pen=turtle.Turtle()
	pen.width(5)
	pen.shape("turtle")
	pen.speed(10)
	pen.lt(36)

	#read file
	result=[]
	file=open("values.txt","r")
	for line in file:
		result.append(list(map(int,line.split(','))))
	print(result)	

	#draw
	for i in range(len(result)):
		pen.color(result[i][3],result[i][4],result[i][5])
		pen.forward(result[i][0])
		if result[i][1]:
			pen.rt(result[i][2])
		else:
			pen.lt(result[i][2])
	pen.goto(0,0)		

main()