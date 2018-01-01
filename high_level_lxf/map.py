# -*- coding=utf-8 -*-
"""map高阶函数"""


def format_name(s):
    return s.capitalize()
    # 不是captalize


print map(format_name, ['adam', 'LISA', 'barT'])
