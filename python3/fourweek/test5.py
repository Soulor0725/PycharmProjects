#文件输入
from string import *

def main():
	filename=input("")
	infile=open(filename,'r')
	sum =0.0
	count=0
	line=infile.readline()
	while line!="":
		for xStr in line.split(","):		
			sum+=eval(xStr)
			count+=1
		line=infile.readline()
	print("平均值是:",sum/count)
	
main()		