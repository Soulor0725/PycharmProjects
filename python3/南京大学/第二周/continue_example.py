from math import sqrt


def isprime(x):
    #'apple operation + to argument'
    '判断是否为素数'
    if x == 1:
        return False
    k = int(sqrt(x))
    for j in range(2, k+1):
        if x % j == 0:
            return False
    return True


for i in range(2, 101):
    if isprime(i):
        print(i, end=' ')
