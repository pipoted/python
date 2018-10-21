# coding=utf-8
# set集合, 无序， 没有重复元素
# frozenset 不可变集合

s = set('ababa')
print(s)
s = set(['a', 'b', 'a'])
print(s)

s = {'a', 'b', 'a'}
print(type(s), s)

another_set = {'cef'}
re_set = s.difference(another_set)
print(re_set)

# set性能很高

if 'c' in re_set:
    print('yes')
else:
    print('no')

print(s.issubset(re_set))
