# coding=utf-8

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]


company = Company(['xiao', 'xiaojian', 'xiaozhixin'])

employee = company.employee

for em in employee:
    print(em)

for em in company:
    print(em)

