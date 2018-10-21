# # coding=utf-8
# # 不建议继承list和dict
#
# class MyDict(dict):
#     def __setitem__(self, key, value):
#         super(MyDict, self).__setitem__(key, value * 2)
#
#
# my_dict = MyDict(one=1)
# my_dict['one'] = 1
# print(my_dict)
#
# from collections import UserDict
#
#
# class MyDict(UserDict):
#     def __setitem__(self, key, value):
#         super(MyDict, self).__setitem__(key, value * 2)
#
#
# my_dict = MyDict(one=1)
# print(my_dict)

from collections import defaultdict

my_dict = defaultdict(dict)

my_value = my_dict['xiao']
print(my_value)
