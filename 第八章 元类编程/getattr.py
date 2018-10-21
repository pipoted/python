# coding=utf-8
# __getattr__, __getattribute__
# __getattr__ 查找不到属性时调用
from datetime import date


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        print('not find attr')

    def __getattribute__(self, name):
        return 'xiao'


if __name__ == "__main__":
    user = User('xiao', date(year=1997, month=2, day=8))
    print(user.age)
