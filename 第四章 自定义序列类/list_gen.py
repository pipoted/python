# coding=utf-8

# 列表生成式(列表推导式）
# 提取出1到20的奇数
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)


def hadle_item(item):
    return item * item


odd_list = [hadle_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)

# 列表生成式的性能高于列表操作

# 生成器表达式

odd_gen = (i for i in range(21) if i % 2 == 1)
print(type(odd_gen), odd_gen)
print(list(odd_gen))
for item in odd_gen:
    print(item)

print(list(odd_gen))

# 字典推导式
my_dict = {
    'xiao': 18,
    'xiaojian': 22,
    'xiaozhixin': 21,
}
reversed_dict = {value: key
                 for key, value in my_dict.items()}

print(reversed_dict)

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set), my_set)

