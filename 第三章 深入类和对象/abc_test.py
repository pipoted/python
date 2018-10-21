# coding=utf-8

# 检查某个类中是否有某个方法

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['xiao', 'xiaojian'])
print(hasattr(com, '__len__'))
print(len(com))

# 在某些情况先判断对象的类型
from collections.abc import Sized

print(isinstance(com, Sized))

# 强制某些子类必须实现某些方法
# 实现一个抽象基类
import abc


class CacheBase(metaclass=abc.ABCMeta):
    # 在初始化时就能够发现异常
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):

    def get(self, key):
        pass

    def set(self, key, value):
        pass
# class CacheBase:
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#
#
# class RedisCache(CacheBase):
#     # 必须实现抽象基类中的方法
    # 只有在调用的时候才会发现异常
#     def get(self, key):
#         pass
#
#     def set(self, key, value):
#         pass
