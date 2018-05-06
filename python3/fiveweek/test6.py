#绘制三角形
from turtle import *

p=Turtle()
p.speed(1)
p.pensize(5)
p.fillcolor("red")
p.begin_fill()
for i in range(3):
	p.forward(200)
	p.right(-120)
p.end_fill()	
	