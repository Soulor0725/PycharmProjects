# str = 'hello world'
# print(str)
# str1 = str.replace('hello','python')
# print(str1,len(str1))
# print(dir(str))

# str1 = b'\xe6\x89\x8e\xe5\xbf\x83\xe4\xba\x86\xef\xbc\x8c\xe8\x80\x81\xe9\x93\x81'
# print(str1.decode('utf8'))

# print(dir(list))
# list.sort()


# def countchar(str):
#     charmap = {}
#     # 初始化字典
#     for i in range(26):
#         charmap[chr(i+65)] = 0
#     # 统一大小写
#     str = str.upper()
#     # 统计个字母出现次数
#     for c in str:
#         if ord("A") <= ord(c) <= ord("Z"):
#             charmap[c] += 1
#         else:
#             continue
#     # print(charmap)    
#     # charlist = []
#     # for i in range(26):
#     #     charlist.append(charmap[chr(i+65)]) 
#     # print(charlist)               
#     return [charmap[chr(i+65)] for i in range(26)]


# if __name__ == "__main__":
#     str = input()
    # print(countchar(str))



# -*- coding:utf-8 -*-    
import math  
  
def prime(n):  # 判断是否为素数  
    if n < 2:  
        return False  
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:  
            return False  
    return True  
  
def monisen(maxn):
    if maxn>8:
       print('不支持')
       exit(0)     

    prime_dic = {}  
    prime_list = []  
    n = 10000  
    for i in range(2, n + 1):  
        prime_dic[i] = 1  
    for i in range(2, int(n ** .5) + 1):  
        for j in range(i * i, n + 1, i):  
            if prime_dic[i] == 1:  
                prime_dic[j] = 0  
    for k, v in prime_dic.items():  
        if v == 1:  
            prime_list.append(k)  
              
    for i in prime_list: 
        mon = 2 ** i - 1 
        
        if prime(mon):  
            maxn = maxn - 1  
            if maxn <= 0:  
                return mon  
                  
  
if __name__ == "__main__":
    print(monisen(int(input())))
