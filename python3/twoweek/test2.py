#三角形绘制
from turtle import *

def drawAng():
	
	for i in range(3): 
		turtle.seth(i*120) 
		turtle.fd(100)

def main():
 	drawAng

main() 	 