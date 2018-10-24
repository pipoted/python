# coding=utf-8

class User:
    # 如果new方法不返回对象，则不会调用init函数
    def __new__(cls, *args, **kwargs):
        # new是用来控制对象的生成过程，在对象生成之前
        print('in new')
        return super().__new__(cls)

    def __init__(self, name):
        # init是用来完善对象的
        print('in init')
        self.name = name


if __name__ == '__main__':
    user = User(name='xiao')
