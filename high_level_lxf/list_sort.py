# -*- coding=utf-8 -*-
class Person(object):
    """
    sorted():函数对所有可迭代的对象进行排序操作。

    sort与sorted区别：
        sort 是应用在 list 上的方法,返回原来的列表;
        sorted 可以对所有可迭代的对象进行排序操作， 返回新的列表。

    语法：
    sorted(iterable[, cmp[, key[, reverse]]])
        iterable -- 可迭代对象。
        cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0
        key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
        reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

    """
p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]

# L1是可迭代对象
L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))

print L2[0].name
print L2[1].name
print L2[2].name
