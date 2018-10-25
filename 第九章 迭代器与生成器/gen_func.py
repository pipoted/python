# coding=utf-8

# 生成器函数,函数中只要含有yield关键字，就是生成器函数


def gen_func():
    yield 1
    yield 2
    yield 3
# 惰性求值，延迟求值


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1


def func():
    return 1


if __name__ == '__main__':
    # 生成器对象,python编译字节码时生成的
    print(fib(index=10))
    print(fib2(index=10))
    for date in gen_fib(index=10):
        print(date)
