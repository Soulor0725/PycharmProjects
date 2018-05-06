# from pandas import Series
# sa = Series(['a', 'b', 'c'], index = [0, 1, 2])
# sb = Series(['a', 'b', 'c'])
# sc = Series(['a', 'c', 'b'])
# print(sa*3 + sc*2)

# 有5名某界大佬xiaoyun、xiaohong、xiaoteng、xiaoyi和xiaoyang，其QQ号分别是
# 88888
# 5555555
# 11111
# 12341234
# 1212121

# 程序框架如下：

# def find_person(dict_users, strU):
#     strUser = ''
#     for user in dict_users:
#         if strU==user:
#             strUser = dict_users[user]

#     if len(strUser):
#         return dict_users[user]
#     else:
#         return 'Not Found'

# if __name__ == "__main__":
#     dict_users = {
#         "xiaoyun":"88888",
#         "xiaohong":"5555555",
#         "xiaoteng":"11111",
#         "xiaoyi":"12341234",
#         "xiaoyang":"1212121"}
#     strU =  input()
#     print(find_person(dict_users, strU))


import collections

def countfeq(s):
    s_list = s.split('/') 
    [s_list.remove(item) for item in s_list if item in '.‘’“”']
    return collections.Counter(s_list)
   
if __name__ == "__main__":
   s = input()
   s_dict = countfeq(s)
   print(len(s_dict.keys()))

   
# s = 'Spring/is/coming/./Spring/is/coming/.'
# s_list = s.split('/') 
# [s_list.remove(item) for item in s_list if item in '.‘’“”']
# print(collections.Counter(s_list))