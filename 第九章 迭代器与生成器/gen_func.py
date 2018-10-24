# coding=utf-8

# 生成器函数,函数中只要含有yield关键字，就是生成器函数


def gen_func():
    yield 1
    yield 2


def func():
    return 1


if __name__ == '__main__':
    # 生成器对象,python编译字节码时生成的
    gen = gen_func()
    for item in gen:
        print(item)
    re = func()
    pass
