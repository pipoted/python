# coding=utf-8

class Date:

    # 构造函数
    def __init__(self, year, mouth, day):
        self.year, self.mouth, self.day = year, mouth, day

    def __str__(self):
        return '{year}/{mouth}/{day}'.format(year=self.year, mouth=self.mouth,
                                             day=self.day)

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(data_str):
        year, mouth, day = tuple(data_str.split('-'))
        return Date(int(year), int(mouth), int(day))

    @classmethod
    def from_string(cls, date_str):
        year, mouth, day = tuple(date_str.split('-'))
        return cls(int(year), int(mouth), int(day))


if __name__ == '__main__':
    new_day = Date(2018, 10, 19)
    new_day.tomorrow()
    print(new_day)

    date_str = '2018-10-19'
    year, mouth, day = tuple(date_str.split('-'))
    print(year, mouth, day)

    # 用staticmethod完成初始化
    new_day_test = Date.parse_from_string(date_str)
    print(new_day_test)

    # 用classmethod完成初始化
    new_day = Date.from_string(date_str)
    print(new_day)
