# -*- coding=utf-8 -*-
def cmp_ignore_case(s1, s2):
    """
    对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。
        1.排序时转换成一致的
    sorted()也可以对字符串进行排序，字符串默认按照ASCII大小来比较：
    """
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 > s2:
        return 1
    if s1 < s2:
        return -1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
