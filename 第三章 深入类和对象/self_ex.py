# coding=utf-8
# 自省：通过一定的机制来查询到对象的内部结构

class Person:
    name = 'user'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student('imooc.com')

    # 通过__dict__查询属性
    print(user.__dict__)
    print(Person.__dict__)
    print(user.name)

    print(dir(user))
