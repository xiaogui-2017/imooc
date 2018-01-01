# -*- coding=utf-8 -*-
def is_not_empty(s):
    # 不要None， 也不要长度为0的
    # strip取出空字符'\n' '\r' '\t' ' '
    return s and len(s.strip()) > 0


# filter自动过滤None
# todo 如何免输git帐号和密码
s_filter = filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
print s_filter
