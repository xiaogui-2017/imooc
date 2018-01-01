# -*- coding=utf-8 -*-
import time


def performance(f):
    """
    它可以打印出函数调用的时间。
    总结：
        1.用×args，××kwargs就能够提高通用性
        2.一定要有返回值, 内部返回函数调用结果， 外部返回内部的那个函数名（变量）
            2.1 不直接return f(*args, **kwargs)是因为这样的话没法断定执行的时间
    :param f:
    :return:
    """

    def wraper(*args, **kwargs):
        start_time = time.time()
        # 怎么把参数传给他
        r = f(*args, **kwargs)
        end_time = time.time()
        print "执行时间为%s" % (end_time - start_time)
        return r

    return wraper


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)
