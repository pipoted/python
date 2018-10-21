# coding=utf-8


def ask(name='xiao'):
    print(name)


def decorator_func():
    print("dec start")
    return ask


# my_func = ask
# my_func('xiaojian')


class Person:
    def __init__(self):
        print('xiao')


class Test:
    def __init__(self):
        print('hello')


class Persong:
    def __new__(self):
