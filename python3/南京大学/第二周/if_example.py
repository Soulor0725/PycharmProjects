# sd1 = input('input a number:')
# sd2 = 2

# if sd1 == sd2:
#     print('equal')
# else:
#     print('no equal')

from random import randint

x = randint(0, 300)
x = int(x)
print(x)

digit = input('please input a number:')

if digit > x:
    print('big')
elif digit < x:
    print('small')
else:
    print('equal')
