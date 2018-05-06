# coding:utf-8
# def cal(count,price):
#     return count*price

# try:
#     count = int(input("苹果数量:"))
#     price = float(input("苹果单价:"))
#     print(cal(count,price))
# except Exception as err:
#     print(err)

# k = 50
# count = 0
# while k > 1:
#     count+=1
#     # print(k)
#     k = k//2
# print(count)

# import random
# print(random.random())

sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i % 10 == 5:
        break
    sum += i
print(sum)


# def f(x):
#     a = 7
#     print(a+x)

# a = 5
# f(3)
# print(a)    

# def my_power(x,n=2):
#     s=1
#     while n>0:
#         n-=1
#         s=s*x 
#     return s    
# print(my_power(-3))


# a=3
# print(a**b)