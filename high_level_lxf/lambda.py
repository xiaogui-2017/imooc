# -*- coding=utf-8 -*-
def is_not_empty(s):
    return s and len(s.strip()) > 0


# 不用遍历后边的列表
print filter(lambda i: i and len(i.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])

print filter(lambda x: x and len(x.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
