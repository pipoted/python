# coding=utf-8

my_list = [1, 'a']

from collections import abc

a = [1, 2]
b = a + [3, 4]
print(b)

a += (3, 4)
print(a)
