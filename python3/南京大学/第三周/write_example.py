# coding:utf-8
# f = open('firstpro.txt','w')
# f.write('hello world')
# f.close()

# with open('firstpro.txt','w') as f:
#     f.write('make in baidu')

# read file
# with open('firstpro.txt') as f:
#     # p1 = f.read(4)
#     p2 = f.read()
#     # print(p1)
#     print(p2)

# with open('firstpro.txt') as f:
#     ret = f.readlines()
#     print(ret)

with open('firstpro.txt') as f:
    rets = f.readlines()
    for i in range(0,len(rets)):
        rets[i] = str(i+1)+'-'+rets[i]
with open('twopro.txt','w') as f:
    f.writelines(rets)