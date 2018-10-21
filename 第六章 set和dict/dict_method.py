# coding=utf-8

# clear
my_dict = {'name': 'xiao'}
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# copy, 返回浅拷贝, 不会进行嵌套拷贝
new_dict = my_dict.copy()

import copy

new_dict = copy.deepcopy(my_dict)

# fromkeys

new_list = ['xiao', 'xiaojian']
new_dict = dict.fromkeys(new_list, {'xiao': 21})
print(new_dict)

for key, value in new_dict.items():
    print(key, value)
