def main():
 	# print("hello world")
	fname=input("Enter filename:")
	infile=open(fname,"r")
	data=infile.read
	print(data)
	# fname.close()

main()