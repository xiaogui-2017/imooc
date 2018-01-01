# -*- coding=utf-8 -*-
def count():
    """
    返回闭包不能引用循环变量，请改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数。
    :return:
    """
    fs = []
    for i in range(1, 4):
        def f(j):
            """
            把i传给内部函数f,而不是直接塞给他, 内部函数f一定要接受enclosing参数
            :param j:
            :return:
            """
            def g():
                return j*j
            return g
        # 把i传给内部函数f,而不是直接塞给他, 内部函数一定要接受参数,
        r = f(i)  # i给啦line 9的j
        fs.append(r)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()
