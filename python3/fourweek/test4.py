def main():
	sum=0.0
	count=0
	moredata="yes"
	while moredata[0]=='y':
		x=eval(input('Enter a number>>'))
		sum=sum+x
		count=count+1
		moredata=input("Do you have more number(yes or no)?")
	print("\n The average of the number in",sum/count)	

main()	