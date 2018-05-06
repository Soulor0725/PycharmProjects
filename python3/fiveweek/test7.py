from turtle import *
from time import *

def tree(plist,l,a,f):
	if l>5:
		lst=[]
		for p in plist:
			p.forward(l)
			q=p.clone()
			p.left(a)
			q.right(a)
			lst.append(p)
			lst.append(q)
		tree(lst,l*f,a,f)	

def maketree(x,y):
	p=Turtle()
	p.speed(1)
	p.color("green")
	p.pensize(5)
	p.hideturtle()

	p.getscreen().tracer(30,0)
	
	p.left(90)#调整画笔
	
	p.penup()
	p.goto(x,y)
	
	p.pendown()

	t=tree([p],110,65,0.6375)


def main():
	maketree(0,0)
	sleep(5)

main()	