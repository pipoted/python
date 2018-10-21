# coding=utf-8

class A(object):
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) is A)
