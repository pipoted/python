# coding=utf-8

from collections.abc import Iterator


class Company:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    # def __getitem__(self, item):
    #     return self.employee_list[item]

    def __iter__(self):
        return MyIterator(self.employee_list)


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return word


# 真正返回迭代值的逻辑


if __name__ == '__main__':
    company = Company(['xiao', 'tom', 'john'])
    for item in company:
        print(item)
