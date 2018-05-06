#计算个人BMI值
from math import *

heightValue,weightValue=eval(input("please input a person's height and weight:"))
BMI=weightValue/pow(heightValue,2)

if BMI<18.5:
	print("BMI:{} 建议：国际18.5---国内18.5".format(BMI))
elif(BMI<24.0):
	print("BMI:{} 建议：国际18.5~25---国内18.5~24".format(BMI))	
elif(BMI<28):
	print("BMI:{} 建议：国际25~30---国内24~28".format(BMI))		
else:
	print("BMI:{} 建议：国际30---国内28".format(BMI))