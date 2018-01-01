# -*- coding=utf-8 -*-
def calc_prod(lst):
    """
    编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
    :param lst:
    :return:
    """
    def wrapper():
        """
        返回函数可以计算参数的乘积。
        :return:
        """
        s = 1
        for i in lst:
            s *= i
        # 一定要有返回值
        return s
    return wrapper
f = calc_prod([1, 2, 3, 4])
print f()
