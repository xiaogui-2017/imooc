# -*- coding=utf-8 -*-
def is_not_empty(s):
    # 不要None， 也不要长度为0的
    return s and len(s.strip()) > 0


# filter自动过滤None
s_filter = filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
print s_filter
