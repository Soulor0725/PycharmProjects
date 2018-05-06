#计算两点之间的距离
from math import *
def square(x):
	return pow(x,2)

def distance(x1,y1,x2,y2):
	return sqrt(square(abs(x1-x2))+square(abs(y1-y2)))

def main():
	a,b=eval(input("please a and b:"))
	print("距离是：",distance(a,a,b,b))

main()	