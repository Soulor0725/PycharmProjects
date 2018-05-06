#五角星的绘制。绘制一个红色的五角星图形，如图所示。

from turtle import *
from time import *
fillcolor("red")
begin_fill()
while True:
	forward(200)
	right(144)
	if abs(pos())<1:
		break
sleep(5)
end_fill()