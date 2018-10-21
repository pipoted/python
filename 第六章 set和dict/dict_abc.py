# coding=utf-8

from collections.abc import Mapping, MutableMapping

# dict属于mapping类型

a = {}
print(isinstance(dict, Mapping))
print(isinstance(dict, MutableMapping))
print(isinstance(a, MutableMapping))
