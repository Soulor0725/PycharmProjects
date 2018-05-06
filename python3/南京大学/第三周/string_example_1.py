# string1 = 'hello, world!'
# string2 = string1[:7]+'Python!'
# print(string2)
# sum = 0
# for i in string2:
#     if i in '.,?!':
#         sum += 1
# print('sum f=', sum)

# print(dir(str))

# string = 'Blowing the wind'
# print(string.replace('the','this'))
# strings = string.split(' ')
# print(strings)
# string_joins = ' '.join(strings)
# print(string_joins)

# string = b'\xe6\x89\x8e\xe5\xbf\x83\xe4\xba\x86\xef\xbc\x8c\xe8\x80\x81\xe9\x93\x81'
# string_encode = string.decode('utf-8')
# print(string_encode)

# print([x*x for x in range(10)])

# print(dir(tuple))
# print(dir(list))

def foo(arg1,*argrs):
    print(arg1)
    print(argrs)

foo('hello','baidu','xiaomi','vivo','oppo')    



