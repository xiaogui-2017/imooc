# -*- coding=utf-8 -*-
import time


def performance(ms):
    """
    @performace增加一个参数，允许传入's'或'ms'：
    :param ms:
    :param unit:
    :return:
    """
    def ourter(unit):
        def wraper(*args, **kwargs):
            s_time = time.time()
            r = unit(*args, **kwargs)
            e_time = time.time()
            # 之前的思路不变， 装饰器的参数ms,最内部函数依然能够调用
            print '执行的时间是%s%s' % (e_time-s_time, ms)
            return r
        return wraper
    return ourter


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)
