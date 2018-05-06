#阶乘
def fact(n):
	if n<=1:
		return 1
	else:
		return n*fact(n-1)	
def main():
	n=eval(input("please input a value:"))
	print("n!={}".format(fact(n)))

main()	