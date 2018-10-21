# coding=utf-8

class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        # 使一个对象变成可切片对象
        import numbers
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name,
                       company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name,
                       company_name=self.company_name,
                       staffs=[self.staffs[item]])

    def __len__(self):
        return len(staffs)

    def __iter__(self):
        return iter(staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ['xiao', 'xiaojian', 'xiaozhixin']
group = Group(group_name='group_one', company_name='com', staffs=staffs)
sub_group = group[:-1]
print(sub_group)
print(group[0])
print(len(group))

if 'xiao' in group:
    print('yes')

for user in group:
    print(user)

reversed(group)

for user in group:
    print(user)
