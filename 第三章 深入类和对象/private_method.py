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


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1997, 2, 8))
    print(user.get_age())
