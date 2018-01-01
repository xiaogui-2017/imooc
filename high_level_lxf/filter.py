# -*- coding=utf-8 -*-
import math


def is_not_empty(s):
    # 不要None， 也不要长度为0的
    # strip取出空字符'\n' '\r' '\t' ' '
    return s and len(s.strip()) > 0


def is_sqr(x):
    """返回开根后为整数"""
    # todo 如何判断是整数 math.sqrt(返回的结果是浮点数)
    """
        1.先转换成int
        2.然后逆向思维，看谁的平方等于100内的数
    """
    r = int(math.sqrt(x))
    """
        可以简写, return r*r == x
        if r*r == x:
            return x
    """
    return r*r == x


# filter自动过滤None
# 免输git帐号和密码,3.新建'.gitconfig' 文件
print(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END']))
print("100内开根号是整数列表是%s" % filter(is_sqr, range(1, 101)))
