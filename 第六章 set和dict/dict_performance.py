# coding=utf-8

# dict的查找性能远远高于list的查找
# 在list中，随着list的增大，查找时间也随着增大
# 在dict中查找元素不会随着dict的增大而增加耗时

# dict的key与set的值都必须是可hash的
# 不可变对象都是可hash的，如str，frozenset，tuple, 自己实现的类实现__hash__函数

# dict的内存花销大,但是查询速度快，自定义对象，或者Python内部的对象都是用dict包装的
# dict的存储顺序与元素的添加顺序有关
# 添加数据有可能改变已有数据的顺序
