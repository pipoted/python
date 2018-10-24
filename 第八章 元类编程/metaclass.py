# coding=utf-8

# 类也是对象，type创建类的类
def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return 'user'

        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return 'company'

        return Company


# type动态创建类
# User = type('User', (), {})

def say(self):
    return 'i am user'
    # return self.name


class BaseClass:
    def answer(self):
        return 'i am baseclass'


class MetaClass(type):
    pass


class User(metaclass=MetaClass):
    pass


# python中创建类实例化过程，首先寻找metaclass, 通过metaclass创建user类
# type去创建类对象，实例


if __name__ == '__main__':
    # MyClass = create_class('user')
    # my_object = MyClass()
    # print(my_object)
    User = type('User', (BaseClass,), {'name': 'user', 'say': say})
    my_obj = User()
    print(my_obj.name)
    print(my_obj.say())
    print(my_obj.answer())

# 元类是创建类的类 type->class(对象)->对象
