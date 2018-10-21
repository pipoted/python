# coding=utf-8

def exe_try():
    try:
        print('this is start')
        raise KeyError
    except KeyError as e:
        print('key error')
        return 2
    # else:
    #     # 如果try语句块中没有抛出异常则执行else语句块中内容
    #     print('other error')
    finally:
        # 无论有没有抛出异常都会执行该语句块
        print('finally')
        return 3


# 上下文管理器
class Sample:
    def __enter__(self):
        # 获取资源
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print('exit')

    def do_something(self):
        print('do some thing')


if __name__ == '__main__':
    result = exe_try()
    print(result)

    with Sample() as sample:
        sample.do_something()
