score=eval(input("please a score:"))

if score>60.0:
	grade='D'
elif score>=70:
	grade='C'
elif score>=80:
	grade='B'		
elif score>=90.0:
	grade='A'

print("grade:",grade)		