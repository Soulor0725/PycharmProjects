# r = lambda x:x+x
# print (r(5))

# def fib(n):
#     a,b = 0,1
#     count=1
#     while count<n:
#         a,b=b,a+b
#         count+=1
#     print(a)

# fib(9)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)


print(fib(9))

import os
print(os.getcwd())

import math
print(dir(math))

help(math.ceil)

with open('example.txt') as f:
    for line in f:
        print(line,end=' ')