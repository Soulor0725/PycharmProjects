# sumA = 0
# i = 1
# while True:
#     sumA += i
#     i +=1

#     if sumA > 10:
#         break
# print(sumA, i)

# 输出2-100之间的素数
from math import sqrt
j = 2
while j <= 100:
    i = 2
    k = int(sqrt(j))
    while j <= k:
        if j % i == 0:
            break
        i =i+ 1
    if i > k:
        print('hi')
        # print(j, end='')
    j += 1
    print(j)