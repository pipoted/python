# coding=utf-8

from datetime import date, datetime
import numbers


class IntField(object):
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            return ValueError('int value need')
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __delete__(self, instance):
        pass


class User:
    age = IntField()


class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value


if __name__ == '__main__':
    user = User()
    user.age = 30
    print(user.age)

    print(getattr(user, 'age'))
