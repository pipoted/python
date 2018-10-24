# coding=utf-8

# 什么是迭代协议
# 迭代器，访问集合内元素的一种方式，一般用来遍历数据
# 迭代器与下标访问时不同的，迭代器是不能返回的, 迭代器提供了一种惰性访问数据的方法

from collections.abc import Iterable, Iterator

a = [1, 2]
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
iter(a)
print(isinstance(iter(a), Iterator))
