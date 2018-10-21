# coding=utf-8

class A:
    name = 'A'

    def __init__(self):
        self.name = 'obj'


a = A()
print(a.name)


class D:
    pass


class B(D):
    pass


class C(D):
    pass


class A(B, C):
    pass

print(A.__mro__)

# 新式类：默认继承object

