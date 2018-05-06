from math import *
def main():
	print("寻找实数去开根")
	a,b,c=eval(input("输入三个实数(a,b,c):"))
	delta=b*b-4*a*c 
	if delta>=0:
		discRoot=sqrt(delta)
		root1=(-b+discRoot)/(2*a)
		root2=(-b-discRoot)/(2*a)
		print("\n the solution are:",root1,root2)
	else:
		print("the result is no real roots")	

main()