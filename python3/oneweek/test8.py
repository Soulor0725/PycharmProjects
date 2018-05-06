#太阳花的绘制。绘制一个太阳花的图形，如图所示。

from turtle import *
from time import *
color('red','yellow')
begin_fill()
while  True:
	forward(200)
	left(170)
	if abs(pos())<1:
		break
end_fill()
sleep(5)
done